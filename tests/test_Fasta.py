#!/usr/bin/env python

import os
import unittest
from formats.fasta import Fasta


def complete_path(wdir, path):
    return os.path.join(wdir, path)

# Define the working directory
working_dir = os.path.dirname(__file__)

PATH_VALID_FILES_AA = complete_path(working_dir, "test_files/valid/fasta_aa")
PATH_VALID_FILES_DNA = complete_path(working_dir, "test_files/valid/fasta_dna")

PATH_CORRUPT_FILES_AA = complete_path(working_dir, "test_files/corrupt/fasta_aa")
PATH_CORRUPT_FILES_DNA = complete_path(working_dir, "test_files/corrupt/fasta_dna")


def get_path(valid, dna, filename):
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
    """TODO DOC String"""

    def test_valid(self):
        """TODO DOC String"""

        filename = "valid.fasta"
        valid = True
        
        f = Fasta("DNA")
        valid, msg = f.validate_file(get_path(valid, True, filename))
        self.assertTrue(valid)
        self.assertEqual(msg, "")

        f = Fasta("AA")
        valid, msg = f.validate_file(get_path(valid, False, filename))
        self.assertTrue(valid)
        self.assertEqual(msg, "")

    def test_wrong_coding(self):
        """TODO DOC String"""

        filename = "wrongCoding.fasta"
        valid = False

        f = Fasta("DNA")
        valid, msg = f.validate_file(get_path(valid, True, filename))
        self.assertFalse(valid)
        self.assertEqual(msg, "Fasta: Character not allowed [O] in sequence at line: 2:10")

        f = Fasta("AA")
        valid, msg = f.validate_file(get_path(valid, False, filename))
        self.assertFalse(valid)
        self.assertEqual(msg, "Fasta: Character not allowed [J] in sequence at line: 2:9")

    def test_empty_line(self):
        """TODO DOC String"""

        filename = "emptyLine.fasta"
        valid = False

        f = Fasta("DNA")
        valid, msg = f.validate_file(get_path(valid, True, filename))
        self.assertFalse(valid)
        self.assertEqual(msg, "Fasta: Error empty line at line: 3")

        f = Fasta("AA")
        valid, msg = f.validate_file(get_path(valid, False, filename))
        self.assertFalse(valid)
        self.assertEqual(msg, "Fasta: Error empty line at line: 3")

    def test_double_header(self):
        """TODO DOC String"""

        filename = "doubleHeader.fasta"
        valid = False

        f = Fasta("DNA")
        valid, msg = f.validate_file(get_path(valid, True, filename))
        self.assertFalse(valid)
        self.assertEqual(msg, "Fasta: Header without a sequence in line: 3")

        f = Fasta("AA")
        valid, msg = f.validate_file(get_path(valid, False, filename))
        self.assertFalse(valid)
        self.assertEqual(msg, "Fasta: Header without a sequence in line: 3")


if __name__ == '__main__':
    unittest.main()
