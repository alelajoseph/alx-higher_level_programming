#!/usr/bin/python3

if _name_ == "_main_":
    """Print the sum of a and b."""
    from add_0 import add

    a = 1
    b = 2
    print("{0} + {1} = {2}".format(a, b, add(a, b)))
