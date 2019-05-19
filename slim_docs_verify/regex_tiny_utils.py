

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


