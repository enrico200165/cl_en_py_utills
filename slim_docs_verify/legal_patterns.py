
import re

import masks


class IDMatcher(object):

    def __init__(self, name):
        self.name = name
        sistema = None
        etichetta = None
        matched_patterm = None
        pos_gruppo_etichetta = None
        pos_gruppo_sistema = None


    def elabora(self):

        p = re.compile("(<.*?>)")
        p = re.compile("(<.*?>(?:/<.*?>)+)")


        # groups = re.search()
        groups = re.findall(p, self.name)

        print("elaboro name: "+self.name)
        for (i, g) in enumerate(groups):
            print(i, g)




def generate_regex(mask):

    parts = mask.split("_");
    new_parts = []
    for p in parts:
        if False:
            pass
        elif re.match("\{.*\}", p):
            p = p.replace("{", "(").replace("}", ")").replace("/", "|")
            new_parts.append(p)
        else:
            new_parts.append(p)
        new_parts[-1] = new_parts[-1]+"_"

    regex_for_mask = "".join(new_parts)[:-1]
    #print("{}\n{}\n".format(mask,regex_for_mask ))
    return regex_for_mask


def generate_regexes():

    regexes_list = []
    mask_lines = masks.masks_lines_list.split("\n")
    for l in mask_lines:
        if len(l) == 0:
            continue
        r = generate_regex(l)
        regexes_list.append(r)

    return regexes_list



temp_list = generate_regexes()
for r in temp_list:
    m = IDMatcher(r)
    m.elabora()



