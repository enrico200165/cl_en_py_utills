
import re
import global_defs as g
import logging


import e2bi_patterns as e2p
import e2bipatterns_checks as pc


log = g.init_logging()


class TableNamesChecker(object):

    def __init__(self):
        self._last_matched_pattern_wrapper = None
        self._last_matched_token = None

    def generate_pattern_wrappers(self, ad_hoc_test = None):
        """from list of E2BI patterns build the parse objects that contain
        the objects is needed to check that e2bi pattern against a string
        """
        pattern_wrappers_list = []
        if ad_hoc_test is None:
            mask_lines = e2p.patterns_list.split("\n")
        else:
            if isinstance(ad_hoc_test , list):
                mask_lines = ad_hoc_test
            else:
                log.debug("working with dummy pattern, length {} first chars: \n{} ...".format(
                    len(ad_hoc_test), ad_hoc_test[:79]))
                mask_lines = ad_hoc_test.split("\n")

        mask_lines = [l.strip() for l in mask_lines]

        for l in mask_lines:
            if len(l) == 0:
                continue
            p = pc.PatternWrapper(l)
            pattern_wrappers_list.append(p)

        return pattern_wrappers_list

    def __init__(self, e2bi_patterns_list = None):
        self._patterns = self.generate_pattern_wrappers(e2bi_patterns_list)

    def check_table_name(self, token):

        (self._last_matched_pattern_wrapper, self._last_matched_token ) = (None, None)


        if re.match('".*"', token):
            token = token[1:-1]

        # check if it is matched by one of the patterns
        # TODO now patters are not only for tables, check if must be changed
        for e2bi_pattern in self._patterns:
            if e2bi_pattern.check_stmt_token(token):
                self._last_matched_pattern_wrapper = e2bi_pattern
                self._last_matched_token = token
                log.info("token: \n{} matched by: \n{} from pattern: \n{}".format(
                    token, e2bi_pattern.regex, e2bi_pattern.e2bi_pattern))
                return True

        return False

