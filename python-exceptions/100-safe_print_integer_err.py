#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    """Prints an integer with error handling.
    Args:
        value: Value to print (can be any type)
    Returns:
        True if value was printed successfully (is an integer),
        False if value could not be printed as an integer
    """
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError) as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return False
