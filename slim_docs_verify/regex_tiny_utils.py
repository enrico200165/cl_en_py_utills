
import re

OPT_WHITESPACE = "[\s]*"
VAL_IN_BRACKETS = "\([\s]*([0-9]*)[\s]*\)"


NUMBER = "[\s]*([0-9]*)[\s]*"
CAPT_NUMBER = NUMBER
VAL2_IN_BRACKETS = "\(" \
    +OPT_WHITESPACE+CAPT_NUMBER+OPT_WHITESPACE+","\
    +OPT_WHITESPACE+CAPT_NUMBER +OPT_WHITESPACE\
    +"\)"+OPT_WHITESPACE+"$"


def cap_grp(s, is_optional):
    tmp = "({})".format(s)
    if is_optional:
        tmp += "?"
    return tmp


def pref_cap_grp(s, is_optional):

    if is_optional:
        tmp = "(?:_({}))?".format(s)
    else:
        tmp = "_({})".format(s)
    return tmp


def non_cap_grp(s, is_optional):
    tmp = "(?:{})".format(s)
    if is_optional:
        tmp += "?"
    return tmp


def dbtype_with_1size(root_word, str_to_check):
    """ checks if it matches xxx(N) and retusn
    (True/False, N)
    """
    ptrn = root_word+"\([\s]*([0-9]*)[\s]*\)"
    captured_groups = re.findall(ptrn,str_to_check)
    if captured_groups is not None and len(captured_groups) == 1:
        num_val = int(captured_groups[0])
        return (True, num_val)
    else:
        return (False, None)


def dbtype_with_2size(root_word, str_to_check):
    """ checks if it matches xxx(N) and retusn
    (True/False, N)
    """
    ptrn = root_word+VAL2_IN_BRACKETS
    captured_groups = re.findall(ptrn,str_to_check)
    if captured_groups is not None and len(captured_groups) >= 1:
        matched_vals = []
        for tmp in captured_groups:
            if isinstance(tmp,tuple):
                for t in tmp:
                    matched_vals.append(t)
            else:
                matched_vals.append(tmp)
        num_val1 = int(matched_vals [0])
        num_val2 = int(matched_vals[1])
        return (True, num_val1, num_val2)
    else:
        return (False, None, None)
