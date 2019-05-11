
import read_clipboard as clbd
import sql_parser
import test_sql_01

import global_defs as g
import legal_patterns as lp



def main():

    #text = clbd.read_clipboard()
    #print("from clpbd read: "+text)


    # print("sql statement\\n"+ test_sql_01.sql_test_ddl_01)

    legal_patterns_list = lp.generate_regexes()



    tables = sql_parser.parse_sql(test_sql_01.sql_test_ddl_01)


main()