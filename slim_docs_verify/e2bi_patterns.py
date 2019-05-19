

#masks_lines_lists = "MV_ODS_{<sistema sorgente>/<sistema BI>/COM}_{DT/LV/LH/LM/SC}_<label>"


#patterns_list  = "T_BSC_<sistema sorgente>_<nome tabella sorgente>"


patterns_list = '''
T_MTD_<raggruppamento>_{DT/LV/LH/LM/SC/DL}_<label>	
T_BSC_<sistema sorgente>_<nome tabella sorgente>
T_STG_{<sistema sorgente>/<sistema BI>}_{DT/LV/LH/LM/SC/DL}_<nome tabella o vista senza prefissi>_[KEY/RT/DD/WW/MM]	
T_ODS_{<sistema sorgente>/<sistema BI>/ALL}_{DT/LV/LH/LM/LN/TT/SC}_<label>
T_DMT_<sistema sorgente>/<sistema BI>_{DM/FT/FA/LM}_<label>	
T_TDL_{<sistema sorgente>/<sistema BI>/ALL}_{DT/LV/LH/LM/LN/TT/SC}_<label>
T_MTD_<raggruppamento>_{DT/LV/LH/LM/SC/DL}_<nome tabella A>2<nome tabella B>	
T_BSC_<sistema sorgente>2<nome tabella sorgente>
T_STG_{<sistema sorgente>/<sistema BI>}_{DT/LV/LH/LM/SC/DL}_<nome tabella A>2<nome tabella B>	
T_ODS_{<sistema sorgente>/<sistema BI>/ALL}_{DT/LV/LH/LM/LN/TT/SC}_<nome tabella A>2<nome tabella B>	
T_DMT_<sistema sorgente>/<sistema BI>_{DM/FT/FA/LM}_<nome tabella A>2<nome tabella B>	
P_<nome tabella senza prefisso T_>_<nome campo>_{<valore>|<range_valori>}					
Z_MTD_<raggruppamento>_{DT/LV/LH/LM/SC/DL}_<label> 					
V_MTD_<raggruppamento>_{DT/LV/LH/LM/SC}_<label>
V_BSC_<sistema sorgente>_<label>	
V_STG_{<sistema sorgente>/<sistema BI}_{DT/LV/LH/LM/SC}_<label>
V_ODS_{<sistema sorgente>/<sistema BI>/COM}_{DT/LV/LH/LM/SC}_<label>
V_DMT_<sistema sorgente>/<sistema BI>_{DM/FT/FA/LM}_<label>
V_TDL_{<sistema sorgente>/<sistema BI>/ALL}_{DT/LV/LH/LM/LN/TT/SC}_<label>
MV_MTD_<raggruppamento>_{DT/LV/LH/LM/SC}_<label>
MV_BSC_<sistema sorgente>_<label>
MV_STG_{<sistema sorgente>/<sistema BI}_{DT/LV/LH/LM/SC}_<label>
MV_ODS_{<sistema sorgente>/<sistema BI>/COM}_{DT/LV/LH/LM/SC}_<label>
MV_DMT_<sistema sorgente>/<sistema BI>_{DM/FT/FA/LM}_<label>
MV_TDL_{<sistema sorgente>/<sistema BI>/ALL}_{DT/LV/LH/LM/LN/TT/SC}_<label>
<acronimo tipo dato>_<label>
<acronimo tipo dato>_<label>			
PK_<nome tabella senza prefisso T_>					
FK_<nome tabella padre senza prefisso T_>[_ <label>]					
SEQ_MTD_<label>	
SEQ_BSC_<label>	
SEQ_STG_<label>	
SEQ_ODS_<label>
SEQ_DMT_<label>
SEQ_TDL_<label>
FUN_MTD_<label>
FUN_BSC_<label>	
SEQ_STG_<label>
FUN_ODS_<label>
FUN_DMT_<label>
FUN_TDL_<label>
PRC_MTD_<label>
PRC_BSC_<label>	
PRC_STG_<label>
PRC_ODS_<label>
PRC_DMT_<label>
PRC_TDL_<label>
PKG_MTD_<label>
PKG_BSC_<label>	
PKG_STG_<label>
PKG_ODS_<label>
PKG_DMT_<label>	
IDX_<nome tabella senza prefisso T_>_UQ_<nomi colonna/e>
IDX_<nome tabella senza prefisso T_>_<nomi colonna/e>
IDX_<nome tabella senza prefisso T_>_UQ
IDX_<nome tabella senza prefisso T_>					
DBL_MTD_<sistema sorgente>
DBL_MTD_<sistema BI>	
DBL_BSC_<sistema sorgente>[<_label>]
DBL_BSC_<sistema BI>[<_label>]	
DBL_STG_<sistema sorgente>[<_label>]
DBL_STG_<sistema BI>[<_label>]	
DBL_ODS_<sistema sorgente>[<_label>]
DBL_ODS_<sistema BI>[<_label>]	
DBL_DMT_<sistema sorgente>[<_label>]
DBL_DMT_<sistema BI>[<_label>]	
SYN_MTD_R_<nome oggetto con prefisso>
SYN_MTD_L_<nome oggetto con prefisso>	
SYN_BSC_R_<nome oggetto con prefisso>
SYN_BSC_L_<nome oggetto con prefisso>	
SYN_STG_R_<nome oggetto con prefisso>
SYN_STG_L_<nome oggetto con prefisso>	
SYN_ODS_R_<nome oggetto con prefisso>
SYN_ODS_L_<nome oggetto con prefisso>	
SYN_DMT_R_<nome oggetto con prefisso>
SYN_DMT_L_<nome oggetto con prefisso>
SYN_<db_name>_L_<nome oggetto con prefisso>
SYN_TDL_R_<nome oggetto con prefisso>
SYN_TDL_L_<nome oggetto con prefisso>
TS_MTD_D
TS_MTD_<label>_D
TS_MTD_I
TS_MTD_<label>_I	
TS_BSC_<sistema sorgente>_D
TS_BSC_<sistema sorgente>_<label>_D
TS_BSC_<sistema BI>_I
TS_BSC_<sistema BI>_<label>_I	
TS_STG_<sistema sorgente>_D
TS_STG_<sistema sorgente>_<label>_D
TS_STG_<sistema BI>_D
TS_STG_<sistema BI>_<label>_D

TS_STG_<sistema sorgente>_I
TS_STG_<sistema sorgente>_<label>_I

TS_STG_<sistema BI>_I
TS_STG_<sistema BI>_<label>_I	
TS_ODS_<sistema BI>_D
TS_ODS_<sistema BI>_<label>_D

TS_ODS_<sistema sorgente>_D
TS_ODS_<sistema sorgente>_<label>_D

TS_ODS_<sistema BI>_I
TS_ODS_<sistema BI>_<label>_I

TS_ODS_<sistema sorgente>_I
TS_ODS_<sistema sorgente>_<label>_I

TS_ODS_COM_I
TS_ODS_COM_<label>_I	
TS_DMT_<sistema sorgente>/<sistema BI>_D
TS_DMT_<sistema sorgente>/<sistema BI>_<label>_D

TS_DMT_<sistema sorgente>/<sistema BI>_I
TS_DMT_<sistema sorgente>/<sistema BI>_<label>_I
'''
