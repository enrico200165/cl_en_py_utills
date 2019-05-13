
import re
import sys

import global_defs as g
import e2bi_patterns
import legal_systems as ls

""""
----- TERMINOLOGIA ------------------------------
qui: in questo file, non necessariamente in altri

pattern: 
specifiche di identificativi, ex.
MV_ODS_{<sistema sorgente>/<sistema BI>/COM}_{DT/LV/LH/LM/SC}_<label>
_ funge da separatore, le parti fra i separatori sono chiamate parti :-)
e qui identificate dalla numerazione
la parte 2 è {<sistema sorgente>/<sistema BI>/COM}
la parte 3 è {DT/LV/LH/LM/SC}

VARIABILI: 
<sistema sorgente> o <sistema BI> sono chiamate qui variabili 


----- ALGORITMO MATCHING ------------------------
Name patterns possono avere parti come
1) {DT/LV/LH/LM/SC} 
2) {<sistema sorgente>/<sistema BI>/COM} 

1) ha costanti chiare e now mappo direttamente in regex
2) 2 contiene variabili, con variabili o liste difficili da gestire 
con mapping  diretto in regex, now gestisco con un capturing group: 
dopo il matching se ho catturato una delle costanti ok, se no controllo 
sul domino delle variabili    per fare questo ho bisogno di salvare:  
    - lista delle costanti, qui ["COM"]
    - lista delle variabili
    se ho catturato una delle costanti OK 
    altrimenti controllo, per ogni variabile, se ho catturato uno dei suoi 
    valori (controllo specifico per singola variabile),
    se una delle variabili è soddisfatta il controllo è ok
"""


class VariableValidation(object):
    """ PREMESSA: ogni parte può contenere una o più variabili
    ex. in MV_ODS_{<sistema sorgente>/<sistema BI>/COM}_{DT/LV/LH/LM/SC}_<label>
    la parte 3 contiene una variabile: {<sistema sorgente>/<sistema BI>/COM}
    in T_STG_{<sistema sorgente>/<sistema BI>}_{DT/LV/LH/LM/SC/DL}_<nome tabella A>2<nome tabella B>
    la parte 5 contiene 2 variabili
    per ogni parte che contiene almeno una variabile devo salvare
    lista costanti e lista variabili, vedi doc algoritmo in testa modulo
    SCOPO: contenitore lista costanti e lista variabili di una parte
    USO: contenuti consultati dopo il matching(capturing)
    CONTEXT: contenuta negli oggeti che gestiscono il matching,
    pressibilmente in lista con corrispondenza posizionale
    """
    def __init__(self, part_string, pos):
        self._part = part_string
        self._vars = []
        self._consts = []
        self._part_pos = pos # num of corresponding capturing group
        # NB capturing group, not part, a part can have more than one
        # variable, this is the index of the capturing group, global
        # not of the part

    @property
    def vars(self):
        pass
        return self._vars


    @property
    def part_pos(self):
        pass
        return self._part_pos

    def add_vars(self, vars):
        if not isinstance(vars, list):
            vars = [vars]
        self._vars.extend(vars)

    @property
    def consts(self):
        pass
        return self._consts

    def add_consts(self, consts):
        if not isinstance(consts, list):
            consts = [consts]
        self._consts.extend(consts)

    def dumpToStr(self, i = None):
        s ="["+str(i)+"] " if i is not None else ""
        s += "pos("+str(self.part_pos)+")"
        s += " part: "+self._part
        s += " - vars:" +", ".join(self._vars)
        s += " - consts: "+", ".join(self._consts)
        return s


class PartValidation(object):
    """ a part can correspond to more than 1 variable
    this is the list of the (var) validations for one part
    """

    def __init__(self, var_validation, part):
        self._var_validations = [var_validation]
        self._part = part # part of the mask

    def add_var(self, var_validation):
        self._var_validations.append(var_validation)

    def dumpToStr(self):
        s = "part validations"
        for i, v in enumerate(self._var_validations):
            s += "\nvar val[{}] ".format(i) + v.dumpToStr(i)
        return s



class PatternWrapper(object):
    """ Logic to control if IDs match
    normal regex do not seem enough, at least at first sight
     it is a wrapper around the naming pattern
    """
    def __init__(self, e2bi_pattern):
        self._e2bi_pattern = e2bi_pattern
        self._parts_validation = []
        self._regex_for_mask = None
        self._regex_pattern_compiled = None
        self.generate_regex()
        if self._regex_for_mask is not None and len(self._regex_for_mask) > 0:
            self._regex_pattern_compiled = re.compile(self._regex_for_mask)
        else:
            print("error - exiting")
            sys.exit(1)
        pass


    def generate_regex(self, mask = None):
        """ itera sui pattern e li trasforma in regez
        now la trasformazione è parziale
        now opera su un dato globale
        TODO
        """

        if mask is None:
            mask = self._e2bi_pattern

        parts = mask.strip().split("_");
        new_parts = []
        matching_group_idx = 0 # track matching groups
        for p_idx, part in enumerate(parts):
            if False:
                pass
            elif re.match(g.RE_VARIABLE_SIMPLE+"2"+g.RE_VARIABLE_SIMPLE, part):
                # per <nome tabella A>2<nome tabella B>

                # generate var entry, 2 variables here
                var1_validation = VariableValidation(part, matching_group_idx)
                matching_group_idx = matching_group_idx+1
                var1_validation.add_vars(part)
                part_validation = PartValidation(var1_validation,p_idx)

                var2_validation = VariableValidation(part, matching_group_idx)
                matching_group_idx = matching_group_idx+1
                var2_validation.add_vars(part)

                part_validation.add_var(var2_validation)
                #print(part_validation.dumpTostr())
                self._parts_validation.append(part_validation)

                pass

            elif re.match("^"+g.RE_VARIABLE_SIMPLE+"$", part):
                # print("var: "+p) variable must use capturing group

                # generate var entry, 1 variable here
                var_validation = VariableValidation(part, matching_group_idx)
                matching_group_idx = matching_group_idx+1
                var_validation.add_vars(part)
                # add part validation
                part_validation = PartValidation(var_validation,p_idx)
                # print(part_validation.dumpTostr())
                self._parts_validation.append(part_validation)

                new_parts.append(g.RE_CAPTURE_GROUP_SIMPLE) # part of our regest

            elif re.match("\{.*\}", part):
                part = part[1:-1] # remove {}
                assert len(part) > 0
                if not re.match(g.RE_VARIABLE_SIMPLE, part): # only constants ?
                    part = part.replace("{", "(").replace("}", ")").replace("/", "|")
                    new_parts.append("("+part+")")
                else: # mix of constants and vars

                    # funziona solo con variabile singola
                    # gestione variabile
                    var_validation = VariableValidation(part, matching_group_idx)
                    matching_group_idx = matching_group_idx+1
                    alternatives = part.split("/")
                    for a in alternatives:
                        if re.match(g.RE_VARIABLE_SIMPLE, a):
                            var_validation.add_vars(a)
                        else:
                            var_validation.add_consts(a)
                    # add part validation
                    part_validation = PartValidation(var_validation,p_idx)
                    #print(part_validation.dumpTostr())
                    self._parts_validation.append(part_validation)

                    new_parts.append(g.RE_CAPTURE_GROUP_SIMPLE)
            else:
                new_parts.append(part)

        self._regex_for_mask = "^"+"_".join(new_parts)+"$"
        #print("{}\n{}\n".format(mask,regex_for_mask ))
        return self._regex_for_mask


    def checkString(self, s):

        # match groups
        captured_vals = []
        groups = re.findall(self._regex_pattern_compiled, s)
        if groups is not None and len(groups) > 0:
            print("matched pattern {} on string {}".format(self._regex_for_mask, s) )
            for tuple in groups:
                for m in tuple:
                    captured_vals.append(m)
            print("groups: "+", ".join(captured_vals))
            pass
        else:
            return False
        # check captured versus variables etc
        ret = True
        print("matched e2bi pattern vs. string:\n" + self._e2bi_pattern+"\n"+s)
        for i, part_val in enumerate(self._parts_validation):
            print("part["+str(i) + "] "+ part_val.dumpToStr())
            found = captured_vals[part_val.part_pos]
            print("againsts captured value: "+found)
            if "sistema" in found:
                if "sorgente" in found:
                    ret = ret and found in ls.destination_systems
                elif "BI" in found:
                    ret = ret and found in ls.destination_systems
            elif "etichetta" in found:
                print("found etichetta: "+found)
            else:
                print("error")
                sys.exit(1)
        return ret


    def dumpToStr(self):

        s = "{PatternWrapper}\n"
        s += "e2bi:  "+self._e2bi_pattern
        s += "\nregex: "+self._regex_for_mask
        for (i,p) in enumerate(self._parts_validation):
            s += "\n"+p.dumpToStr()
        return s



def generate_pattern_wrappers():
    """from list of E2BI patterns build the parse objects that contain
    the objects is needed to check that e2bi pattern against a string
    """
    pattern_wrappers_list = []
    mask_lines = e2bi_patterns.patterns_list.split("\n")
    for l in mask_lines:
        if len(l) == 0:
            continue
        p = PatternWrapper(l)
        # print(p.dumpToStr())
        pattern_wrappers_list.append(p)

    return pattern_wrappers_list



s = "T_STG_sistemasorgente_DT_miatabella"
# p. checkString(s)


