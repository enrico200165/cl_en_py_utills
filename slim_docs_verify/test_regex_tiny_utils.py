from unittest import TestCase

import regex_tiny_utils as rtu
import global_defs as g


log = g.init_logging()


class TestDbTinyUtils(TestCase):

    def test_dbtype_with_1size(self):
        (expected, found) = ("pippo", "pippo(10)")
        val = rtu.Val1Wrapper(0)
        ret = rtu.matches_dbtype_with_1size(expected, found, val)
        if not ret or val.val != 10:
            self.fail()


    def test_dbtype_with_2size(self):
        (expected, found) = ("pippo", "pippo(10,20)")
        v2 = rtu.Val2Wrapper(0,0)
        ret = rtu.matches_dbtype_with_2size(expected, found, v2)
        if not ret or v2.val1 != 10 or v2.val2 != 20:
            self.fail()
