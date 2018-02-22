#author=Tyler Fording

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
    scaffold_list = []
    for key in tenkbDict:
        scaffold_list.append([tenkbDict[key], key])
    scaffold_list = sorted(scaffold_list, reverse=True)

    reversed_scaf_list = []

    for i in range(len(scaffold_list)):
        #print scaffold_list[i]
        item = [scaffold_list[i][1], scaffold_list[i][0]]
        reversed_scaf_list.append(item)

    scflst = [i[1] for i in scaffold_list]
    scflenlst = [i[0] for i in scaffold_list]
    #print scflenlst
    #print scaffold_list
    print reversed_scaf_list
    #print scflst
    #print len(scflst)


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


getLengths('/Volumes/projects/tfording/genomes/Asp/AspMar_1.0.fasta')