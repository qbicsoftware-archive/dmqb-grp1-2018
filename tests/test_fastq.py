
import os
import unittest
from formats.fastq import Fastq


def complete_path(wdir, path):
    """"""
    return os.path.join(wdir, path)


# Define the working directory
working_dir = os.path.dirname(__file__)

PATH_VALID_FILES = complete_path(working_dir, "test_files/valid/fastq")
PATH_CORRUPT_FILES = complete_path(working_dir, "test_files/corrupt/fastq")


class TestFastq(unittest.TestCase):
    """Unittest class to test the functionality of the fastq validator"""

    def test_valid(self):
        fastq = Fastq()

        valid, msg = fastq.validate_file(complete_path(PATH_VALID_FILES, "valid.fastq"))
        self.assertTrue(valid)
        self.assertEqual(msg, "")

    def test_wrong_coding(self):
        fastq = Fastq()

        valid, msg = fastq.validate_file(complete_path(PATH_CORRUPT_FILES, "wrong_dna_coding.fastq"))
        self.assertFalse(valid)
        self.assertEqual(msg, "Fastq: Expected DNA sequence contains banned characters. Line: 2")

        valid, msg = fastq.validate_file(complete_path(PATH_CORRUPT_FILES, "wrong_quality_coding.fastq"))
        self.assertFalse(valid)
        self.assertEqual(msg, "Fastq: Expected quality sequence contains banned characters. Line: 4")

    def test_missing_line(self):
        fastq = Fastq()

        valid, msg = fastq.validate_file(complete_path(PATH_CORRUPT_FILES, "missing_line.fastq"))
        self.assertFalse(valid)
        self.assertEqual(msg, "Fastq: Expected quality sequence contains banned characters. Line: 4")  # space


if __name__ == '__main__':
    unittest.main()
