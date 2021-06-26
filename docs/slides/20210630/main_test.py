
# %%
# Doctest
import unittest
import doctest


def add(a, b):
    """Return the sum of a and b.

    >>> add(2, 2)
    4
    """
    sum = a
    return sum


doctest.testmod(verbose=True)

# %%
# Unittest


class TestFunction(unittest.TestCase):
    def test_add(self):
        self.assertEquals(add(2, 2), 4)


def add(a, b):
    """Return the sum of a and b."""
    sum = a + b
    return sum


unittest.main(argv=[''], verbosity=2, exit=False)
