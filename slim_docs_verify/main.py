
import read_clipboard as clbd
import parser_statements
import test_sql__statements_01

import global_defs as g
import e2bipatterns_checks as lp


def main():

    #text = clbd.read_clipboard()
    #print("from clpbd read: "+text)


    p = None
    # legal_patterns_list = lp.generate_pattern_wrappers()
    # p = "T_STG_{<sistema sorgente>/<sistema BI>}_{DT/LV/LH/LM/SC/DL}_<nome tabella o vista senza prefissi>_[KEY/RT/DD/WW/MM]"
    # p = "T_MTD_<raggruppamento>_{DT/LV/LH/LM/SC/DL}_<nome tabella A>2<nome tabella B>"
    # p = "T_BSC_<sistema sorgente>2<nome tabella sorgente>"
    # p = "FK_<nome tabella padre senza prefisso T>[_ <label>]"
    #p = "FK_<nome tabella padre senza prefisso T_>[_ <label>]"
    p = "T_STG_{<sistema sorgente>/<sistema BI>}_{DT/LV/LH/LM/SC/DL}_<nome tabella o vista senza prefissi>_[KEY/RT/DD/WW/MM]"

    legal_patterns_list = lp.generate_pattern_wrappers(p)
    print("generated object that check an edbi pattern against a string")
    for e2bipattern in legal_patterns_list:
        print(e2bipattern.dumpToStr())


    parser_statements.detect_build_dispatch_sqlstmt(test_sql__statements_01.sql_test_ddl_01)


main()