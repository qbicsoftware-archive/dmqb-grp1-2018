
import os
import unittest
from validators.fastq_validator import Fastq


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

PATH_VALID_FILES = complete_path(working_dir, "test_files/valid/fastq")
PATH_CORRUPT_FILES = complete_path(working_dir, "test_files/corrupt/fastq")


class TestFastq(unittest.TestCase):
    """Unittest class for automatic testing of the Fastq class in validators.fastq."""

    def test_valid(self):
        """Tests the Fastq validator with all valid files"""
        fastq = Fastq()

        for file in get_all_file_paths(PATH_VALID_FILES):
            valid, msg = fastq.validate_file(file)
            self.assertTrue(valid)
            self.assertEqual(msg, "")

    def test_wrong_coding(self):
        """Tests the Fastq validator files that have a faulty coding in the dna sequence or quality sequence"""
        fastq = Fastq()

        valid, msg = fastq.validate_file(complete_path(PATH_CORRUPT_FILES, "wrong_dna_coding.fastq"))
        self.assertFalse(valid)
        self.assertEqual(msg, "Expected DNA sequence contains banned characters. Line: 2")

        valid, msg = fastq.validate_file(complete_path(PATH_CORRUPT_FILES, "wrong_quality_coding.fastq"))
        self.assertFalse(valid)
        self.assertEqual(msg, "Expected quality sequence contains banned characters. Line: 4")

    def test_missing_line(self):
        """Tests the Fastq validator a files that has a missing line"""
        fastq = Fastq()

        valid, msg = fastq.validate_file(complete_path(PATH_CORRUPT_FILES, "missing_line.fastq"))
        self.assertFalse(valid)
        self.assertEqual(msg, "Expected quality sequence contains banned characters. Line: 4")  # space

    def test_all_corrupt(self):
        """Tests the Fastq validator with all corrupt files"""
        fastq = Fastq()

        for file in get_all_file_paths(PATH_CORRUPT_FILES):
            valid, msg = fastq.validate_file(file)
            self.assertFalse(valid)


if __name__ == '__main__':
    unittest.main()
