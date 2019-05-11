
import read_clipboard as clbd
import sql_parser
import test_sql_01


def main():

    #text = clbd.read_clipboard()
    #print("from clpbd read: "+text)


    # print("sql statement\\n"+ test_sql_01.sql_test_ddl_01)

    tables = sql_parser.parse_sql_tables(test_sql_01.sql_test_ddl_01)

    for t in tables:
        print(t)

main()