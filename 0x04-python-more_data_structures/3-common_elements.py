#!/usr/bin/python3
def common_elements(set_1, set_2):
    if set_1 and set_2:
        for gtc in set_1:
            for gtc2 in set_2:
                if gtc2 == gtc:
                    return gtc
    return list()
