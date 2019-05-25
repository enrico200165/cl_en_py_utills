""" Mission: checking tokens, ie. single words like table name Etc
currently all (also columns names Etc"

"""

import sys
import re
import patterns_table_names
import global_defs as g

log = g.init_logging()

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
        log.error("error checking {}".format(token))
        log.error("element {} not in ".format(n_part+1) + ", ".join([e.name for e in father_enum]))
        return (False, None)

    return (True, val)

