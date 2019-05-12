
import re

import global_defs as g
import masks

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

class PatternPartValidation(object):
    """ PREMESSA: per ogni parte che contiene almeno una variabile devo salvare
    lista costanti e lista variabili, vedi doc algoritmo in testa modulo
    SCOPO: contenitore lista costanti e lista variabili di una parte
    USO: contenuti consultati dopo il matching(capturing)
    CONTEXT: contenuta negli oggeti che gestiscono il matching,
    presubilmente in lista con corrispondenza posizionale
    """
    def __init__(self, part_string):
        self._part = part_string
        self._vars = []
        self._consts = []

    @property
    def vars(self):
        pass
        return self._vars

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
        s += "part: "+self._part
        s += " - vars:" +", ".join(self._vars)
        s += " - consts: "+", ".join(self._consts)
        return s



class PatternWrapper(object):
    """ Logic to control if IDs match
    normal regex do not seem enough, at least at first sight
     it is a wrapper around the naming pattern
    """
    def __init__(self, name):
        self._name = name
        self._parts_validation = []
        self._regex_for_mask = None


    def generate_regex(self, mask = None):
        """ itera sui pattern e li trasforma in regez
        now la trasformazione è parziale
        now opera su un dato globale
        TODO
        """

        if mask is None:
            mask = self._name

        parts = mask.strip().split("_");
        new_parts = []
        for p in parts:
            if False:
                pass
            elif re.match("^"+g.RE_VARIABLE_SIMPLE+"$", p):
                # print("var: "+p) variable must use capturing group
                new_parts.append(g.RE_CAPTURE_GROUP_SIMPLE)

                part_validation = PatternPartValidation(p)
                part_validation.add_vars(p)
                self._parts_validation.append(part_validation)
                pass
            elif re.match("\{.*\}", p):
                p = p[1:-1] # remove {}
                assert len(p) > 0
                if not re.match(g.RE_VARIABLE_SIMPLE, p): # only constants ?
                    p = p.replace("{", "(").replace("}", ")").replace("/", "|")
                    new_parts.append("("+p+")")
                else: # mix of constants and vars
                    part_validation = PatternPartValidation(p)
                    alternatives = p.split("/")
                    for a in alternatives:
                        if re.match(g.RE_VARIABLE_SIMPLE, a):
                            part_validation.add_vars(a)
                        else:
                            part_validation.add_consts(a)
                    self._parts_validation.append(part_validation)
                    new_parts.append(g.RE_CAPTURE_GROUP_SIMPLE)
            else:
                new_parts.append(p)

        self._regex_for_mask = "_".join(new_parts)
        #print("{}\n{}\n".format(mask,regex_for_mask ))
        return self._regex_for_mask


    def dumpToStr(self):

        s = "{PatternWrapper}\n"
        s += "part:  "+self._name
        s += "\nregex: "+self._regex_for_mask
        for (i,p) in enumerate(self._parts_validation):
            s += "\n"+p.dumpToStr(i)
        return s



def generate_regexes():

    pattern_wrappers_list = []
    mask_lines = masks.masks_lines_list.split("\n")
    for l in mask_lines:
        if len(l) == 0:
            continue
        p = PatternWrapper(l)
        #p.elabora()
        p.generate_regex(l)
        print(p.dumpToStr())
        # pattern_wrappers_list.append(p)

    return pattern_wrappers_list



temp_list = generate_regexes()


