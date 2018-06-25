#!/usr/bin/env python

from formats.fasta import Fasta


def get_format(name):
    if name == "fastaDna":
        return Fasta("DNA")
    if name == "fastaAA":
        return Fasta("AA")

    raise Exception("FormatFactory.get_format() - Error: Unknown Format identifier.")
