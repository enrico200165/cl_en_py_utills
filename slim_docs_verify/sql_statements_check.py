
import sys

import global_defs as g
import tokens_checks as tc
import sql_preprocess as ih

log = g.init_logging()


def find_table_name(tokens):
    """True if it COULD be, may also not be """
    for token in tokens:
        if "_" in token:
            return token

    return False


def check_sql_create_stmt(stmt_lines_list, table_patterns_checker):
    """ check if CREATE TABLE is correct """

    nr_errors_found = 0 # we try to count and go on

    cur_line_nr = 0
    nr_lines = len(stmt_lines_list)

    first_stmt_line = stmt_lines_list[cur_line_nr]

    table_name = find_table_name(first_stmt_line.split())
    if not table_patterns_checker.check_table_name(table_name):
        log.warning("table name seems not correct: "+table_name)
        nr_errors_found = nr_errors_found + 1

    if not cur_line_nr+1 < nr_lines:
        log.warning("incomplete create statement")
        return False
    cur_line_nr = cur_line_nr+1
    if not stmt_lines_list[cur_line_nr].strip() == "(":
        log.warning("line after create table does not contain (:\n"+cur_line_nr[cur_line_nr])

    # now there should be the values
    for line in stmt_lines_list[cur_line_nr:]:
        log.debug(line)



    return nr_errors_found > 0


def process_stmt_lines(stmt_type, stmt_lines, table_patterns_checker):
    """ routes statement types to appropriate handler"""

    log.info("processing stmt: " +stmt_lines[0]+ "\n")

    ret = False
    if False: # just for uniform syntax
        pass
    elif stmt_type == g.SQLStmtType.CREATE_TABLE:
        ret = check_sql_create_stmt(stmt_lines, table_patterns_checker)
    elif stmt_type == g.SQLStmtType.ALTER_TABLE:
        log.info("Warn: statement not yet supported: "+stmt_lines[0])
        ret = False
    elif stmt_type == g.SQLStmtType.INSERT:
        log.info("Warn: statement not yet supported: "+stmt_lines[0])
        ret = False
    elif stmt_type == g.SQLStmtType.DISTRIBUTE:
        log.info("Warn: statement not yet supported: "+stmt_lines[0])
        ret = False
    elif stmt_type == g.SQLStmtType.UNKNOWN:
        log.info("Warn: statement not yet supported: "+stmt_lines[0])
        ret = False
    else:
        m = ": "+stmt_lines[0] if stmt_lines[0] is not None else ""
        log.error("Warn: unable to process unknown statmement type"+m)
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

