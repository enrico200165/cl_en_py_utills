

def cap_grp(s, is_optional):
    tmp = "({})".format(s)
    if is_optional:
        tmp += "?"
    return tmp


def non_cap_grp(s, is_optional):
    tmp = "(?:{})".format(s)
    if is_optional:
        tmp += "?"
    return tmp


