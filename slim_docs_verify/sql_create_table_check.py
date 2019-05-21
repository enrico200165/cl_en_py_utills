
import sys
import re

import global_defs as g

import regex_tiny_utils as rtu

log = g.init_logging()


class ColumnInfo(object):
    def __init__(self):
        self._line = None
        self._name = None
        self._val1 = None
        self._val2 = None
        self._default = None
        self._nullable = None
        self._key_type = None # 0 not known , 1 = PK, 2 FK
        self._type = None

    def dumpToStr(self):
        s = ""
        s += "name = " +self._name
        s += " type = "+self._type
        s += " size = (" + str(self._val1) + ", " + str(self._val2)
        return s


def find_table_name(tokens):
    """True if it COULD be, may also not be """
    for token in tokens:
        if "_" in token:
            return token

    return False




def parse_column_decl(line):
    """ parse column line in DDL and nothing more
    semantics check will be done in other function using
    as input the info parsed here
    return a tuple with (OK, ColumnInfo Object)
    """
    col_info = ColumnInfo()

    line = line[:-1].strip() if line[-1:] == "," else line.strip()
    col_info._line = line

    tokens = line.split()
    if len(tokens) < 2:
        log.error("less than 3 tokens found in line: \n"+line)
        sys.exit()

    (nullable, ret, cur_idx) = (True, True, 0)

    col_info._name = tokens[cur_idx ]

    # solo per debug casereccio
    if col_info._name == "PK_P4C_PARTNER":
        log.warning("")

    # --- type ----------------------------------
    cur_idx = cur_idx+1

    val1 = rtu.Val1Wrapper()
    val2 = rtu.Val2Wrapper()

    temp_type = ""
    token_type = tokens[cur_idx]

    if tokens[cur_idx].lower() == "national":
        if tokens[cur_idx+1].lower() != "character":
            log.error("national not followed by character")
            sys.exit(1)
        cur_idx = cur_idx+1
        temp_type = "national_"

    # national character varying(N)
    if tokens[cur_idx] == "character":
        temp_type += "character"
        cur_idx = cur_idx+1
        captured_groups = re.findall("varying\(([0-9]+)\)",tokens[cur_idx])
        if captured_groups is not None:
            assert(len(captured_groups) == 1)
            col_info._size = int(captured_groups[0])
            temp_type += "_varying"
    elif tokens[cur_idx].lower() in ["bigint", "byteint","timestamp"]:
        temp_type += tokens[cur_idx]
        log.info("identified type: "+tokens[cur_idx])
    elif rtu.dbtype_with_2size("numeric", tokens[cur_idx].lower(), val2):
        (col_info._val1, col_info._val2)  = (val2.val1, val2.val2)
        temp_type += "numeric"
    else:
        log.error("unmanaged type: " + tokens[cur_idx] + " in " +line)
        return (False, None)

    col_info._type = temp_type

    # --- NOT NULL ------------------------------
    if cur_idx >= len(tokens)-1:
        return (True, col_info)
    else:
        cur_idx = cur_idx+1
    if tokens[cur_idx].lower() == "not":
        nullable = False
        if tokens[cur_idx+1].lower() != "null":
            log.error('"not" not followed by null in: '+line)
            return (False, None)
        if cur_idx >= len(tokens)-1:
            return (True, col_info)
        else:
            cur_idx = cur_idx+1

    if tokens[cur_idx].lower() == "null":
        pass

    col_info._nullable = nullable

    # --- default -------------------------------
    if cur_idx >= len(tokens)-1:
        return (True, col_info)
    else:
        cur_idx = cur_idx+1

    if tokens[cur_idx].lower() == "default":
        log.warning("default not implementato")

    return (True, col_info)


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
    ok = True
    for line in stmt_lines_list[cur_line_nr+1:]:
        # fragile way to detect end of column names
        # works only if code is formatted as requested
        if re.match("[\w]*\)[\w]*$", line):
            break
        try:
            (ok, type_info) = parse_column_decl(line)
        except Exception as e:
            log.error("exiting: Exception: "+str(e)+"\nin line:\n"+line)
            sys.exit(1)
        if ok:
            log.debug(type_info.dumpToStr())
        else:
            log.error("failed to parse line:\n" + line)

    return nr_errors_found > 0

