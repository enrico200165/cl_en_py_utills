
import logging

from enum import Enum

def overrides(interface_class):
    def overrider(method):
        assert(method.__name__ in dir(interface_class))
        return method
    return overrider


class DataLayerNames(Enum):
    METADATI = "Metadati"
    BUSINESS_COPY = "Business Copy"
    STAGING_AREA = "Staging Area"
    OPERATIONAL_DATA_STORE = "Operational Data Store"
    DATAMART = "Datamart"
    TECHNICAL_DATA_LAYER = "Technical Data Layer"


# Schema non sembra  guidare nulla,
# questa modellazione probabilmente superflua
class DataLayerSchemi(Enum):
    # UNKNOWN = "layer unknown"
    MTD	= "MTD"
    BSC	= "BSC"
    STG = "STG"
    BDS	= "BDS"
    ODS = "ODS";
    BDB = "BDB"
    BDA	= "BDA"
    DMT = "DMT"
    TDL = "TDL"


class DBObjectsTypes(Enum):
    # UNKNOWN = "layer unknown"
    T = "tabella"
    P	= "tabella partizionata"
    Z = "tabella custom"
    V	= "vista"
    MV = "vista materializzata";
    SEQ = "sequence"
    BDA	= "BDA"
    DMT = "DMT"
    TDL = "TDL"


class SQLStmtType(Enum):
    UNKNOWN = "statement unknown"
    CREATE_TABLE = "Create Table"
    DROP_TABLE = "drop table"
    ALTER_TABLE = "alter table"
    UPDATE = "update table"
    INSERT = "insert"
    DISTRIBUTE = "distribute"


class IDType(Enum):
    TABLE_NAME = "Table Name"
    COL_NAME = "Column Name"
    COL_TYPE = "Column Type"





# RE_CAPTURE_GROUP_SIMPLE = "(.*?)" NON FUNZIONA
RE_CAPTURE_GROUP_SIMPLE = "([^_]*?)"
RE_VARIABLE_SIMPLE = "<.*?>"

legal_patterns_list = None


log = None # global logger object


def init_logging():
    # create logger

    logger = logging.getLogger('main')
    logger.setLevel(logging.DEBUG)

    # create console handler and set level to debug
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)

    # create formatter
    formatter = logging.Formatter('%(asctime)s %(filename)s - %(name)s - %(levelname)s - %(message)s')

    # add formatter to ch
    ch.setFormatter(formatter)

    # add ch to logger
    logger.addHandler(ch)

    global log
    log = logger

    return logger
