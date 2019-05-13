
import read_clipboard as clbd
import sql_parser
import test_sql_01

import global_defs as g
import check_patterns as lp


def main():

    #text = clbd.read_clipboard()
    #print("from clpbd read: "+text)


    # legal_patterns_list = lp.generate_pattern_wrappers()
    p = "T_STG_{<sistema sorgente>/<sistema BI>}_{DT/LV/LH/LM/SC/DL}_<nome tabella o vista senza prefissi>_[KEY/RT/DD/WW/MM]"
    p = "T_MTD_<raggruppamento>_{DT/LV/LH/LM/SC/DL}_<nome tabella A>2<nome tabella B>"

    legal_patterns_list = lp.generate_pattern_wrappers(p)
    print("generated object that check an edbi pattern against a string")
    for e2bipattern in legal_patterns_list:
        print(e2bipattern.dumpToStr())


    #tables = sql_parser.parse_sql(test_sql_01.sql_test_ddl_01)


main()