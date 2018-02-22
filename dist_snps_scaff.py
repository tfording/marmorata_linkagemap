#author=Tyler Fording

import matplotlib.pyplot as plt


def makePlotData(scaffold, snp_list, scaf_len, scaffold_name):
    '''
    
    :param scaffold: 
    :param snp_list: 
    :param scaf_len: 
    :return: 
    '''
    print "Plotting function initiated (4)"
    position_list = []  # This list is a list of the number of snps in each 10kb bin

    bins = int(scaf_len/10000)

    for i in range(bins):
        pos_list = []
        for pos in snp_list:
            if int(pos) >= i*10000 and int(pos) <= (i+1)*10000:
                pos_list.append(pos)
            else:
                pass
        #print (pos_list)
        position_list.append(len(pos_list))
    print "Data prepped for matplot (5)"

    xlist = [i+1 for i in range(len(position_list))]

    plt.subplots(figsize=(8, 16))
    plt.plot(position_list, xlist, 'r-')
    plt.axis([0, 8502, 0, 760])
    plt.set_ylabel('Number of SNPs')
    plt.set_xlabel('10kb bin')
    plt.set_title(scaffold_name)
    plt.show()

    # CHR            num_snps    scaf_len
    # Scpiz6a_49     385288      85027298


def main(fasta, vcf, scaffold_name):
    '''
    This function is the wrapper function for this program.
    :param fasta: PATH to a genome fasta
    :param vcf: PATH to a snp vcf
    :return: none
    '''
    vcfDict = importVCF(vcf)
    scafLenDict = getLengths(fasta)
    makePlotData(scaffold_name, vcfDict[scaffold_name], scafLenDict[scaffold_name], scaffold_name)

    #for scaffold in vcfDict:
        #makePlotData(scaffold, vcfDict[scaffold], scafLenDict[scaffold])


def getLengths(fasta):
    '''
    This function creates a dictionary where key=scaffold name and value=length of the scaffold
    :param fasta: PATH to a fasta 
    :return: SCAFF:len(SCAFF) Dictionary
    '''
    scaffDict = readFastaIntoMemory(fasta)

    tenkbDict = {}
    for key in scaffDict:
        if len(scaffDict[key]) >= 10000:
            tenkbDict[key] = len(scaffDict[key])
    scaffDict = {}
    print "Lengths Loaded (3)"
    return tenkbDict


def importVCF(vcfpath):
    '''
    This function creates a dictionary from a VCF file. The key=CHR and value=POS
    :param vcfpath: PATH to a vcf
    :return: CHR:POS Dictionary
    '''
    fh = open(vcfpath, 'r')
    vcfDict = {}
    for line in fh:
        if line[0] == '#':
            pass
        else:
            line = line.split('\t')
            CHR = line[0]
            POS = line[1]
            if CHR in vcfDict:
                vcfDict[CHR].append(POS)
            else:
                vcfDict[CHR] = [POS]
    print "vcf Loaded (1)"
    return vcfDict


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
    print "Fasta Loaded (2)"
    return chrDict


main('/Volumes/projects/tfording/genomes/AspMar_1.0.fasta', '/Volumes/projects/tfording/marmorata/bin/snps_clean2_haplotypeCallerVariants.vcf', 'Scpiz6a_49')
