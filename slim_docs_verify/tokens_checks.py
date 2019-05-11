

import sys
import re
import masks


import global_defs as g




def check_token_part(t, n_part, father_enum):

    try:
        parts = t.split("_")
        part = parts[n_part]
        val = father_enum(part)
    except Exception:
        print("error checking {}".format(t))
        print("element {} not in ".format(n_part+1) + ", ".join([e.name for e in father_enum]))
        return (False, None)

    return (True, val)


def check_table_name(t):

    # T_MTD_<raggruppamento>                     _{DT/LV/LH/LM/SC/DL}   _<label>
    # T_BSC_<sistema sorgente>                   _<nome tabella sorgente>
    # T_STG_{<sistema sorgente>/<sistema BI>}    _{DT/LV/LH/LM/SC/DL}   _ <nome tabella o vista senza prefissi>_[KEY/RT/DD/WW/MM]
    # T_ODS_{<sistema sorgente>/<sistema BI>/ALL}_{DT/LV/LH/LM/LN/TT/SC}_<label>
    # T_DMT_<sistema sorgente>/<sistema BI>      _{DM/FT/FA/LM}         _<label>
    # T_TDL_{<sistema sorgente>/<sistema BI>/ALL}_{DT/LV/LH/LM/LN/TT/SC}_<label>"

    (ok, val) = check_token_part(t, 1, g.DataLayerSchemi)
    if not ok:
        return False
    data_layer = val



    return True