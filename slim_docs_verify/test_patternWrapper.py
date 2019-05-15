from unittest import TestCase

import global_defs as g

import e2bipatterns_checks as pc

class TestPatternWrapper(TestCase):

    def setUp(self):
        # legal_patterns_list = pc.generate_pattern_wrappers(p)
        # self._pw = PatternWrapper()
        pass


    def check(self, p, v ):
        p = pc.PatternWrapper(p)
        return pc.PatternWrapper(v)


    def test_check_stmt_token_01(self):
        if not self.check("FK_<sistema sorgente>_TT_KK","create table FK_GDO_TT_KK"):
            self.fail()
        return True


    # def test_sum_tuple(self):
    #     self.assertEqual(sum((1, 2, 2)), 6, "Should be 6")


# -----------------------------------------------

if __name__ == '__main__':
    unittest.main()
