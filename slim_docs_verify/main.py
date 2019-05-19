

import logging
import read_clipboard as clbd
import sql_statements_check
import test_sql__statements_01 as t01

import global_defs as g
import e2bi_patterns as e2p
import e2bipatterns_checks as pc
import table_names_checker as tnc



def init():
    """will be filled as code develops"""
    global log
    log = g.init_logging()



def main():


    init()


    #text = clbd.read_clipboard()
    #log.info("from clpbd read: "+text)


    p = None
    # p = "T_STG_{<sistema sorgente>/<sistema BI>}_{DT/LV/LH/LM/SC/DL}_<nome tabella o vista senza prefissi>_[KEY/RT/DD/WW/MM]"
    # p = "T_MTD_<raggruppamento>_{DT/LV/LH/LM/SC/DL}_<nome tabella A>2<nome tabella B>"
    # p = "T_BSC_<sistema sorgente>2<nome tabella sorgente>"
    # p = "FK_<nome tabella padre senza prefisso T>[_ <label>]"
    #p = "FK_<nome tabella padre senza prefisso T_>[_ <label>]"
    #p = "T_STG_{<sistema sorgente>/<sistema BI>}_{DT/LV/LH/LM/SC/DL}_<nome tabella o vista senza prefissi>_[KEY/RT/DD/WW/MM]"
    #p = "FK_<sistema sorgente>_TT_KK"


    # sql = "create table FK_GDO_TT_KK"
    sql = t01.sql_test_ddl_01

    # table names checker
    tc = tnc.TableNamesChecker(e2p.patterns_list)


main()