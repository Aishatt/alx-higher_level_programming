#!/usr/bin/python3

def safe_print_integer(value):
    safe  = True
    try:
        print("{:d}".format(value))
    except (ValueError,TypeError):
        safe = False
    return safe
