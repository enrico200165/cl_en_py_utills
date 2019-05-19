
import global_defs as g

import e2bi_patterns as e2p
import e2bipatterns_checks as pc

log = g.init_logging()


class TableNamesChecker(object):

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
                log.info("working with dummy pattern: " + ad_hoc_test)
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

    def check_table_name(self, table_name):

        # check if it is matched by one of the patterns
        # TODO now patters are not only for tables, check if must be changed
        for e2bi_pattern in self._patterns:
            log.debug(e2bi_pattern.dumpToStr())
            if e2bi_pattern.check_stmt_token(table_name):
                log.debug("table name: {} matched by {}".format(table_name,
                                                                e2bi_pattern.e2bi_pattern))
                return True

        # below here simple checks that should be unnecessary if regex matching works
        # check second (index 1) part of the token
        # (ok, val) = check_token_part(table_name, 1, g.DataLayerSchemi)
        # if not ok:
        #     return False
        # data_layer = val

        # now we know the data layer

        return False

