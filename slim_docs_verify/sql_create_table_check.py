
import sys
import re

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


def parse_column_decl(line):

    line = line[:-1].strip() if line[-1:] == "," else line.strip()

    tokens = line.split()

    if len(tokens) < 3:
        log.error("")
        sys.exit()

    cur_idx = 0
    col_name = tokens[cur_idx ]


    # --- type ---
    cur_idx = cur_idx+1

    token_type = tokens[cur_idx]

    if tokens[cur_idx].lower() == "national":
        if tokens[cur_idx+1].lower() != "character":
            log.error("national not followed by character")
            sys.exit(1)
        cur_idx = cur_idx+1

    # national character varying(N)
    if tokens[cur_idx] == "character":
        cur_idx = cur_idx+1
        captured_groups = re.findall("varying\(([0-9]+)\)",tokens[cur_idx])
        if captured_groups is not None:
            assert(len(captured_groups) == 1)
            type_size = int(captured_groups[0])
    elif tokens[cur_idx].lower() in ["bigint" , "byteint","timestamp"]:
        log.info("identified type: "+tokens[cur_idx])
    else:
        log.error("unmanaged type: " + tokens[cur_idx] + " in " +line)


    # --- NOT NULL
    cur_idx = cur_idx+1
    nullable = True
    if tokens[cur_idx].lower() == "not":
        nullable = True
        if tokens[cur_idx+1].lower() != "null":
            log.error('"not" not followed by null in: '+line)
            sys.exit(1)
        cur_idx = cur_idx+1

    if tokens[cur_idx].lower() == "null":
        pass
    log.warning(line)
    log.warning(line)


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
    for line in stmt_lines_list[cur_line_nr+1:]:
        # fragile way to detect end of column names
        # works only if code is formatted as requested
        if re.match("[\w]*\)[\w]*$", line):
            break
        parse_column_decl(line)
        log.warning(line)

    return nr_errors_found > 0

