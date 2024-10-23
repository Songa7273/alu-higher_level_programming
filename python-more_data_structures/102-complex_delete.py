#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if not a_dictionary:
        return a_dictionary

    delete_keys = [k for k in a_dictionary if a_dictionary[k] == value]
    for k in delete_keys:
        del a_dictionary[k]

    return a_dictionary
