#!/usr/bin/env python3
"""
Provided the left side of an ascii style picture it creates the corresponding
right side and thus creates a full picture.

"""
import argparse
import pathlib


def parse_args():
    """
    Parse commandline.

    """
    parser = argparse.ArgumentParser(
        description=__doc__
    )
    parser.add_argument("-i", "--input", help="input text file", required=True)
    args = parser.parse_args()
    return args

def main():
    args = parse_args()
    input_file = pathlib.Path(args.input)

if __name__ == "__main__":
    main()
