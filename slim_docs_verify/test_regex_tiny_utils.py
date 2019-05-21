from unittest import TestCase

import regex_tiny_utils as rtu
import global_defs as g


log = g.init_logging()


class TestDbTinyUtils(TestCase):

    def test_dbtype_with_1size(self):
        (expected, found) = ("pippo", "pippo(10)")
        (ret, n) = rtu.dbtype_with_1size(expected, found)
        if not ret or n != 10:
            self.fail()


    def test_dbtype_with_2size(self):
        (expected, found) = ("pippo", "pippo(10,20)")
        (ret, n1, n2) = rtu.dbtype_with_2size(expected, found)
        if not ret or n1 != 10 or n2 != 20:
            self.fail()
