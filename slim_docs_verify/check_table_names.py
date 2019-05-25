
import re
import global_defs as g
import logging


import patterns_table_names as e2p
import e2bipatterns_checks as pc


log = g.init_logging()


class PatternsListChecker(object):

    def __init__(self, pattern_lines):
        self._last_matched_pattern_wrapper = None
        self._last_matched_token = None
        self._pattern_lines = pattern_lines

    def generate_pattern_wrappers(self, pattern_lines_par = None):
        """from list of E2BI patterns build the parse objects that contain
        the objects is needed to check that e2bi pattern against a string
        """

        self._pattern_lines = pattern_lines_par if pattern_lines_par is not None else self._pattern_lines

        mask_lines = [l.strip() for l in self._pattern_lines.split("\n")]

        pattern_wrappers_list = []
        for l in mask_lines:
            if len(l) == 0:
                continue
            p = pc.PatternWrapper(l)
            pattern_wrappers_list.append(p)

        return pattern_wrappers_list

    def __init__(self, e2bi_patterns_list = None):
        self._patterns = self.generate_pattern_wrappers(e2bi_patterns_list)

    def check_against_patterns(self, token):

        (self._last_matched_pattern_wrapper, self._last_matched_token ) = (None, None)

        # remove "" around table name, if any
        token = token[1:-1] if re.match('".*"', token) else token

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

