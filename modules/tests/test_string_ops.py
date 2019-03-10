#!/usr/bin/env python3
"""
Test the string operations.

"""

import unittest

try:
    import modules.string_ops as so
except ImportError:
    import sys
    sys.path.append('../..')
    import modules.string_ops as so


class Test_StringOps(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main(verbosity=2)
