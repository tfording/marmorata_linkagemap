#author=Tyler Fording

import matplotlib.pyplot as plt
import pandas as pd


def prep_data(fasta_path, cpl_path):
    '''
    This function sends raw data to other functions and, transforms it as needed, and then sends it to the plot
     function.
    :param fasta_path: PATH to fasta file
    :param cpl_path: PATH to CHR POS LG tsv
    :return: none
    '''
    scaf_list = scaffold_list(fasta_path)
    ChrDict = loadCPL(cpl_path)
    scaf_names = []
    for item in scaf_list:  # This loop removes the scaffold name from the 2D array and stores it in a new array
        scaf_names.append(item[1])
    LG_num_list = []
    plotList = []
    for item in scaf_names:
        if item in ChrDict:
            LG_num_list.append(len(ChrDict[item]))
            plotList.append(item)


    if len(plotList) == len(LG_num_list):
        makeDataFrame(plotList, LG_num_list)
    else:
        print 'NOPE'


def makeDataFrame(scaf_list, lg_list):
    df = pd.DataFrame(columns=['Scaffolds', 'Number of Linkage Groups'])
    df['Scaffolds'] = scaf_list
    df['Number of Linkage Groups'] = lg_list

    hist_plot(df)


def hist_plot(df):
    pos = list(range(len(df['Number of Linkage Groups'])))
    width = 0.40
    fig, ax = plt.subplots(figsize=(20, 10))

    plt.bar(pos, df['Number of Linkage Groups'], width, alpha=.7, color='#EE3224')



    ax.set_ylabel('Number of Linkage Groups')
    ax.set_title('Number of Linkage Groups Per Scaffold')
    ax.set_xticks([p + 2 * width for p in pos])
    ax.set_xticklabels(df['Scaffolds'], rotation=45, ha='right')

    plt.grid()
    plt.show()


def loadCPL(pATH):
    '''
    This function loads the CHR POS LG tsv into a dictionary with the scaffold(CHR) as the key and the LG as it's value
    :param pATH: PATH TO CHR POS LG tsv
    :return: Dictionary
    '''
    fh = open(pATH, 'r')
    ChrDict = {}

    for line in fh:
        line = line.strip('\r')
        line = line.strip('\n')
        line2 = line.split('\t')
        LG = line2[2]
        Chr = line2[0]
        if Chr not in ChrDict:
            ChrDict[Chr] = [int(LG)]
        else:
            if int(LG) in ChrDict[Chr]:
                pass
            else:
                ChrDict[Chr].append(int(LG))
    print 'CPL Loaded'
    return ChrDict


def scaffold_list(fasta_path):
    '''
    This function takes a path to a .fasta file passes the path to readFastaIntoMemory, checks the values under each
     key in the dictionary to see if they meet a lenth requirement. It then stores the key for each value that is
     above the cutoff and returns it.
    :param fasta_path: PATH
    :return: list of scaffold names if order of largest to smallest
    '''
    chrDict = readFastaIntoMemory(fasta_path)
    scaffold_list = []
    for item in chrDict:
        if len(chrDict[item]) < 1:
            pass
        else:
            scaffold_list.append([len(chrDict[item]), item])
    scaffold_list = sorted(scaffold_list, reverse=True)
    print 'Scaffolds Loaded'
    return scaffold_list


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


prep_data('/Volumes/projects/tfording/genomes/AspMar_1.0.fasta', '/Volumes/projects/tfording/a_marmorata/bin/mother_clean_cpL.out')