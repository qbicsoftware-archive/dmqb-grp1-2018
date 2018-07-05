#!/usr/bin/env python

import os
import unittest
from validators.fasta_validator import Fasta


def complete_path(wdir, path):
    """returns the joined path"""
    return os.path.join(wdir, path)


def get_all_file_paths(dir):
    """returns a list of all the files in the given directory."""
    files = []
    dir_files = os.listdir(dir)

    for df in dir_files:
        if os.path.isfile(os.path.join(dir, df)):
            files.append(os.path.join(dir, df))

    return files

# Define the working directory
working_dir = os.path.dirname(__file__)

PATH_VALID_FILES_AA = complete_path(working_dir, "test_files/valid/fasta_aa")
PATH_VALID_FILES_DNA = complete_path(working_dir, "test_files/valid/fasta_dna")

PATH_CORRUPT_FILES_AA = complete_path(working_dir, "test_files/corrupt/fasta_aa")
PATH_CORRUPT_FILES_DNA = complete_path(working_dir, "test_files/corrupt/fasta_dna")


def get_path(valid, dna, filename):
    """small helper to get the path to the correct file."""
    if valid:
        if dna:
            return complete_path(PATH_VALID_FILES_DNA, filename)
        else:
            return complete_path(PATH_VALID_FILES_AA, filename)
    else:
        if dna:
            return complete_path(PATH_CORRUPT_FILES_DNA, filename)
        else:
            return complete_path(PATH_CORRUPT_FILES_AA, filename)


class TestFasta(unittest.TestCase):
    """Unittest class for automatic testing of the Fasta class in validators.fasta."""

    def test_valid(self):
        """Tests the Fasta validator with valid files"""

        filename = "valid.fasta"
        valid = True
        
        f = Fasta("DNA")

        for file in get_all_file_paths(PATH_VALID_FILES_DNA):
            valid, msg = f.validate_file(file)
            self.assertTrue(valid)
            self.assertEqual(msg, "")

        f = Fasta("AA")
        for file in get_all_file_paths(PATH_VALID_FILES_AA):
            valid, msg = f.validate_file(file)
            self.assertTrue(valid)
            self.assertEqual(msg, "")

    def test_wrong_coding(self):
        """Tests the Fasta validator with a corrupt file that has coding errors in the sequences"""

        filename = "wrongCoding.fasta"
        valid = False

        f = Fasta("DNA")
        valid, msg = f.validate_file(get_path(valid, True, filename))
        self.assertFalse(valid)
        self.assertEqual(msg, "Character not allowed [O] in sequence. at line: 3:10")

        f = Fasta("AA")
        valid, msg = f.validate_file(get_path(valid, False, filename))
        self.assertFalse(valid)
        self.assertEqual(msg, "Character not allowed [J] in sequence. at line: 3:10")

    def test_empty_line(self):
        """Tests the Fasta validator with a corrupt file that contains an empty line"""

        filename = "emptyLine.fasta"
        valid = False

        f = Fasta("DNA")
        valid, msg = f.validate_file(get_path(valid, True, filename))
        self.assertFalse(valid)
        self.assertEqual(msg, "Empty line at line: 3")

        f = Fasta("AA")
        valid, msg = f.validate_file(get_path(valid, False, filename))
        self.assertFalse(valid)
        self.assertEqual(msg, "Empty line at line: 3")

    def test_double_header(self):
        """Tests the Fasta validator with a corrupt file that is missing the sequence to a header"""

        filename = "doubleHeader.fasta"
        valid = False

        f = Fasta("DNA")
        valid, msg = f.validate_file(get_path(valid, True, filename))
        self.assertFalse(valid)
        self.assertEqual(msg, "Header without a sequence in line: 3")

        f = Fasta("AA")
        valid, msg = f.validate_file(get_path(valid, False, filename))
        self.assertFalse(valid)
        self.assertEqual(msg, "Header without a sequence in line: 3")

    def test_all_corrupt(self):
        """Tests the Fasta validator with all corrupt files"""
        f = Fasta("DNA")

        for file in get_all_file_paths(PATH_CORRUPT_FILES_DNA):
            valid, msg = f.validate_file(file)
            self.assertFalse(valid)

        f = Fasta("AA")

        for file in get_all_file_paths(PATH_CORRUPT_FILES_AA):
            valid, msg = f.validate_file(file)
            self.assertFalse(valid)


if __name__ == '__main__':
    unittest.main()
