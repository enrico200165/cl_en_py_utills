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


    def test_split_split_e2bi_patterm_01(self):

        patt = "FK[_AA]"
        pw = pc.PatternWrapper(patt)
        (e2bipattern_parts, part_is_optional) = pw.split_e2bi_patterm(patt)
        if not e2bipattern_parts == ["FK", "{AA}"]:
            self.fail()
        if not part_is_optional == [False, True]:
            self.fail()

        patt = "FK[_AA][_BB]"
        pw = pc.PatternWrapper(patt)
        (e2bipattern_parts, part_is_optional) = pw.split_e2bi_patterm(patt)
        if not e2bipattern_parts == ["FK", "{AA}", "{BB}"]:
            self.fail()
        if not part_is_optional == [False, True, True]:
            self.fail()


    def test_split_split_e2bi_patterm_01(self):


        patt = "FK[_AA]"
        pw = pc.PatternWrapper(patt)
        r = pw.generate_regex(patt)

        patt = "FK[_AA/BB]"
        pw = pc.PatternWrapper(patt)
        r = pw.generate_regex(patt)

        patt = 'FK_{<sistema sorgente>/<sistema destinazione>/AA/BBB}'
        pw = pc.PatternWrapper(patt)
        r = pw.generate_regex(patt)
