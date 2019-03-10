#!/usr/bin/env python3
"""
Provided the left side of an ascii style picture it creates the corresponding
right side and thus creates a full picture.

"""
import sys
import argparse
import pathlib
import unittest

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

if __name__ == "__main__":
    main()
