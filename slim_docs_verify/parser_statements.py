
import os
import re
import sqlparse
import test_sql__statements_01

import global_defs as g
import tokens_checks as tc
import sql_preprocess as ih


def process_sql_create_stmt(stmt_lines_list):
    """ check if CREATE TABLE is correct """

    first_stmt_line = stmt_lines_list[0]
    tokens = first_stmt_line.split()
    assert "create" in tokens or "CREATE" in tokens

    # look for table name token by checking one by one if contain _
    table_name = None
    for t in tokens:
        if "_" in t:
            table_name = t
            break
    # check if table name is matched by one of the patterns
    return tc.check_table_name(t)




def process_stmt_lines(stmt_type, stmt_lines):
    """ routes statement types to appropriate handler"""

    print("processing stmt: " +stmt_lines[0]+ "\n")

    ret = False
    if stmt_type == g.SQLStmtType.CREATE_TABLE:
        ret = process_sql_create_stmt(stmt_lines)
    elif stmt_type == g.SQLStmtType.UNKNOWN:
        pass # shoul only happen the first time
    else:
        pass



def parse_sql(sql):
    """ TODO probably redundant with other """

    sql = ih.clean_sql_text(sql)

    cur_stmt_type = g.SQLStmtType.UNKNOWN
    sql_lines = sql.splitlines()

    curr_stmt_text_lines = []
    for l in sql_lines:

        # detect start of a statement and process previous
        if "create " in l or "CREATE " in l:
            if cur_stmt_type != g.SQLStmtType.UNKNOWN:
                process_stmt_lines(cur_stmt_type, curr_stmt_text_lines)
                curr_stmt_text_lines = []
            cur_stmt_type = g.SQLStmtType.CREATE_TABLE
        elif "alter " in l or "ALTER " in l:
            if cur_stmt_type != g.SQLStmtType.UNKNOWN:
                process_stmt_lines(cur_stmt_type, curr_stmt_text_lines)
                curr_stmt_text_lines = []
            cur_stmt_type = g.SQLStmtType.ALTER_TABLE
        elif "distribute " in l or "DISTRIBUTE " in l:
            if cur_stmt_type != g.SQLStmtType.UNKNOWN:
                process_stmt_lines(cur_stmt_type, curr_stmt_text_lines)
                curr_stmt_text_lines = []
            cur_stmt_type = g.SQLStmtType.ALTER_TABLE
        else:
            pass

        curr_stmt_text_lines.append(l)

    # process last statement
    process_stmt_lines(cur_stmt_type, curr_stmt_text_lines)

