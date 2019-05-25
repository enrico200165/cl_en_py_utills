from unittest import TestCase

import global_defs as g

import check_table_names as tnc


log = g.init_logging()

class TestCheck_table_name(TestCase):


    def setUp(self):
        self._checker = tnc.PatternsListChecker()
        pass


    def check(self, name):
        return self._checker.check_against_patterns(name)


    def test_check_table_name(self):

        if not self.check("TS_MTD_D"):
            self.fail()

        if not self.check("TS_MTD_I"):
            self.fail()

        if not self.check("TS_ODS_COM_I"):
            self.fail()


        if not self.check("TS_MTD_enricolabel_D"):
            self.fail()


        if not self.check("TS_MTD_enricolabel_I"):
            self.fail()


        if not self.check("TS_BSC_P4C_I"):
            self.fail()


        if not self.check("TS_STG_AUD_D"):
            self.fail()

        if not self.check("TS_STG_AUD_I"):
            self.fail()

        if not self.check("TS_ODS_AUD_D"):
            self.fail()

        if not self.check("TS_ODS_AUD_I"):
            self.fail()

        if not self.check("DBL_MTD_AUD"):
            self.fail()


        if not self.check("TS_ODS_COM_enricolabel_I"):
            self.fail()
        if not self.check("TS_ODS_COM_enricolabel_I"):
            self.fail()
        if not self.check("TS_ODS_COM_enricolabel_I"):
            self.fail()
        if not self.check("TS_ODS_COM_enricolabel_I"):
            self.fail()


        if not self.check("DBL_MTD_AUD"):
            self.fail()

        if not self.check("TS_BSC_GEO_D"):
            self.fail()

        if not self.check("TS_STG_AUD_D"):
            self.fail()


        if not self.check("TS_STG_AUD_I"):
            self.fail()
        if not self.check("TS_STG_AUD_I"):
            self.fail()
        if not self.check("TS_STG_AUD_I"):
            self.fail()
        if not self.check("TS_STG_AUD_I"):
            self.fail()


        if not self.check("TS_ODS_AUD_D"):
            self.fail()
        if not self.check("TS_ODS_AUD_D"):
            self.fail()
        if not self.check("TS_ODS_AUD_D"):
            self.fail()
        if not self.check("TS_ODS_AUD_D"):
            self.fail()


        if not self.check("TS_ODS_AUD_I"):
            self.fail()
        if not self.check("TS_ODS_AUD_I"):
            self.fail()
        if not self.check("TS_ODS_AUD_I"):
            self.fail()
        if not self.check("TS_ODS_AUD_I"):
            self.fail()


        if not self.check("TS_STG_AUD_enricolabel_D"):
            self.fail()

        if not self.check("TS_ODS_AUD_enricolabel_D"):
            self.fail()

        if not self.check("TS_ODS_AUD_enricolabel_I"):
            self.fail()


        if not self.check("DBL_BSC_GEO_enricolabel"):
            self.fail()
        if not self.check("DBL_BSC_GEO"):
            self.fail()
        if not self.check("DBL_BSC_P4C_enricolabel"):
            self.fail()
        if not self.check("DBL_BSC_P4C"):
            self.fail()



        if not self.check("DBL_STG_AUD_enricolabel"):
            self.fail()
        if not self.check("DBL_STG_AUD"):
            self.fail()
        if not self.check("DBL_STG_P4C_enricolabel"):
            self.fail()
        if not self.check("DBL_STG_P4C"):
            self.fail()

        if not self.check("DBL_ODS_GEO_enricolabel"):
            self.fail()
        if not self.check("DBL_ODS_GEO"):
            self.fail()
        if not self.check("DBL_ODS_P4C_enricolabel"):
            self.fail()
        if not self.check("DBL_ODS_P4C"):
            self.fail()


        if not self.check("DBL_DMT_GEO_enricolabel"):
            self.fail()
        if not self.check("DBL_DMT_GEO"):
            self.fail()
        if not self.check("DBL_DMT_P4C_enricolabel"):
            self.fail()
        if not self.check("DBL_DMT_P4C"):
            self.fail()


        if not self.check("TS_BSC_AUD_enricolabel_I"):
            self.fail()
        if not self.check("TS_BSC_AUD_enricolabel_I"):
            self.fail()
        if not self.check("TS_BSC_AUD_enricolabel_I"):
            self.fail()
        if not self.check("TS_BSC_AUD_enricolabel_I"):
            self.fail()


        if not self.check("TS_STG_AUD_enricolabel_I"):
            self.fail()
        if not self.check("TS_STG_AUD_enricolabel_I"):
            self.fail()
        if not self.check("TS_STG_AUD_enricolabel_I"):
            self.fail()
        if not self.check("TS_STG_AUD_enricolabel_I"):
            self.fail()

        if not self.check("MV_BSC_GEO_enricolabel"):
            self.fail()
        if self.check("MV_BSC_P4C_enricolabel"): # non ammette sistema destinazione
            self.fail()


        if not self.check("V_BSC_GEO_enricolabel"):
            self.fail()


        #TS_BSC_<sistema sorgente>_D

        if not self.check("TS_BSC_GEO_D"):
            self.fail()
        if self.check("TS_BSC_P4C_D"):
            self.fail()

        #TS_BSC_<sistema sorgente>_<label>_D
        if not self.check("TS_BSC_GEO_enricolabel_D"):
            self.fail()
        if self.check("TS_BSC_P4C_enricolabel_D"):
            self.fail()


        # TS_STG_<sistema sorgente>_D
        if not self.check("TS_STG_GEO_D"):
            self.fail()
        if not self.check("TS_STG_P4C_D"):
            self.fail()
        # TS_STG_<sistema sorgente>_<label>_D
        if not self.check("TS_STG_GEO_enricolabel_D"):
            self.fail()
        if not self.check("TS_STG_P4C_enricolabel_D"):
            self.fail()
        # TS_STG_<sistema BI>_D
        if not self.check("TS_STG_P4C_D"):
            self.fail()


        # TS_STG_<sistema BI>_<label>_D
        if not self.check("TS_STG_P4C_enricolabel_D"):
            self.fail()
        if not self.check("TS_STG_P4C_D"):
            self.fail()

        # TS_ODS
        if not self.check("TS_ODS_GEO_enricolabel_D"):
            self.fail()
        if not self.check("TS_ODS_GEO_D"):
            self.fail()
        if not self.check("TS_ODS_AUD_enricolabel_I"):
            self.fail()
        if not self.check("TS_ODS_AUD_I"):
            self.fail()

        if not self.check("DBL_BSC_GEO_enricolabel"):
            self.fail()
        if not self.check("DBL_BSC_AUD_enricolabel"):
            self.fail()
        if not self.check("DBL_BSC_AUD_enricolabel"):
            self.fail()
        if not self.check("DBL_BSC_AUD_enricolabel"):
            self.fail()


        if not self.check("DBL_STG_AUD_enricolabel"):
            self.fail()
        if not self.check("DBL_STG_AUD_enricolabel"):
            self.fail()
        if not self.check("DBL_STG_AUD_enricolabel"):
            self.fail()
        if not self.check("DBL_STG_AUD_enricolabel"):
            self.fail()


        if not self.check("DBL_ODS_AUD_enricolabel"):
            self.fail()
        if not self.check("DBL_ODS_AUD_enricolabel"):
            self.fail()
        if not self.check("DBL_ODS_AUD_enricolabel"):
            self.fail()
        if not self.check("DBL_ODS_AUD_enricolabel"):
            self.fail()


        if not self.check("DBL_DMT_AUD_enricolabel"):
            self.fail()
        if not self.check("DBL_DMT_AUD_enricolabel"):
            self.fail()
        if not self.check("DBL_DMT_AUD_enricolabel"):
            self.fail()
        if not self.check("DBL_DMT_AUD_enricolabel"):
            self.fail()


        if not self.check("SEQ_MTD_enricolabel"):
            self.fail()
        if not self.check("SEQ_BSC_enricolabel"):
            self.fail()


        if not self.check("FUN_MTD_enricolabel"):
            self.fail()
        if not self.check("FUN_BSC_enricolabel"):
            self.fail()

        if not self.check("PRC_MTD_enricolabel"):
            self.fail()
        if not self.check("PRC_BSC_enricolabel"):
            self.fail()


        if not self.check("PKG_MTD_enricolabel"):
            self.fail()
        if not self.check("PKG_BSC_enricolabel"):
            self.fail()


        if not self.check("IDX_<nome tabella senza prefisso T_>_UQ"):
            self.fail()
        if not self.check("IDX_<nome tabella senza prefisso T_>_UQ"):
            self.fail()
        if not self.check("IDX_<nome tabella senza prefisso T_>_UQ"):
            self.fail()
        if not self.check("IDX_<nome tabella senza prefisso T_>_UQ"):
            self.fail()


        if not self.check("SYN_MTD_L_<nome oggetto con prefisso>"):
            self.fail()
        if not self.check("SYN_MTD_L_<nome oggetto con prefisso>"):
            self.fail()
        if not self.check("SYN_MTD_L_<nome oggetto con prefisso>"):
            self.fail()
        if not self.check("SYN_MTD_L_<nome oggetto con prefisso>"):
            self.fail()


        if not self.check("SYN_BSC_L_<nome oggetto con prefisso>"):
            self.fail()
        if not self.check("SYN_BSC_L_<nome oggetto con prefisso>"):
            self.fail()
        if not self.check("SYN_BSC_L_<nome oggetto con prefisso>"):
            self.fail()
        if not self.check("SYN_BSC_L_<nome oggetto con prefisso>"):
            self.fail()


        if not self.check("SYN_STG_L_<nome oggetto con prefisso>"):
            self.fail()
        if not self.check("SYN_STG_L_<nome oggetto con prefisso>"):
            self.fail()
        if not self.check("SYN_STG_L_<nome oggetto con prefisso>"):
            self.fail()
        if not self.check("SYN_STG_L_<nome oggetto con prefisso>"):
            self.fail()


        if not self.check("SYN_ODS_L_<nome oggetto con prefisso>"):
            self.fail()
        if not self.check("SYN_ODS_L_<nome oggetto con prefisso>"):
            self.fail()
        if not self.check("SYN_ODS_L_<nome oggetto con prefisso>"):
            self.fail()
        if not self.check("SYN_ODS_L_<nome oggetto con prefisso>"):
            self.fail()


        if not self.check("TS_DMT_AUD/AUD_D"):
            self.fail()
        if not self.check("TS_DMT_AUD/AUD_D"):
            self.fail()
        if not self.check("TS_DMT_AUD/AUD_D"):
            self.fail()
        if not self.check("TS_DMT_AUD/AUD_D"):
            self.fail()


        if not self.check("TS_DMT_AUD/AUD_I"):
            self.fail()
        if not self.check("TS_DMT_AUD/AUD_I"):
            self.fail()
        if not self.check("TS_DMT_AUD/AUD_I"):
            self.fail()
        if not self.check("TS_DMT_AUD/AUD_I"):
            self.fail()


        if not self.check("SYN_<db_name>_L_<nome oggetto con prefisso>"):
            self.fail()
        if not self.check("SYN_<db_name>_L_<nome oggetto con prefisso>"):
            self.fail()
        if not self.check("SYN_<db_name>_L_<nome oggetto con prefisso>"):
            self.fail()
        if not self.check("SYN_<db_name>_L_<nome oggetto con prefisso>"):
            self.fail()


        if not self.check("V_MTD_<raggruppamento>_{DT/LV/LH/LM/SC}_enricolabel"):
            self.fail()
        if not self.check("V_MTD_<raggruppamento>_{DT/LV/LH/LM/SC}_enricolabel"):
            self.fail()
        if not self.check("V_MTD_<raggruppamento>_{DT/LV/LH/LM/SC}_enricolabel"):
            self.fail()
        if not self.check("V_MTD_<raggruppamento>_{DT/LV/LH/LM/SC}_enricolabel"):
            self.fail()


        if not self.check("T_BSC_AUD_<nome tabella sorgente>"):
            self.fail()
        if not self.check("T_BSC_AUD_<nome tabella sorgente>"):
            self.fail()
        if not self.check("T_BSC_AUD_<nome tabella sorgente>"):
            self.fail()
        if not self.check("T_BSC_AUD_<nome tabella sorgente>"):
            self.fail()


        if not self.check("T_BSC_AUD2<nome tabella sorgente>"):
            self.fail()
        if not self.check("T_BSC_AUD2<nome tabella sorgente>"):
            self.fail()
        if not self.check("T_BSC_AUD2<nome tabella sorgente>"):
            self.fail()
        if not self.check("T_BSC_AUD2<nome tabella sorgente>"):
            self.fail()


        if not self.check("MV_MTD_<raggruppamento>_{DT/LV/LH/LM/SC}_enricolabel"):
            self.fail()
        if not self.check("MV_MTD_<raggruppamento>_{DT/LV/LH/LM/SC}_enricolabel"):
            self.fail()
        if not self.check("MV_MTD_<raggruppamento>_{DT/LV/LH/LM/SC}_enricolabel"):
            self.fail()
        if not self.check("MV_MTD_<raggruppamento>_{DT/LV/LH/LM/SC}_enricolabel"):
            self.fail()


        if not self.check("TS_DMT_AUD/AUD_enricolabel_D"):
            self.fail()
        if not self.check("TS_DMT_AUD/AUD_enricolabel_D"):
            self.fail()
        if not self.check("TS_DMT_AUD/AUD_enricolabel_D"):
            self.fail()
        if not self.check("TS_DMT_AUD/AUD_enricolabel_D"):
            self.fail()


        if not self.check("TS_DMT_AUD/AUD_enricolabel_I"):
            self.fail()
        if not self.check("TS_DMT_AUD/AUD_enricolabel_I"):
            self.fail()
        if not self.check("TS_DMT_AUD/AUD_enricolabel_I"):
            self.fail()
        if not self.check("TS_DMT_AUD/AUD_enricolabel_I"):
            self.fail()


        if not self.check("PK_<nome tabella senza prefisso T_>"):
            self.fail()
        if not self.check("PK_<nome tabella senza prefisso T_>"):
            self.fail()
        if not self.check("PK_<nome tabella senza prefisso T_>"):
            self.fail()
        if not self.check("PK_<nome tabella senza prefisso T_>"):
            self.fail()


        if not self.check("IDX_<nome tabella senza prefisso T_>"):
            self.fail()
        if not self.check("IDX_<nome tabella senza prefisso T_>"):
            self.fail()
        if not self.check("IDX_<nome tabella senza prefisso T_>"):
            self.fail()
        if not self.check("IDX_<nome tabella senza prefisso T_>"):
            self.fail()


        if not self.check("T_MTD_<raggruppamento>_{DT/LV/LH/LM/SC/DL}_enricolabel"):
            self.fail()
        if not self.check("T_MTD_<raggruppamento>_{DT/LV/LH/LM/SC/DL}_enricolabel"):
            self.fail()
        if not self.check("T_MTD_<raggruppamento>_{DT/LV/LH/LM/SC/DL}_enricolabel"):
            self.fail()
        if not self.check("T_MTD_<raggruppamento>_{DT/LV/LH/LM/SC/DL}_enricolabel"):
            self.fail()


        if not self.check("IDX_<nome tabella senza prefisso T_>_<nomi colonna/e>"):
            self.fail()
        if not self.check("IDX_<nome tabella senza prefisso T_>_<nomi colonna/e>"):
            self.fail()
        if not self.check("IDX_<nome tabella senza prefisso T_>_<nomi colonna/e>"):
            self.fail()
        if not self.check("IDX_<nome tabella senza prefisso T_>_<nomi colonna/e>"):
            self.fail()


        if not self.check("IDX_<nome tabella senza prefisso T_>_UQ_<nomi colonna/e>"):
            self.fail()
        if not self.check("IDX_<nome tabella senza prefisso T_>_UQ_<nomi colonna/e>"):
            self.fail()
        if not self.check("IDX_<nome tabella senza prefisso T_>_UQ_<nomi colonna/e>"):
            self.fail()
        if not self.check("IDX_<nome tabella senza prefisso T_>_UQ_<nomi colonna/e>"):
            self.fail()


        if not self.check("PKG_STG_enricolabel    PKG_ODS_enricolabel    PKG_DMT_enricolabel"):
            self.fail()
        if not self.check("PKG_STG_enricolabel    PKG_ODS_enricolabel    PKG_DMT_enricolabel"):
            self.fail()
        if not self.check("PKG_STG_enricolabel    PKG_ODS_enricolabel    PKG_DMT_enricolabel"):
            self.fail()
        if not self.check("PKG_STG_enricolabel    PKG_ODS_enricolabel    PKG_DMT_enricolabel"):
            self.fail()


        if not self.check("V_DMT_AUD/AUD_{DM/FT/FA/LM}_enricolabel"):
            self.fail()
        if not self.check("V_DMT_AUD/AUD_{DM/FT/FA/LM}_enricolabel"):
            self.fail()
        if not self.check("V_DMT_AUD/AUD_{DM/FT/FA/LM}_enricolabel"):
            self.fail()
        if not self.check("V_DMT_AUD/AUD_{DM/FT/FA/LM}_enricolabel"):
            self.fail()


        if not self.check("MV_DMT_AUD/AUD_{DM/FT/FA/LM}_enricolabel"):
            self.fail()
        if not self.check("MV_DMT_AUD/AUD_{DM/FT/FA/LM}_enricolabel"):
            self.fail()
        if not self.check("MV_DMT_AUD/AUD_{DM/FT/FA/LM}_enricolabel"):
            self.fail()
        if not self.check("MV_DMT_AUD/AUD_{DM/FT/FA/LM}_enricolabel"):
            self.fail()


        if not self.check("T_DMT_AUD/AUD_{DM/FT/FA/LM}_enricolabel"):
            self.fail()
        if not self.check("T_DMT_AUD/AUD_{DM/FT/FA/LM}_enricolabel"):
            self.fail()
        if not self.check("T_DMT_AUD/AUD_{DM/FT/FA/LM}_enricolabel"):
            self.fail()
        if not self.check("T_DMT_AUD/AUD_{DM/FT/FA/LM}_enricolabel"):
            self.fail()


        if not self.check("V_STG_{AUD/<SBI}_{DT/LV/LH/LM/SC}_enricolabel"):
            self.fail()
        if not self.check("V_STG_{AUD/<SBI}_{DT/LV/LH/LM/SC}_enricolabel"):
            self.fail()
        if not self.check("V_STG_{AUD/<SBI}_{DT/LV/LH/LM/SC}_enricolabel"):
            self.fail()
        if not self.check("V_STG_{AUD/<SBI}_{DT/LV/LH/LM/SC}_enricolabel"):
            self.fail()


        if not self.check("MV_STG_{AUD/<SBI}_{DT/LV/LH/LM/SC}_enricolabel"):
            self.fail()
        if not self.check("MV_STG_{AUD/<SBI}_{DT/LV/LH/LM/SC}_enricolabel"):
            self.fail()
        if not self.check("MV_STG_{AUD/<SBI}_{DT/LV/LH/LM/SC}_enricolabel"):
            self.fail()
        if not self.check("MV_STG_{AUD/<SBI}_{DT/LV/LH/LM/SC}_enricolabel"):
            self.fail()


        if not self.check("Z_MTD_<raggruppamento>_{DT/LV/LH/LM/SC/DL}_enricolabel"):
            self.fail()
        if not self.check("Z_MTD_<raggruppamento>_{DT/LV/LH/LM/SC/DL}_enricolabel"):
            self.fail()
        if not self.check("Z_MTD_<raggruppamento>_{DT/LV/LH/LM/SC/DL}_enricolabel"):
            self.fail()
        if not self.check("Z_MTD_<raggruppamento>_{DT/LV/LH/LM/SC/DL}_enricolabel"):
            self.fail()


        if not self.check("FK_<nome tabella padre senza prefisso T_>[_ enricolabel]"):
            self.fail()
        if not self.check("FK_<nome tabella padre senza prefisso T_>[_ enricolabel]"):
            self.fail()
        if not self.check("FK_<nome tabella padre senza prefisso T_>[_ enricolabel]"):
            self.fail()
        if not self.check("FK_<nome tabella padre senza prefisso T_>[_ enricolabel]"):
            self.fail()


        if not self.check("V_ODS_{AUD/AUD/COM}_{DT/LV/LH/LM/SC}_enricolabel"):
            self.fail()
        if not self.check("V_ODS_{AUD/AUD/COM}_{DT/LV/LH/LM/SC}_enricolabel"):
            self.fail()
        if not self.check("V_ODS_{AUD/AUD/COM}_{DT/LV/LH/LM/SC}_enricolabel"):
            self.fail()
        if not self.check("V_ODS_{AUD/AUD/COM}_{DT/LV/LH/LM/SC}_enricolabel"):
            self.fail()


        if not self.check("MV_ODS_{AUD/AUD/COM}_{DT/LV/LH/LM/SC}_enricolabel"):
            self.fail()
        if not self.check("MV_ODS_{AUD/AUD/COM}_{DT/LV/LH/LM/SC}_enricolabel"):
            self.fail()
        if not self.check("MV_ODS_{AUD/AUD/COM}_{DT/LV/LH/LM/SC}_enricolabel"):
            self.fail()
        if not self.check("MV_ODS_{AUD/AUD/COM}_{DT/LV/LH/LM/SC}_enricolabel"):
            self.fail()


        if not self.check("SEQ_STG_enricolabel    SEQ_ODS_enricolabel    SEQ_DMT_enricolabel    SEQ_TDL_enricolabel"):
            self.fail()
        if not self.check("SEQ_STG_enricolabel    SEQ_ODS_enricolabel    SEQ_DMT_enricolabel    SEQ_TDL_enricolabel"):
            self.fail()
        if not self.check("SEQ_STG_enricolabel    SEQ_ODS_enricolabel    SEQ_DMT_enricolabel    SEQ_TDL_enricolabel"):
            self.fail()
        if not self.check("SEQ_STG_enricolabel    SEQ_ODS_enricolabel    SEQ_DMT_enricolabel    SEQ_TDL_enricolabel"):
            self.fail()

        if not self.check("SEQ_STG_enricolabel    FUN_ODS_enricolabel    FUN_DMT_enricolabel    FUN_TDL_enricolabel"):
            self.fail()
        if not self.check("SEQ_STG_enricolabel    FUN_ODS_enricolabel    FUN_DMT_enricolabel    FUN_TDL_enricolabel"):
            self.fail()
        if not self.check("SEQ_STG_enricolabel    FUN_ODS_enricolabel    FUN_DMT_enricolabel    FUN_TDL_enricolabel"):
            self.fail()
        if not self.check("SEQ_STG_enricolabel    FUN_ODS_enricolabel    FUN_DMT_enricolabel    FUN_TDL_enricolabel"):
            self.fail()

        if not self.check("PRC_STG_enricolabel    PRC_ODS_enricolabel    PRC_DMT_enricolabel    PRC_TDL_enricolabel"):
            self.fail()
        if not self.check("PRC_STG_enricolabel    PRC_ODS_enricolabel    PRC_DMT_enricolabel    PRC_TDL_enricolabel"):
            self.fail()
        if not self.check("PRC_STG_enricolabel    PRC_ODS_enricolabel    PRC_DMT_enricolabel    PRC_TDL_enricolabel"):
            self.fail()
        if not self.check("PRC_STG_enricolabel    PRC_ODS_enricolabel    PRC_DMT_enricolabel    PRC_TDL_enricolabel"):
            self.fail()


        if not self.check("T_ODS_{AUD/AUD/ALL}_{DT/LV/LH/LM/LN/TT/SC}_enricolabel"):
            self.fail()
        if not self.check("T_ODS_{AUD/AUD/ALL}_{DT/LV/LH/LM/LN/TT/SC}_enricolabel"):
            self.fail()
        if not self.check("T_ODS_{AUD/AUD/ALL}_{DT/LV/LH/LM/LN/TT/SC}_enricolabel"):
            self.fail()
        if not self.check("T_ODS_{AUD/AUD/ALL}_{DT/LV/LH/LM/LN/TT/SC}_enricolabel"):
            self.fail()


        if not self.check("T_TDL_{AUD/AUD/ALL}_{DT/LV/LH/LM/LN/TT/SC}_enricolabel"):
            self.fail()
        if not self.check("T_TDL_{AUD/AUD/ALL}_{DT/LV/LH/LM/LN/TT/SC}_enricolabel"):
            self.fail()
        if not self.check("T_TDL_{AUD/AUD/ALL}_{DT/LV/LH/LM/LN/TT/SC}_enricolabel"):
            self.fail()
        if not self.check("T_TDL_{AUD/AUD/ALL}_{DT/LV/LH/LM/LN/TT/SC}_enricolabel"):
            self.fail()


        if not self.check("V_TDL_{AUD/AUD/ALL}_{DT/LV/LH/LM/LN/TT/SC}_enricolabel"):
            self.fail()
        if not self.check("V_TDL_{AUD/AUD/ALL}_{DT/LV/LH/LM/LN/TT/SC}_enricolabel"):
            self.fail()
        if not self.check("V_TDL_{AUD/AUD/ALL}_{DT/LV/LH/LM/LN/TT/SC}_enricolabel"):
            self.fail()
        if not self.check("V_TDL_{AUD/AUD/ALL}_{DT/LV/LH/LM/LN/TT/SC}_enricolabel"):
            self.fail()


        if not self.check("MV_TDL_{AUD/AUD/ALL}_{DT/LV/LH/LM/LN/TT/SC}_enricolabel"):
            self.fail()
        if not self.check("MV_TDL_{AUD/AUD/ALL}_{DT/LV/LH/LM/LN/TT/SC}_enricolabel"):
            self.fail()
        if not self.check("MV_TDL_{AUD/AUD/ALL}_{DT/LV/LH/LM/LN/TT/SC}_enricolabel"):
            self.fail()
        if not self.check("MV_TDL_{AUD/AUD/ALL}_{DT/LV/LH/LM/LN/TT/SC}_enricolabel"):
            self.fail()


        if not self.check("T_MTD_<raggruppamento>_{DT/LV/LH/LM/SC/DL}_<nome tabella A>2<nome tabella B>"):
            self.fail()
        if not self.check("T_MTD_<raggruppamento>_{DT/LV/LH/LM/SC/DL}_<nome tabella A>2<nome tabella B>"):
            self.fail()
        if not self.check("T_MTD_<raggruppamento>_{DT/LV/LH/LM/SC/DL}_<nome tabella A>2<nome tabella B>"):
            self.fail()
        if not self.check("T_MTD_<raggruppamento>_{DT/LV/LH/LM/SC/DL}_<nome tabella A>2<nome tabella B>"):
            self.fail()


        if not self.check("T_DMT_AUD/AUD_{DM/FT/FA/LM}_<nome tabella A>2<nome tabella B>"):
            self.fail()
        if not self.check("T_DMT_AUD/AUD_{DM/FT/FA/LM}_<nome tabella A>2<nome tabella B>"):
            self.fail()
        if not self.check("T_DMT_AUD/AUD_{DM/FT/FA/LM}_<nome tabella A>2<nome tabella B>"):
            self.fail()
        if not self.check("T_DMT_AUD/AUD_{DM/FT/FA/LM}_<nome tabella A>2<nome tabella B>"):
            self.fail()


        if not self.check("P_<nome tabella senza prefisso T_>_<nome campo>_{<valore>|<range_valori>}"):
            self.fail()
        if not self.check("P_<nome tabella senza prefisso T_>_<nome campo>_{<valore>|<range_valori>}"):
            self.fail()
        if not self.check("P_<nome tabella senza prefisso T_>_<nome campo>_{<valore>|<range_valori>}"):
            self.fail()
        if not self.check("P_<nome tabella senza prefisso T_>_<nome campo>_{<valore>|<range_valori>}"):
            self.fail()


        if not self.check("T_STG_{AUD/AUD}_{DT/LV/LH/LM/SC/DL}_<nome tabella A>2<nome tabella B>"):
            self.fail()
        if not self.check("T_STG_{AUD/AUD}_{DT/LV/LH/LM/SC/DL}_<nome tabella A>2<nome tabella B>"):
            self.fail()
        if not self.check("T_STG_{AUD/AUD}_{DT/LV/LH/LM/SC/DL}_<nome tabella A>2<nome tabella B>"):
            self.fail()
        if not self.check("T_STG_{AUD/AUD}_{DT/LV/LH/LM/SC/DL}_<nome tabella A>2<nome tabella B>"):
            self.fail()


        if not self.check("T_ODS_{AUD/AUD/ALL}_{DT/LV/LH/LM/LN/TT/SC}_<nome tabella A>2<nome tabella B>"):
            self.fail()
        if not self.check("T_ODS_{AUD/AUD/ALL}_{DT/LV/LH/LM/LN/TT/SC}_<nome tabella A>2<nome tabella B>"):
            self.fail()
        if not self.check("T_ODS_{AUD/AUD/ALL}_{DT/LV/LH/LM/LN/TT/SC}_<nome tabella A>2<nome tabella B>"):
            self.fail()
        if not self.check("T_ODS_{AUD/AUD/ALL}_{DT/LV/LH/LM/LN/TT/SC}_<nome tabella A>2<nome tabella B>"):
            self.fail()


        if not self.check("T_STG_{AUD/AUD}_{DT/LV/LH/LM/SC/DL}_<nome tabella o vista senza prefissi>_[KEY/RT/DD/WW/MM]"):
            self.fail()
        if not self.check("T_STG_{AUD/AUD}_{DT/LV/LH/LM/SC/DL}_<nome tabella o vista senza prefissi>_[KEY/RT/DD/WW/MM]"):
            self.fail()
        if not self.check("T_STG_{AUD/AUD}_{DT/LV/LH/LM/SC/DL}_<nome tabella o vista senza prefissi>_[KEY/RT/DD/WW/MM]"):
            self.fail()
        if not self.check("T_STG_{AUD/AUD}_{DT/LV/LH/LM/SC/DL}_<nome tabella o vista senza prefissi>_[KEY/RT/DD/WW/MM]"):
            self.fail()


        if not self.check("SYN_MTD_R_<nome oggetto con prefisso>"):
            self.fail()
        if not self.check("SYN_MTD_R_<nome oggetto con prefisso>"):
            self.fail()
        if not self.check("SYN_MTD_R_<nome oggetto con prefisso>"):
            self.fail()
        if not self.check("SYN_MTD_R_<nome oggetto con prefisso>"):
            self.fail()


        if not self.check("SYN_BSC_R_<nome oggetto con prefisso>"):
            self.fail()
        if not self.check("SYN_BSC_R_<nome oggetto con prefisso>"):
            self.fail()
        if not self.check("SYN_BSC_R_<nome oggetto con prefisso>"):
            self.fail()
        if not self.check("SYN_BSC_R_<nome oggetto con prefisso>"):
            self.fail()


        if not self.check("SYN_STG_R_<nome oggetto con prefisso>"):
            self.fail()
        if not self.check("SYN_STG_R_<nome oggetto con prefisso>"):
            self.fail()
        if not self.check("SYN_STG_R_<nome oggetto con prefisso>"):
            self.fail()
        if not self.check("SYN_STG_R_<nome oggetto con prefisso>"):
            self.fail()


        if not self.check("SYN_ODS_R_<nome oggetto con prefisso>"):
            self.fail()
        if not self.check("SYN_ODS_R_<nome oggetto con prefisso>"):
            self.fail()
        if not self.check("SYN_ODS_R_<nome oggetto con prefisso>"):
            self.fail()
        if not self.check("SYN_ODS_R_<nome oggetto con prefisso>"):
            self.fail()


        if not self.check("SYN_DMT_R_<nome oggetto con prefisso>"):
            self.fail()
        if not self.check("SYN_DMT_R_<nome oggetto con prefisso>"):
            self.fail()
        if not self.check("SYN_DMT_R_<nome oggetto con prefisso>"):
            self.fail()
        if not self.check("SYN_DMT_R_<nome oggetto con prefisso>"):
            self.fail()


        if not self.check("SYN_DMT_L_<nome oggetto con prefisso>"):
            self.fail()
        if not self.check("SYN_DMT_L_<nome oggetto con prefisso>"):
            self.fail()
        if not self.check("SYN_DMT_L_<nome oggetto con prefisso>"):
            self.fail()
        if not self.check("SYN_DMT_L_<nome oggetto con prefisso>"):
            self.fail()


        if not self.check("SYN_TDL_R_<nome oggetto con prefisso>"):
            self.fail()
        if not self.check("SYN_TDL_R_<nome oggetto con prefisso>"):
            self.fail()
        if not self.check("SYN_TDL_R_<nome oggetto con prefisso>"):
            self.fail()
        if not self.check("SYN_TDL_R_<nome oggetto con prefisso>"):
            self.fail()


        if not self.check("SYN_TDL_L_<nome oggetto con prefisso>"):
            self.fail()
        if not self.check("SYN_TDL_L_<nome oggetto con prefisso>"):
            self.fail()
        if not self.check("SYN_TDL_L_<nome oggetto con prefisso>"):
            self.fail()
        if not self.check("SYN_TDL_L_<nome oggetto con prefisso>"):
            self.fail()

