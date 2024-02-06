#!/usr/bin/python3
class list:
    """list is base class"""


class MyList(list):
    """Enacts sorted printing for the built-in list class."""

    def print_sorted(self):
        """Print a list in sorted ascending order."""
        print(sorted(self))