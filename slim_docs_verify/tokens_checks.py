""" Mission: checking tokens, ie. single words like table name Etc
currently all (also columns names Etc"

"""

import sys
import re
import e2bi_patterns


import global_defs as g


def check_token_part(token, n_part,
                     father_enum  # enum Type/class
                     ):
    """ if part n_part is one of the values of the enum
    used for the simpler checks on tokens
    enums have as values the allowed strings, and IDs identical to the string
    maybe this is redundant and not necessary
    """

    try:
        parts = token.split("_")
        part = parts[n_part]
        val = father_enum(part) # index by string
        pass
    except Exception:
        print("error checking {}".format(token))
        print("element {} not in ".format(n_part+1) + ", ".join([e.name for e in father_enum]))
        return (False, None)

    return (True, val)


def check_table_name(table_name, table_patterns_checker):

    # check if it is matched by one of the patterns
    # TODO now patters are not only for tables, check if must be changed
    for e2bi_pattern in table_patterns_checker:
        print(e2bi_pattern.dumpToStr())
        if e2bi_pattern.check_stmt_token(table_name):
            print("table name: {} matched by {}".format(table_name,
                                                        e2bi_pattern.e2bi_pattern))
            return True

    # below here simple checks that should be unnecessary if regex matching works
    # check second (index 1) part of the token
    # (ok, val) = check_token_part(table_name, 1, g.DataLayerSchemi)
    # if not ok:
    #     return False
    # data_layer = val

    # now we know the data layer

    return False