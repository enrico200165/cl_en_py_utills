
import re
import sys
import logging


import global_defs as g
import e2bi_patterns
import legal_systems as ls
import regex_tiny_utils as ru


"""
----- DIFETTI CERTI E PROBABILI -----------------
La gestione delle parti opzionali, ex  T_<var>[_AA/BB/CC] implementata
di corsa, male ed ad-ho per il caso banale
se funziona funziona solo per il caso più banale
implementarla bene è o molto complesso o implica ristrutturare quasi tutto 
il meccanismo

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

log = g.init_logging()




class PatternVariableValidation(object):
    """ PREMESSA: ogni parte può contenere una o più variabili
    ex. in MV_ODS_{<sistema sorgente>/<sistema BI>/COM}_{DT/LV/LH/LM/SC}_<label>
    la parte 3 contiene una variabile: {<sistema sorgente>/<sistema BI>/COM}
    in T_STG_{<sistema sorgente>/<sistema BI>}_{DT/LV/LH/LM/SC/DL}_<nome tabella A>2<nome tabella B>
    la parte 5 contiene 2 variabili
    per ogni parte che contiene almeno una variabile devo salvare
    lista costanti e lista variabili, vedi doc algoritmo in testa modulo

    SCOPO: contenere UNA posizione variabile, in cui possono essere più variabili in alternativa
    ex. _{<sistema sorgente>/<sistema BI>
     lista eventuali costanti
    USO: contenuti consultati dopo il matching(capturing)
    CONTEXT: una parte conterrà uno di questi oggetti per ogni posizione variabile
    """
    def __init__(self, part_string, pos):
        self._part = part_string
        self._altern_vars_for_single_position = []
        self._consts = []
        self._var_slot_pos = pos # num of corresponding capturing group
        # NB capturing group, not part, a part can have more than one
        # variable, this is the index of the capturing group, global
        # not of the part

    @property
    def vars(self):
        pass
        return self._altern_vars_for_single_position


    @property
    def var_slot_pos(self):
        pass
        return self._var_slot_pos

    def add_vars(self, vars):
        if not isinstance(vars, list):
            vars = [vars]
        self._altern_vars_for_single_position.extend(vars)

    @property
    def consts(self):
        pass
        return self._consts

    def add_consts(self, consts):
        if not isinstance(consts, list):
            consts = [consts]
        self._consts.extend(consts)


    def is_matched(self, variable_part_value):

        # check if one of the eventual constants, like in
        # _{<var1>/CONST1/CONST2}
        if variable_part_value in self._consts:
            return True

        # check the variables, the variable name tells
        # which domain to check
        for cur_alternative_var  in self._altern_vars_for_single_position:
            if "istem" in cur_alternative_var:
                if "orgent" in cur_alternative_var:
                    if variable_part_value in ls.source_systems:
                        return True
                elif "estin" in cur_alternative_var:
                    if variable_part_value in ls.destination_systems:
                        return True
                else:
                    log.warning("unrecognized variable: <"+cur_alternative_var+">")

        return False


    def dumpToStr(self, i = None):
        s ="["+str(i)+"] " if i is not None else ""
        s += "pos(" + str(self.var_slot_pos) + ")"
        s += " part: "+self._part
        s += " - vars:" +", ".join(self._altern_vars_for_single_position)
        s += " - consts: "+", ".join(self._consts)
        return s


class PatternPartValidation(object):
    """ a part can correspond to more than 1 variable
    this is the list of the (var) validations for one part
    """

    def __init__(self, var_validation, part, part_str):
        self._var_pos_validations = [var_validation]
        self._part_nr = part # part of the mask
        self._part_str = part_str

    def add_var(self, var_validation):
        self._var_pos_validations.append(var_validation)

    def dumpToStr(self, verbose = None):
        s = ""
        if verbose:
            s += "part validation, "
        s += "part["+str(self._part_nr) + "] " + self._part_str
        if verbose:
            for i, v in enumerate(self._var_pos_validations):
                s += "\nvar val[{}] ".format(i) + v.dumpToStr(i)
        return s

    @property
    def variables_positions(self):
        pass
        return self._var_pos_validations


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
            log.error("exiting")
            sys.exit(1)
        pass

    @property
    def e2bi_pattern(self):
        return self._e2bi_pattern

    def adjust_e2bi_pattern(self, s):
        """ eventual changes/adjustments to make subsequen partsing easier """

        # rimuovi _ dentro < _ >
        underscore = ".*<.*_.*>"
        inside = False
        if re.match(underscore, s):
            copy = ""
            for c in s:
                if c == "<":
                    inside = True
                if c == ">":
                    inside = False
                if c == "_" and inside:
                    c = "-"
                copy += c
            s = copy
        return s


    def split_e2bi_patterm(self, e2bipattern):
        """ splits a patter into elementary parts, ex "T_AA_<var_BB>"
        in ["T", "AA", "<var>", "BB"]
        """

        parts = []
        part_is_optional = []

        opzionale = False
        in_variable = False # between <>
        i = 0
        cur_part = ""
        while i < len(e2bipattern):
            c = e2bipattern[i]

            # get context
            if c == "[":
                parts.append(cur_part)
                part_is_optional.append(opzionale)
                opzionale = True
                cur_part = "{"
                if i+2 < len(e2bipattern) and e2bipattern[i+1] == "_":
                    i = i+2 # skip _ dato che già splittato
                else:
                    log.error("[ non seguita da _: caso non gestito")
                continue
            if c == "]":
                c = "}"  # attenzione se in futuro controllo per il vero }
                # opzionale = False
            if c == "<":
                in_variable = True
            if c == ">" and in_variable:
                in_variable = False

            if c == " " and not in_variable:
                log.warning("found space outside variable, pattern: "+e2bipattern)
                i = i+1
                continue

            if c == "_" and not in_variable:
                parts.append(cur_part)
                part_is_optional.append(opzionale)
                opzionale = False
                cur_part = ""
                i = i+1
                continue

            cur_part += c
            i = i+1

        parts.append(cur_part)
        part_is_optional.append(opzionale)

        return (parts, part_is_optional)


    def generate_regex(self, e2bipattern = None):
        """ itera sui pattern e li trasforma in regez
        now la trasformazione è parziale
        now opera su un dato globale
        TODO
        """

        if e2bipattern is None:
            e2bipattern = self._e2bi_pattern

        e2bipattern = self.adjust_e2bi_pattern(e2bipattern)
        (e2bipattern_parts, part_is_optional) = self.split_e2bi_patterm(e2bipattern)
        new_parts = []
        matching_group_idx = 0 # track matching groups
        prefix = ""
        for p_idx, part in enumerate(e2bipattern_parts):
            if p_idx > 0:
                prefix = "_"
            if False:
                pass
            elif re.match(g.RE_VARIABLE_SIMPLE+"2"+g.RE_VARIABLE_SIMPLE, part):
                # per <nome tabella A>2<nome tabella B>

                twovars = part.split("2")
                # generate var entry, 2 variables here
                var1_validation = PatternVariableValidation(part, matching_group_idx)
                matching_group_idx = matching_group_idx+1
                var1_validation.add_vars(twovars[0])
                part_validation = PatternPartValidation(var1_validation, p_idx, part)

                var2_validation = PatternVariableValidation(part, matching_group_idx)
                matching_group_idx = matching_group_idx+1
                var2_validation.add_vars(twovars[1])

                part_validation.add_var(var2_validation)
                log.debug(part_validation.dumpToStr())
                self._parts_validation.append(part_validation)

                new_parts.append(prefix+g.RE_CAPTURE_GROUP_SIMPLE+"2"+g.RE_CAPTURE_GROUP_SIMPLE) # part of our regest

            elif re.match("^"+g.RE_VARIABLE_SIMPLE+"$", part):
                # generate var entry, 1 variable here
                var_validation = PatternVariableValidation(part, matching_group_idx)
                matching_group_idx = matching_group_idx+1
                var_validation.add_vars(part)
                # add part validation
                part_validation = PatternPartValidation(var_validation, p_idx, part)
                self._parts_validation.append(part_validation)

                new_parts.append(prefix+g.RE_CAPTURE_GROUP_SIMPLE) # part of our regest

            elif re.match("\{.*\}", part):
                part = part[1:-1] # remove {}
                assert len(part) > 0
                if not re.match(g.RE_VARIABLE_SIMPLE, part): # only constants ?

                    # qui facciamo una gestione ad hoc delle alternative
                    alternatives = part.split("/")
                    tmp = ""
                    for a in alternatives:
                        tmp += "_"+a+"|"
                    tmp = tmp[:-1]
                    tmp = ru.non_cap_grp(tmp, part_is_optional)
                    new_parts.append(tmp)
                else: # mix of constants and vars

                    # funziona solo con variabile singola
                    # gestione variabile
                    var_validation = PatternVariableValidation(part, matching_group_idx)
                    matching_group_idx = matching_group_idx+1
                    alternatives = part.split("/")
                    for a in alternatives:
                        if re.match(g.RE_VARIABLE_SIMPLE, a):
                            var_validation.add_vars(a)
                        else:
                            var_validation.add_consts(a)
                    # add part validation
                    part_validation = PatternPartValidation(var_validation, p_idx, part)
                    log.debug(part_validation.dumpToStr())
                    self._parts_validation.append(part_validation)
                    new_parts.append("_"+g.RE_CAPTURE_GROUP_SIMPLE)
            else:
                new_parts.append(prefix+part)

        self._regex_for_mask = "^"+"".join(new_parts)+"$"
        return self._regex_for_mask


    def check_stmt_token(self, token):


        # chedk if token matches regex
        if not self._regex_pattern_compiled.match(token):
            log.warning("{} NOT matches {}".format(self._regex_for_mask, token))
            return False

        # FALL OFF
        log.info("{} matches {}".format(self._regex_for_mask, token))

        # match groups and save matched values
        captured_vals = []
        captured_groups = re.findall(self._regex_pattern_compiled, token)
        if captured_groups is not None and len(captured_groups) > 0:
            log.debug("matched pattern {} on string {}".format(self._regex_for_mask, token))
            for capt_grops in captured_groups:
                    captured_vals.append(capt_grops)
            log.debug("groups: "+", ".join(captured_vals))
            log.debug("matched e2bi pattern vs. string:\n" + self._e2bi_pattern +"\n" + token)

        # check captured versus variables etc
        # iteriamo sulle parti del toeken, e, internamente
        # iteriamo sulle POSIZIONI delle variabili
        # stessa pos può avere più var: ex. _<var1>/<var2>
        # qui dovrei andare sulla variabile
        ret = True
        for i, part_val in enumerate(self._parts_validation):
            log.debug("part["+str(i) + "] "+ part_val.dumpToStr())
            ret = True
            for vp_idx, var_position in enumerate(part_val.variables_positions):
                capt_group_idx_for_var = var_position.var_slot_pos
                if capt_group_idx_for_var > len(captured_groups)-1:
                    log.error("problem with capturing groups")
                matched_group_val = captured_groups[capt_group_idx_for_var]
                if not var_position.is_matched(matched_group_val):
                    log.debug("could not match part: "+part_val.dumpToStr())
                    return False
                else:
                    pass

        # TODO - primo tentativo, controlla che il pattern non match solo parte iniaile
        # TODO FORSE NON NECESSARIO E DA RIMUOVERE
        log.warning(self._regex_for_mask)
        if len(captured_groups[0]) > len(token):
            return false

        return ret


    def dumpToStr(self, verbose = None):

        s = "{PatternWrapper}\n"
        s += "e2bi:   "+self._e2bi_pattern
        if verbose is not None:
            s += "\nregex: "+self._regex_for_mask
            for i, p in enumerate(self._parts_validation):
                s += "\n"+p.dumpToStr()
        return s



def generate_pattern_wrappers(dummy_single_test = None):
    """from list of E2BI patterns build the parse objects that contain
    the objects is needed to check that e2bi pattern against a string
    """
    pattern_wrappers_list = []
    if dummy_single_test is None:
        mask_lines = e2bi_patterns.patterns_list.split("\n")
    else:
        print("working with dummy pattern: "+dummy_single_test)
        mask_lines = [dummy_single_test]
    for l in mask_lines:
        if len(l) == 0:
            continue
        p = PatternWrapper(l)
        # print(p.dumpToStr())
        pattern_wrappers_list.append(p)

    return pattern_wrappers_list


s = "T_STG_sistemasorgente_DT_miatabella"
# p. checkString(s)

