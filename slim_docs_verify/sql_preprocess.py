
import re
import os

def clean_sql_text(sql):
    """ removes empty lines, comments, echo statements"""
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


