

import logging
import read_clipboard as clbd
import parser_statements
import test_sql__statements_01

import global_defs as g
import e2bipatterns_checks as pc




def init():
    """will be filled as code develops"""
    global log
    log = g.init_logging()



def main():


    init()


    #text = clbd.read_clipboard()
    #print("from clpbd read: "+text)


    p = None
    # legal_patterns_list = pc.generate_pattern_wrappers()
    # p = "T_STG_{<sistema sorgente>/<sistema BI>}_{DT/LV/LH/LM/SC/DL}_<nome tabella o vista senza prefissi>_[KEY/RT/DD/WW/MM]"
    # p = "T_MTD_<raggruppamento>_{DT/LV/LH/LM/SC/DL}_<nome tabella A>2<nome tabella B>"
    # p = "T_BSC_<sistema sorgente>2<nome tabella sorgente>"
    # p = "FK_<nome tabella padre senza prefisso T>[_ <label>]"
    #p = "FK_<nome tabella padre senza prefisso T_>[_ <label>]"
    #p = "T_STG_{<sistema sorgente>/<sistema BI>}_{DT/LV/LH/LM/SC/DL}_<nome tabella o vista senza prefissi>_[KEY/RT/DD/WW/MM]"
    p = "FK_<sistema sorgente>_TT_KK"


    sql = "create table FK_GDO_TT_KK"


    # generate pattern checker objects, currently column names
    legal_patterns_list = pc.generate_pattern_wrappers(p)
    log.debug("generated object that check an edbi pattern against a string")
    for e2bipattern in legal_patterns_list:
        print(e2bipattern.dumpToStr())

    parser_statements.detect_build_dispatch_sqlstmt(sql,
                                                    legal_patterns_list)


main()