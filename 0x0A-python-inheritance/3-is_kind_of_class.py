#!/usr/bin/python3
"""Defines a class and inherited class-checking function."""


def is_kind_of_class(obj, a_class):
    """check if an object is an instance or inherited instance of a class.
    Args:
        obj (any): The object to chck.
        a_class (type): The class to match the typr of obj to.
    Returns:
        If obj is an instance or inherited instance of a_class - True.
        Otherwise - False.
        """
    if isinstance(obj, a_classs):
        return True
    return False
