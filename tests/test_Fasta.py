#!/usr/bin/env python

import os
import unittest
from formats.fasta import Fasta


def complete_path(wdir, path):
    return os.path.join(wdir, path)


# Define the working directory
working_dir = os.path.dirname(__file__)

PATH_VALID_FILES = complete_path(working_dir, "testFiles/valid")
PATH_CORRUPT_FILES = complete_path(working_dir, "testFiles/corrupt")


class TestFasta(unittest.TestCase):
    """TODO DOC String"""
    def test_valid(self):
        """TODO DOC String"""
        f = Fasta("DNA")
        valid, msg = f.validate_file(PATH_VALID_FILES + "/fastaDNA/valid.fasta")
        self.assertTrue(valid)
        self.assertEqual(msg, "")

        f = Fasta("AA")
        valid, msg = f.validate_file(PATH_VALID_FILES + "/fastaAA/valid.fasta")
        self.assertTrue(valid)
        self.assertEqual(msg, "")

    def test_wrong_coding(self):
        """TODO DOC String"""
        f = Fasta("DNA")
        valid, msg = f.validate_file(PATH_CORRUPT_FILES + "/fastaDNA/wrongCoding.fasta")
        self.assertFalse(valid)
        self.assertEqual(msg, "Fasta: Character not allowed [O] in sequence at line: 2:10")

        f = Fasta("AA")
        valid, msg = f.validate_file(PATH_CORRUPT_FILES + "/fastaAA/wrongCoding.fasta")
        self.assertFalse(valid)
        self.assertEqual(msg, "Fasta: Character not allowed [J] in sequence at line: 2:9")

    def test_empty_line(self):
        """TODO DOC String"""
        f = Fasta("DNA")
        valid, msg = f.validate_file(PATH_CORRUPT_FILES + "/fastaDNA/emptyLine.fasta")
        self.assertFalse(valid)
        self.assertEqual(msg, "Fasta: Error empty line at line: 3")

        f = Fasta("AA")
        valid, msg = f.validate_file(PATH_CORRUPT_FILES + "/fastaAA/emptyLine.fasta")
        self.assertFalse(valid)
        self.assertEqual(msg, "Fasta: Error empty line at line: 3")

    def test_double_header(self):
        """TODO DOC String"""
        f = Fasta("DNA")
        valid, msg = f.validate_file(PATH_CORRUPT_FILES + "/fastaDNA/doubleHeader.fasta")
        self.assertFalse(valid)
        self.assertEqual(msg, "Fasta: Header without a sequence in line: 3")

        f = Fasta("AA")
        valid, msg = f.validate_file(PATH_CORRUPT_FILES + "/fastaAA/doubleHeader.fasta")
        self.assertFalse(valid)
        self.assertEqual(msg, "Fasta: Header without a sequence in line: 3")


if __name__ == '__main__':
    unittest.main()
