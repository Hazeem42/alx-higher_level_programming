#!/usr/bin/python3
"""Defines a Puyhon class-to-JSON function."""


def class_to_json(obj):
    """Return the dctionary representation of a simple data structure."""
    return obj.__dict__
