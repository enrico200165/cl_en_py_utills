
import sys
import re
import inspect
import traceback
import global_defs as g

import utils_regex_tiny as rtu

log = g.init_logging()


numeric_types_0par_keywords = ["bigint", "byteint"]
numeric_types_1par_keywords = ["numeric"]
numeric_types_2par_keywords = ["numeric"]

char_types_0par_keywords = []
char_types_1par_keywords = ["character", "varchar"]
char_types_2par_keywords = []

time_types_0par_keywords = ["timestamp"]
time_types_1par_keywords = []
time_types_2par_keywords = []



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
        s = "Column info for line:\n"
        s += "Line: "+"  ".join(self._line.split()) + "\n"
        s += "name=" +self._name
        s += " type="+self._type
        s += " size(s)=(" + str(self._val1) + ", " + str(self._val2) +")"
        s += " default="+str(self._default)
        s += " nullable="+str(self._nullable)
        s += " key_type="+str(self._key_type)

        return s


def find_table_name(tokens):
    """True if it COULD be, may also not be """
    for token in tokens:
        if "_" in token:
            return token

    return False


def parse_column_decl(line, col_info):
    """ parse column line in DDL and nothing more
    semantics check will be done in other function using
    as input the info parsed here
    return a tuple with (OK, ColumnInfo Object)
    """
    # col_info = ColumnInfo()

    # remove ending , if any
    line = line[:-1].strip() if line[-1:] == "," else line.strip()
    col_info._line = line

    tokens = line.split()
    if len(tokens) < 2:
        log.error("less than 3 tokens found in line: \n"+line)
        return False

    (nullable, ret, cur_idx) = (True, True, 0)

    col_info._name = tokens[cur_idx ]

    # solo per debug casereccio
    if col_info._name == "PK_P4C_PARTNER":
        log.warning("")

    # --- type NB here only data estraction, no validation --
    cur_idx = cur_idx+1
    val2 = rtu.Val2Wrapper()
    temp_type = ""

    if tokens[cur_idx].lower() == "national":
        if tokens[cur_idx+1].lower() != "character":
            log.error("national not followed by character")
            sys.exit(1)
        cur_idx = cur_idx+1
        temp_type = "national_"

    # national character varying(N)
    if tokens[cur_idx] == "character":
        cur_idx = cur_idx+1
        temp_type += "_character"
        if rtu.matches_dbtypes_with_1size(["varying"], tokens[cur_idx].lower(), val2):
            col_info._val1 = val2.val1
            temp_type += "_varying"
            col_info._type = temp_type

    # =============== NUMERIC ===================
    # numeric without esplicit size
    elif tokens[cur_idx].lower() in numeric_types_0par_keywords:
        temp_type += tokens[cur_idx]
        log.info("identified type: "+tokens[cur_idx])
    # numeric types with 1 size parameter (ANY ?)
    elif rtu.matches_dbtypes_with_1size(numeric_types_1par_keywords,
                tokens[cur_idx].lower(), val2):
        col_info._val1 = val2.val
        temp_type += val2.strval
    # numeric types with 2 size parameter (ANY ?)
    elif rtu.matches_dbtypes_with_2size(numeric_types_2par_keywords,
                                         tokens[cur_idx].lower(), val2):
        (col_info._val1, col_info._val2)  = (val2.val1, val2.val2)
        temp_type += val2.strval

# =============== CHARACTER ===================
    # numeric without esplicit size
    elif tokens[cur_idx].lower() in char_types_0par_keywords:
        temp_type += tokens[cur_idx]
        log.info("identified type: "+tokens[cur_idx])
        temp_type = tokens[cur_idx]
    # numeric types with 1 size parameter (ANY ?)
    elif rtu.matches_dbtypes_with_1size(char_types_1par_keywords,
                                        tokens[cur_idx].lower(), val2):
        col_info._val1 = val2.val1
        temp_type += val2.strval
    # numeric types with 2 size parameter (ANY ?)
    elif rtu.matches_dbtypes_with_2size(char_types_2par_keywords,
                                        tokens[cur_idx].lower(), val2):
        (col_info._val1, col_info._val2)  = (val2.val1, val2.val2)
        temp_type += val2.strval

    # =============== TIME ===================
    # time without esplicit size
    elif tokens[cur_idx].lower() in time_types_0par_keywords:
        temp_type += tokens[cur_idx]
        log.info("identified type: "+tokens[cur_idx])

    else:
        log.error("unmanaged type: " + tokens[cur_idx] + " in " +line)
        return False

    col_info._type = temp_type

    # --- NOT NULL ------------------------------
    if cur_idx >= len(tokens)-1:
        return True
    else:
        cur_idx = cur_idx+1
    if tokens[cur_idx].lower() == "not":
        nullable = False
        if tokens[cur_idx+1].lower() != "null":
            log.error('"not" not followed by null in: '+line)
            return False
        if cur_idx >= len(tokens)-1:
            return True
        else:
            cur_idx = cur_idx+1

    if tokens[cur_idx].lower() == "null":
        pass

    col_info._nullable = nullable

    # --- default -------------------------------
    if cur_idx >= len(tokens)-1:
        return True
    else:
        cur_idx = cur_idx+1

    if tokens[cur_idx].lower() == "default":
        log.debug("default value check not implementato")

    return True


def check_sql_create_table(stmt_lines_list, table_patterns_checker):
    """ check if CREATE TABLE is correct """

    nr_errors_found = 0 # we try to count and go on

    (cur_line_nr, nr_lines) = (0, len(stmt_lines_list))

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
        if re.match("[\w]*\)[\w]*$", line): # line with just ")"
            break
        try:
            col_info = ColumnInfo()
            if not parse_column_decl(line, col_info):
                log.error("error parsing column decl namme, line:\n"+line)
                continue

            check_column_name(line)

        except Exception as e:
            log.error("exiting: Exception maybe thrown from line : " +
            str(traceback.format_exc())+" "+str(e)+"\nin line:\n"+line)
            sys.exit(1)
        if ok:
            log.debug(col_info.dumpToStr())
        else:
            log.error("failed to parse line:\n" + line)

    return nr_errors_found > 0


def check_column_name(col_name):
    """
    PK_<label di chiave primaria>
    IDN_<label IDN>_SK
    IDN_<label IDN>
    IDC_<label IDC>
    :param col_name:
    :return:
    """




    pass
