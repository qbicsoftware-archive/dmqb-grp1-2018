#!/usr/bin/env python

from formats.fasta.fasta import Fasta


def available_formats():
    return ["fasta-dna", "fasta-aa"]


def get_format(name):
    if name == "fasta-dna":
        return Fasta("DNA")
    if name == "fasta-aa":
        return Fasta("AA")

    raise Exception("FormatFactory.get_format() - Error: Unknown Format identifier.")
