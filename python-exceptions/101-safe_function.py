#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    """Executes a function safely and handles any exceptions.
    Args:
        fct: Function to execute
        *args: Arguments to pass to the function
    Returns:
        Result of the function if successful, None if an error occurs
    """
    try:
        result = fct(*args)
        return result
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return None
