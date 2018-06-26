#!/usr/bin/env python

from formats.abstract_format import AbsFormat

"""
Fasta format validator following the NCBI definition.
https://blast.ncbi.nlm.nih.gov/Blast.cgi?CMD=Web&PAGE_TYPE=BlastDocs&DOC_TYPE=BlastHelp (17.6.18)

"""


class Fasta(AbsFormat):

    def __init__(self, code):
        if code == "DNA":
            self.allowed = self.get_dna()
        if code == "AA":
            self.allowed = self.get_aa()

    def validate_file(self, file_path):
        file = open(file_path, "r")

        had_header = False
        count = 1
        for line in file:
            line = line.strip()
            if line == "":
                file.close()
                raise Exception("Fasta.validate_file() - Error empty line at line: " + str(count), file_path)

            if had_header:
                if line.startswith(">"):
                    file.close()
                    raise Exception("Fasta.validate_file() - Header without a sequence in line: " + str(count-1), file_path)

                # test for the
                c_count = 1
                for c in line:
                    if c in self.allowed:
                        c_count += 1
                        continue
                    else:
                        file.close()
                        raise Exception("Fasta.validate_file() - Character not allowed [" + c + "] in sequence in line: "
                                        + str(count) + ":" + str(c_count), file_path)

                had_header = False
                count += 1

            else:
                if line.startswith(">"):
                    had_header = True
                    count += 1
                    continue

        if had_header:
            file.close()
            raise Exception("Fasta.validate_file() - Header at end of file with no sequence.", file_path)

        file.close()
        return True



    """
        A  adenosine          C  cytidine             G  guanine
        T  thymidine          N  A/G/C/T (any)        U  uridine 
        K  G/T (keto)         S  G/C (strong)         Y  T/C (pyrimidine) 
        M  A/C (amino)        W  A/T (weak)           R  G/A (purine)        
        B  G/T/C              D  G/A/T                H  A/C/T      
        V  G/C/A              -  gap of indeterminate length
    """
    def get_dna(self):
        return ['A', 'C', 'G', 'T', 'N', 'U', 'K', 'S', 'Y', 'M', 'W', 'R', 'B', 'D', 'H', 'V', '-']

    """
        A  alanine               P  proline       
        B  aspartate/asparagine  Q  glutamine      
        C  cystine               R  arginine      
        D  aspartate             S  serine      
        E  glutamate             T  threonine      
        F  phenylalanine         U  selenocysteine
        G  glycine               V  valine        
        H  histidine             W  tryptophan        
        I  isoleucine            Y  tyrosine
        K  lysine                Z  glutamate/glutamine
        L  leucine               X  any
        M  methionine            *  translation stop
        N  asparagine            -  gap of indeterminate length
    """

    def get_aa(self):
        return ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
                'W', 'Y', 'Z', 'X', '*', '-']
