#!/usr/bin/python3
""""Defines a function that returns a list"""


def lookup(obj):
    """Return a list of an object's available attributes."""
    return (dir(obj))
