import os
import sys

import unittest


def complete_path(wdir, path):
    return os.path.join(wdir, path)


# Define the working directory
working_dir = os.path.dirname(__file__)

PATH_VALID_FILES = complete_path(working_dir, "testfiles/valid/fasta")
PATH_CORRUPT_FILES = complete_path(working_dir, "testfiles/corrupt/fasta")


class TestFasta(unittest.TestCase):
    """ TODO: Unit Test for the fasta format."""
    pass
