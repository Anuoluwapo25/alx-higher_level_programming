#!/usr/bin/python3

def best_score(a_dictionary):
    mvalue = 0
    mkey = 0

    if (a_dictionary):
        for key, value in a_dictionary.items():
            if value > mvalue:
                mvalue = value
                mkey = key
        return (mkey)

    else:
        return None
