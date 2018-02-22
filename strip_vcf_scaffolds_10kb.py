#author=Tyler Fording


import argparse

def main(fasta_path, vcf_path, new_vcf):
    '''
strip_vcf_scaffolds_10kb.py
    :param fasta_path:
    :param vcf_path:
    :param new_vcf:
    :return:
    '''
    scaflist = scaffold_list(fasta_path)
    fh = open(vcf_path, 'r')
    fh_out = open(str(new_vcf), 'w')
    for line in fh:
        if line[0] == '#':
            fh_out.write(line)
        else:
            line1 = line.split('\t')
            if line1[0] in scaflist:
                fh_out.write(line)
            else:
                pass


def scaffold_list(fasta_path):
    '''
    This function takes a path to a .fasta file passes the path to readFastaIntoMemory, checks the values under each
     key in the dictionary to see if they meet a lenth requirement. It then stores the key for each value that is
     above the cutoff and returns it.
    :param fasta_path: PATH
    :return: list of scaffold names
    '''
    chrDict = readFastaIntoMemory(fasta_path)
    scaffold_list = []
    for item in chrDict:
        if len(chrDict[item]) < 10000:
            pass
        else:
            scaffold_list.append(item)
    return scaffold_list # in the first use case (Asp marmorata) 223 scaffolds


def readFastaIntoMemory(fasta):
    '''
    This function stores a .fasta into a dictionary with the scaffold name being the key and the value being the
    sequence.
    :param fasta: PATH
    :return: Dictionary of scaffolds with the scaffold name being the key and the sequence being the value
    :author: Aaron Odell
    '''
    chrDict = {}
    fasta = open(fasta,'r')
    ### This loops through our fasta file and creates a new dictionary entry for each new chromosome it comes across. The value is inittially a list that gets appended too for each new line sequence ###
    for line in fasta:
        line = line.strip('\r')
        line = line.strip('\n')
        if line[0] == ">":
            chrName = line[1::]
            if chrName not in chrDict:
                chrDict.update({chrName:[]})
            else:
                return "Error"+'\t'+"Multiple chromosomes with the same name"
        else:
            chrDict[chrName].append(line)
    ### Now we have the whole fasta in memory. We loop through the keys/values and "join" the list of seuqnces together into a single string for each chromsome entry in the dictionary
    for chromosome in chrDict:
        chrDict[chromosome] = ''.join(chrDict[chromosome])
    return chrDict


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="VCF to pre-makeped")
    parser.add_argument("fasta_path", type=str, help="Enter file path to a fasta file", nargs='?')
    parser.add_argument("vcf_path", type=str, help="Enter file path to the vcf to be parsed", nargs='?')
    parser.add_argument("new_vcf", type=str, help="Enter file name for output", nargs='?')
    args = parser.parse_args()


main(args.fasta_path, args.vcf_path, args.new_vcf)


