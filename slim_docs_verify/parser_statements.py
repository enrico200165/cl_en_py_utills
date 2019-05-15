
import sys

import global_defs as g
import tokens_checks as tc
import sql_preprocess as ih


def check_sql_create_stmt(stmt_lines_list, table_patterns_checker):
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
    return tc.check_table_name(t, table_patterns_checker)


def process_stmt_lines(stmt_type, stmt_lines, table_patterns_checker):
    """ routes statement types to appropriate handler"""

    print("processing stmt: " +stmt_lines[0]+ "\n")

    ret = False
    if False: # just for uniform syntax
        pass
    elif stmt_type == g.SQLStmtType.CREATE_TABLE:
        ret = check_sql_create_stmt(stmt_lines, table_patterns_checker)
    elif stmt_type == g.SQLStmtType.ALTER_TABLE:
        print("Warn: statement not yet supported: "+stmt_lines[0])
        ret = False
    elif stmt_type == g.SQLStmtType.INSERT:
        print("Warn: statement not yet supported: "+stmt_lines[0])
        ret = False
    elif stmt_type == g.SQLStmtType.DISTRIBUTE:
        print("Warn: statement not yet supported: "+stmt_lines[0])
        ret = False
    elif stmt_type == g.SQLStmtType.UNKNOWN:
        print("Warn: statement not yet supported: "+stmt_lines[0])
        ret = False
    else:
        m = ": "+stmt_lines[0] if stmt_lines[0] is not None else ""
        print("Warn: unable to process unknown statmement type"+m)
        sys.exit(1)




def detect_build_dispatch_sqlstmt(sql, table_patterns_checker):
    """ TODO probably redundant with other """

    sql = ih.clean_sql_text(sql)

    cur_stmt_type = g.SQLStmtType.UNKNOWN
    sql_lines = sql.splitlines()

    curr_stmt_text_lines = []
    for l in sql_lines:

        # detect start of a statement and process previous
        if "create " in l or "CREATE " in l:
            if cur_stmt_type != g.SQLStmtType.UNKNOWN:
                process_stmt_lines(cur_stmt_type, curr_stmt_text_lines, table_patterns_checker)
                curr_stmt_text_lines = []
            cur_stmt_type = g.SQLStmtType.CREATE_TABLE

        elif "alter " in l or "ALTER " in l:
            if cur_stmt_type != g.SQLStmtType.UNKNOWN:
                process_stmt_lines(cur_stmt_type, curr_stmt_text_lines, table_patterns_checker)
                curr_stmt_text_lines = []
            cur_stmt_type = g.SQLStmtType.ALTER_TABLE

        elif "distribute " in l or "DISTRIBUTE " in l:
            if cur_stmt_type != g.SQLStmtType.UNKNOWN:
                process_stmt_lines(cur_stmt_type, curr_stmt_text_lines, table_patterns_checker)
                curr_stmt_text_lines = []
            cur_stmt_type = g.SQLStmtType.DISTRIBUTE

        else:
            """qui NON devo e non posso fare nulla, dato che solo la prima
            riga dello statement identifica il tipo statement, ma qui le scorriamo
            tutte per costruire il corpo dello statement
            
            al limite qui FORSE potrebbe andare la rilevazione di qualche situazione
            particolaree per patch programmative
            """
            pass


        curr_stmt_text_lines.append(l)

    # process last statement
    process_stmt_lines(cur_stmt_type, curr_stmt_text_lines, table_patterns_checker)

