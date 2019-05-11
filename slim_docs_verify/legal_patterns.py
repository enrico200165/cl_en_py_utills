
import re

import masks

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
    print("{}\n{}\n".format(mask,regex_for_mask ))
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


