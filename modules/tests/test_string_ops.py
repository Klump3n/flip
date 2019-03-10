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

    def test_flip_empty_string(self):
        """flip empty string
        """
        res = so.flip_string("")
        self.assertEqual(res, "")

    def test_flip_onechar_string(self):
        """flip one char string
        """
        res = so.flip_string("a")
        self.assertEqual(res, "a")

    def test_flip_twochar_string(self):
        """flip two char string
        """
        res = so.flip_string("nm")
        self.assertEqual(res, "mn")

    def test_flip_twochar_space_string(self):
        """flip two char string with space
        """
        res = so.flip_string("nm ")
        self.assertEqual(res, " mn")

    def test_string_padding_no_arg(self):
        """add padding to the string; no length raises ValueError
        """
        with self.assertRaises(ValueError):
            res = so.pad_string("a")

    def test_string_padding_short_length(self):
        """add padding to the string; short length raises ValueError
        """
        with self.assertRaises(ValueError):
            res = so.pad_string("aa", 1)

    def test_string_padding_same_length(self):
        """add padding to the string; same length causes no change
        """
        res = so.pad_string("aa", 2)
        self.assertEqual(res, "aa")

    def test_string_padding_more_length(self):
        """add padding to the string; same length causes no change
        """
        res = so.pad_string("aa", 3)
        self.assertEqual(res, "aa ")

        res = so.pad_string("aa", 5)
        self.assertEqual(res, "aa   ")

    def test_replace_chars(self):
        """swap characters in the string
        """
        res = so.replace_chars("d")
        self.assertEqual(res, "b")

        res = so.replace_chars("b")
        self.assertEqual(res, "d")

        res = so.replace_chars("p")
        self.assertEqual(res, "q")

        res = so.replace_chars("q")
        self.assertEqual(res, "p")

        res = so.replace_chars("/")
        self.assertEqual(res, "\\")

        res = so.replace_chars("\\")
        self.assertEqual(res, "/")

        res = so.replace_chars("´")
        self.assertEqual(res, "`")

        res = so.replace_chars("`")
        self.assertEqual(res, "´")



if __name__ == '__main__':
    unittest.main(verbosity=2)
