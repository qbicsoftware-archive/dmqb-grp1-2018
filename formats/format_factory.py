
from formats.fasta import Fasta


def available_formats():
    """TODO DOC String"""
    return ["fasta-dna", "fasta-aa"]


def get_format(name):
    """TODO DOC String"""
    if name == "fasta-dna":
        return Fasta("DNA")
    if name == "fasta-aa":
        return Fasta("AA")

    raise Exception("FormatFactory.get_format() - Error: Unknown Format identifier.")
