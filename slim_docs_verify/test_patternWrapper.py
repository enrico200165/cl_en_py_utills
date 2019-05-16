from unittest import TestCase

import global_defs as g

import e2bipatterns_checks as pc

log = g.init_logging()


class TestPatternWrapper(TestCase):

    def setUp(self):
        # legal_patterns_list = pc.generate_pattern_wrappers(p)
        # self._pw = PatternWrapper()
        pass


    # --- Utility Functions ---
    def check(self, p, v ):
        p = pc.PatternWrapper(p)
        return p.check_stmt_token(v)


    # -- test one/single occurrence ---

    def test_check_stmt_token_one_const_01(self):
        """ 1 constant"""
        if not self.check("FK_TT", "FK_TT"):
            self.fail()
        # these must not match
        if self.check("FK_TT", "FK_TT_TT"):
            self.fail()
        if self.check("FK_TT", "FK_ZZ"):
            self.fail()
        if self.check("FK_TT", "FK_"):
            self.fail()
        return True


    def test_check_stmt_token_one_var_01(self):
        """ 1 constant"""
        if not self.check("FK_<sistema sorgente>", "FK_GDO"):
            self.fail()
        if not self.check("FK_<sistema destinazione>", "FK_TFE"):
            return True
        # below here must not match
        if self.check("FK_AAA", "FK_TFE_AAA"): # fuori posizione
            self.fail()
        if self.check("FK_<sistema sorgente>", "FK_TFE"):
            self.fail()
        if self.check("FK_<sistema destinazione>", "FK_GDO"):
            self.fail()
        if self.check("FK_<sistema destinazione>", "FK"):
            self.fail()
        if self.check("FK_<sistema destinazione>", "FK"):
            self.fail()

        return True



    def test_check_stmt_token_alternative_one(self):
        """ """

        # pseudo alternative
        if not self.check("FK_{<sistema sorgente>}", "FK_GDO"):
            self.fail()
        # consts
        if not self.check("FK_{A}", "FK_A"):
            self.fail()

        # consts
        if not self.check("FK_{A/B/C}", "FK_A") \
                or not self.check("FK_{A/B/C}", "FK_B") \
                or not self.check("FK_{A/B/C}", "FK_C"):
            self.fail()

        if not self.check("FK_{<sistema sorgente>/AA}", "FK_GDO"):
            self.fail()
        if not self.check("FK_{<sistema sorgente>/AA}", "FK_AA"):
            self.fail()
        if not self.check("FK_{<sistema sorgente>/<sistema destinazione>/AA}", "FK_AA"):
            self.fail()
        if not self.check("FK_{<sistema sorgente>/<sistema destinazione>/AA}", "FK_GDO"):
            self.fail()
        if not self.check("FK_{<sistema sorgente>/<sistema destinazione>/AA}", "FK_TFE"):
            self.fail()
        if not self.check("FK_{<sistema sorgente>/<sistema destinazione>/AA/BBB}", "FK_BBB"):
            self.fail()

        # below here they must not match
        if self.check("FK_{<sistema sorgente>/<sistema destinazione>/AA}", "FK_ZZZ"):
            self.fail()
        # fuori posizione
        if self.check("FK_{<sistema sorgente>/<sistema destinazione>/AA/BBB}", "FK_BBB_GDO"):
            self.fail()

        return True


    # def test_sum_tuple(self):
    #     self.assertEqual(sum((1, 2, 2)), 6, "Should be 6")


# -----------------------------------------------

if __name__ == '__main__':
    unittest.main()
