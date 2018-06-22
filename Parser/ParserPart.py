class parser:
    list = []
    def readPars(self):
        head = ""
        sequence = ""
        file = open('/Users/najiaahmadi/Desktop/dmqb-grp1-2018/Parser/sequencesMSA.fasta')
        for i in file:
            if i.startswith(">"):
                self.list.append((head, sequence))
                if head != "":
                    head =""
                    sequence=""
                head+=i[:-2]
            else:
                sequence+=i[:-2]

        self.list.append((head,sequence))

        self.list = self.list[1:]

        print(self.list)

        file.close()

if __name__ == "__main__":
    parser=parser()
    parser.readPars()
