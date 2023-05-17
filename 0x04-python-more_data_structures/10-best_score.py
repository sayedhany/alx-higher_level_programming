#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    max = list(a_dictionary.values())[0]

    def get_key(val):
        for key, value in a_dictionary.items():
            if val == value:
                return key

    for key, value in a_dictionary.items():
        if value > max:
            max = value
    return get_key(max)
