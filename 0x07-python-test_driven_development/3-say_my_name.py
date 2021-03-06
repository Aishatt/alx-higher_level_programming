#!/usr/bin/python3
"""
This function prints a message with the first and last name
"""


def say_my_name(first_name, last_name):
    """ function that prints "My name is <first name> <last name>"""
    if not isinstance(first_name,str):
        raise TypeError("firstname must be a string")
    if not isinstance(last_name,str):
        raise TypeError("lastname must be a string")

    print(f"My name is {first_name} {last_name}")
