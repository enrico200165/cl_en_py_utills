
import re

OPT_WHITESPACE = "[\s]*"
VAL_IN_BRACKETS = "\([\s]*([0-9]*)[\s]*\)"


NUMBER = "[\s]*([0-9]*)[\s]*"
CAPT_NUMBER = NUMBER
VAL2_IN_BRACKETS = "\(" \
    +OPT_WHITESPACE+CAPT_NUMBER+OPT_WHITESPACE+","\
    +OPT_WHITESPACE+CAPT_NUMBER +OPT_WHITESPACE\
    +"\)"+OPT_WHITESPACE+"$"


class Val1Wrapper(object):
    """ just allow functions to change parameters"""
    def __init__(self, val=None):
        self._val = val

    @property
    def val(self):
        return self._val

    @val.setter
    def val(self, val):
        self._val = val



class Val2Wrapper(object):
    """ just allow functions to change 2 parameter values"""
    def __init__(self, val1=None, val2=None):
        self._val1 = val1
        self._val2 = val2

    @property
    def val1(self):
        return self._val1

    @val1.setter
    def val1(self, val):
        self._val1 = val

    @property
    def val2(self):
        return self._val2

    @val2.setter
    def val2(self, val):
        self._val2 = val


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


def dbtype_with_1size(root_word, str_to_check, valwrapper):
    """ checks if it matches xxx(N) and retusn
    (True/False, N)
    """
    v1 = Val1Wrapper(0)
    ptrn = root_word+"\([\s]*([0-9]*)[\s]*\)"
    captured_groups = re.findall(ptrn,str_to_check)
    if captured_groups is not None and len(captured_groups) == 1:
        valwrapper.val = int(captured_groups[0])
        return True
    else:
        return False


def dbtype_with_2size(root_word, str_to_check, val2_wrapper):
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
        val2_wrapper.val1 = int(matched_vals [0])
        val2_wrapper.val2= int(matched_vals[1])
        return True
    else:
        return False
