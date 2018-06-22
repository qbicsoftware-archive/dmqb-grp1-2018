import os
import unittest
from formats.fasta import Fasta


def complete_path(wdir, path):
    return os.path.join(wdir, path)


# Define the working directory
working_dir = os.path.dirname(__file__)

PATH_VALID_FILES = complete_path(working_dir, "tests/testFiles/valid")
PATH_CORRUPT_FILES = complete_path(working_dir, "tests/testFiles/corrupt")


class TestFasta(unittest.TestCase):
    """ TODO: Unit Test for the fasta format."""
    def test_valid(self):
        f = Fasta("DNA")
        self.assertTrue(f.validate_file(PATH_VALID_FILES + "/fastaDNA/valid.fasta"))

        f = Fasta("AA")
        self.assertTrue(f.validate_file(PATH_VALID_FILES + "/fastaAA/valid.fasta"))

    def test_wrong_coding(self):
        f = Fasta("DNA")
        with self.assertRaises(Exception):
            f.validate_file(PATH_CORRUPT_FILES + "/fastaDNA/wrongCoding.fasta")

        f = Fasta("AA")
        with self.assertRaises(Exception):
            f.validate_file(PATH_CORRUPT_FILES + "/fastaAA/wrongCoding.fasta")

    def test_empty_line(self):
        f = Fasta("DNA")
        with self.assertRaises(Exception):
            f.validate_file(PATH_CORRUPT_FILES + "/fastaDNA/emptyLine.fasta")

        f = Fasta("AA")
        with self.assertRaises(Exception):
            f.validate_file(PATH_CORRUPT_FILES + "/fastaAA/emptyLine.fasta")

    def test_double_header(self):
        f = Fasta("DNA")
        with self.assertRaises(Exception):
            f.validate_file(PATH_CORRUPT_FILES + "/fastaDNA/doubleHeader.fasta")

        f = Fasta("AA")
        with self.assertRaises(Exception):
            f.validate_file(PATH_CORRUPT_FILES + "/fastaAA/doubleHeader.fasta")


if __name__ == '__main__':
    unittest.main()
