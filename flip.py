#!/usr/bin/env python3
"""
Provided the left side of an ascii style picture it creates the corresponding
right side and thus creates a full picture.

"""
import sys
import argparse
import pathlib
import unittest

import modules.string_ops as so

def parse_args():
    """
    Parse commandline.

    """
    parser = argparse.ArgumentParser(
        description=__doc__
    )
     # in case of unittests we shouldn't have to supply config, poolname and
    # user name
    unittest_requirements = ('--test' not in sys.argv)
    parser.add_argument("-i", "--input", help="input text file",
                        required=unittest_requirements)
    parser.add_argument("--test", help="perform unittests",
                        action="store_true")
    args = parser.parse_args()
    return args

def flip(path):
    """
    Flip the ascii art at path.

    """
    maxlen = 0
    print()
    with open(str(path), "r") as ascii_file:

        # get length of longest line
        for line in ascii_file.readlines():
            length = len(line)
            if length > maxlen:
                maxlen = length

        # go to start of file
        ascii_file.seek(0)

        # flip every line
        for line in ascii_file.readlines():
            string = line
            string = string.replace("\r", "")
            string = string.replace("\n", "")
            string = so.pad_string(string, maxlen-1)
            old_string = string
            string = so.replace_chars(string)
            string = so.flip_string(string)
            print("{}{}".format(old_string, string))

    # one last newline
    print()

def perform_unittests():
    """
    Start unittest for the program.

    """
    tests = unittest.TestLoader().discover('.')
    unittest.runner.TextTestRunner(verbosity=2, buffer=True).run(tests)

    sys.exit("--- Performed unittests, exiting ---")

def main():
    args = parse_args()

    if args.test:
        perform_unittests()

    input_file = pathlib.Path(args.input)
    flip(input_file)

if __name__ == "__main__":
    main()
