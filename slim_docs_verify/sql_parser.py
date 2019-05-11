
import os
import re
import sqlparse
import test_sql_01

import global_defs as g
import tokens_checks as tc


# Sample code sqlparse: https://www.programcreek.com/python/example/66949/sqlparse.parse


# print(sqlparse.format('select * from foo', reindent=True))
# parsed = sqlparse.parse('select * from foo')[0]
#print(parsed.tokens)




previous_tokens = [None, None, None]


def setPreviousToken(token):

    assert len(previous_tokens) > 0

    i = len(previous_tokens)-1;
    while 1 <= i:
        previous_tokens[i] = previous_tokens[i-1]
        i = i-1
    previous_tokens[i] = token
    pass


def clean_sql(sql):

    # remove comments
    # remove all occurance streamed comments (/*COMMENT */) from string
    sql= re.sub(re.compile("/\*.*?\*/",re.DOTALL ) ,"" ,sql)
    # remove all occurrence single-line comments (# COMMENT\n ) from string
    sql = re.sub(re.compile("#.*" ) ,"" ,sql)
    sql = re.sub(re.compile(" *\\\echo.*" ) ,"" ,sql)

    lines = sql.splitlines()
    non_empty_lines = []
    for l in lines:
        if len(l) == 0:
            continue
        if re.match("^\s*$",l):
            continue
        else:
            non_empty_lines.append(l)

    sql = os.linesep.join([s for s in non_empty_lines if s])

    return sql


def process_sql_create_stmt(stmt_lines):

    tokens = stmt_lines[0].split()
    assert "create" in tokens or "CREATE" in tokens

    table_name = None
    for t in tokens:
        if "_" in t:
            table_name = t
            break
    # print("tabella: {} in {}".format(table_name,tokens))
    tc.check_table_name(t)


def process_stmt_lines(stmt_type, stmt_lines):

    print("processing stmt"+ "\n".join(stmt_lines))
    if stmt_type == g.SQLStmtType.CREATE_TABLE:
        process_sql_create_stmt(stmt_lines)
    elif stmt_type == g.SQLStmtType.UNKNOWN:
        print("sconosciuto")
    else:
        pass



def parse_sql(sql):

    sql = clean_sql(sql)

    cur_stmt_type = g.SQLStmtType.UNKNOWN
    stmt_text_lines = []
    lines = sql.splitlines()
    for l in lines:

        if "create " in l or "CREATE " in l:
            process_stmt_lines(cur_stmt_type, stmt_text_lines)
            cur_stmt_type = g.SQLStmtType.CREATE_TABLE
            stmt_text_lines = []
        elif "alter " in l or "ALTER " in l:
            process_stmt_lines(cur_stmt_type, stmt_text_lines)
            cur_stmt_type = g.SQLStmtType.ALTER_TABLE
            stmt_text_lines = []
        else:
            pass

        stmt_text_lines.append(l)

    # process last statement
    process_stmt_lines(cur_stmt_type, stmt_text_lines)

parse_sql(test_sql_01.sql_test_ddl_01)