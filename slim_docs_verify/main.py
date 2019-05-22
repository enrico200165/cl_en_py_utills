

import logging
import read_clipboard as clbd
import sql_statements_check as sc

# real life statements for test
import test_sql_statements_01 as t01

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

    # sql = "create table FK_GDO_TT_KK"
    sql = t01.sql_test_ddl_01

    # table names checker
    tc = tnc.TableNamesChecker(e2p.patterns_list)

    sc.detect_build_dispatch_sqlstmt(t01.sql_test_ddl_01, tc)


main()