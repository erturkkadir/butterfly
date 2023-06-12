import os

dna_codons = {
    # 'M' - START, '_' - STOP
    "GCT": "A", "GCC": "A", "GCA": "A", "GCG": "A",
    "TGT": "C", "TGC": "C",
    "GAT": "D", "GAC": "D",
    "GAA": "E", "GAG": "E",
    "TTT": "F", "TTC": "F",
    "GGT": "G", "GGC": "G", "GGA": "G", "GGG": "G",
    "CAT": "H", "CAC": "H",
    "ATA": "I", "ATT": "I", "ATC": "I",
    "AAA": "K", "AAG": "K",
    "TTA": "L", "TTG": "L", "CTT": "L", "CTC": "L", "CTA": "L", "CTG": "L",
    "ATG": "\r\n",
    "AAT": "N", "AAC": "N",
    "CCT": "P", "CCC": "P", "CCA": "P", "CCG": "P",
    "CAA": "Q", "CAG": "Q",
    "CGT": "R", "CGC": "R", "CGA": "R", "CGG": "R", "AGA": "R", "AGG": "R",
    "TCT": "S", "TCC": "S", "TCA": "S", "TCG": "S", "AGT": "S", "AGC": "S",
    "ACT": "T", "ACC": "T", "ACA": "T", "ACG": "T",
    "GTT": "V", "GTC": "V", "GTA": "V", "GTG": "V",
    "TGG": "W",
    "TAT": "Y", "TAC": "Y",
    "TAA": "_", "TAG": "_", "TGA": "_"
}


def data2dna():
    files = os.listdir("./data")
    for file in files:
        fName = "./data/" + file
        print(fName)
        l = 0
        with open(fName, 'r') as rdata:
            with open("./data/out.txt", "a") as wdata:
                lines = rdata.readlines()
                for aline in lines:
                    if aline[0] != '>':
                        bLine = aline.upper().replace('N', '').replace('\r', '').replace('\n', '')\
                            .replace('\r\n', '').replace('\n\r','')
                        l += len(bLine)
                        wdata.write(bLine)
                wdata.write("\r\n")
            wdata.close()
        rdata.close()
        print( format(l, ",") )
    print("all done")


def dna2codon():
    with open("./data/out.txt", "r") as rdata:
        with open("./data/codon.txt", "a") as wdata:
            lines = rdata.readlines()
            for line in lines:
                aa = []
                print(len(line))
                for i in range(0, len(line)-3, 3):
                    cdn = line[i:i+3]
                    if len(cdn) == 3:
                        aa.append(dna_codons[cdn])
                bb = ''.join(str(a) for a in aa)
                wdata.write(str(bb) + "\r\n")
                print(len(bb))
            wdata.write("\r\n")
        wdata.close()
    rdata.close()


data2dna()
dna2codon()


