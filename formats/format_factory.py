
from formats.fasta import Fasta
from formats.fastq import Fastq

def available_formats():
    """TODO DOC String"""
    return ["fasta-dna", "fasta-aa", "fastq"]


def get_format_from_ending(file_ending):
    """TODO"""
    if file_ending == "fasta":
        return "fasta-dna"
    if file_ending == "fastq":
        return "fastq"

    # in case of an unknown ending return empty string.
    return ""


def get_validator(name):
    """TODO DOC String"""
    if name == "fasta-dna":
        return Fasta("DNA")
    if name == "fasta-aa":
        return Fasta("AA")
    if name == "fastq":
        return Fastq()

    raise Exception("FormatFactory.get_format() - Error: Unknown Format identifier.")
