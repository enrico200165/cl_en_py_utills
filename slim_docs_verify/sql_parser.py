

import re
import sqlparse
import test_sql_01

# Sample code sqlparse: https://www.programcreek.com/python/example/66949/sqlparse.parse


# print(sqlparse.format('select * from foo', reindent=True))
# parsed = sqlparse.parse('select * from foo')[0]
#print(parsed.tokens)


def removeComments(string):
    # remove all occurrences streamed comments (/*COMMENT */) from string
    string = re.sub(re.compile("/\*.*?\*/",re.DOTALL ) ,"" ,string)
    # remove all occurrence single-line comments (# COMMENT\n ) from string
    string = re.sub(re.compile("#.*" ) ,"" ,string)
    string = re.sub(re.compile(" *\\\echo.*" ) ,"" ,string)

    return string


def parse_sql_tables(sql):

    # remove comments
    # remove all occurance streamed comments (/*COMMENT */) from string
    sql = re.sub(re.compile("/\*.*?\*/",re.DOTALL ) ,"" ,sql)
    sql = removeComments(sql)

    tables = []
    stmt_idx = 0
    statements = sqlparse.parse(sql)
    for stmt in statements:
        print("-" * 60)
        stmt_idx = stmt_idx +1
        tkn_idx = 0
        for token in stmt.tokens:
            tkn_idx = tkn_idx + 1
            coord = "[{}][{}]".format(stmt_idx,tkn_idx)

            # skip separators
            if re.match("[\s]+", token.value, flags=0):
                # print('keyword {} {} "{}"'.format(coord,"blank",token.value))
                continue

            # parser only catches some keywors
            if token.is_keyword:
                print('keyword {} {} "{}"'.format(coord,"keyword",token.value))
                continue
            else:
                print('keyword {} {} "{}"'.format(coord,"id",token.value))
                pass
    return tables


parse_sql_tables(test_sql_01.sql_test_ddl_01)
#parse_sql_tables(test_sql_01.sql_test_comments_01)

#parse_sql_tables("aaa/**/aaaabbb/*xxxxxxx*/bbbbbbbbbbcccc/*xxxxxxx*/ccccccccd#ddddd")