from enum import Enum



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
    MTD	= "MTD"
    BSC	= "BSC"
    STG = "STG"
    BDS	= "BDS"
    ODS = "ODS";
    BDB = "BDB"
    BDA	= "BDA"
    DMT = "DMT"
    TDL = "TDL"





print(DataLayerNames.STAGING_AREA.value)

