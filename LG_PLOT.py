#author=Tyler Fording

import argparse
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def makeDataFrame(cpL_mother, cpL_father):

    motherDict = makedict(cpL_mother)
    fatherDict = makedict(cpL_father)
    #print fatherDict
    mother_twodlist = []
    father_twodlist = []

    for key in motherDict:
        mother_twodlist.append([int(key), len(motherDict[key])])
    mother_twodlist = sorted(mother_twodlist)
    mother_markers = []
    for i in mother_twodlist:
        mother_markers.append(i[1])

    for key in fatherDict:
        father_twodlist.append([int(key), len(fatherDict[key])])
    father_twodlist = sorted(father_twodlist)
    father_markers = []
    for i in father_twodlist:
        father_markers.append(i[1])


    groupnum = []
    for i in range(1,65):
        groupnum.append('Group #'+str(i))
    #groupnum = [x for x in range(1,65)]

    df = pd.DataFrame(columns=['Linkage Group', 'Mother', 'Father'])
    df['Linkage Group'] = groupnum
    #print mother_markers
    df['Mother'] = mother_markers
    #print len(father_markers)
    df['Father'] = father_markers

    barplot(df)


def barplot(df):

    pos = list(range(len(df['Linkage Group'])))
    width = 0.40
    fig, ax = plt.subplots(figsize=(20, 10))
    #First set of bars
    plt.bar(pos,
            # using df['mother'] data,
            df['Mother'],
            # of width
            width,
            # with alpha 0.5
            alpha=.70,
            # with color
            color='#EE3224',
            # with label the first value in first_name
            label=df['Linkage Group'][0])

    plt.bar([p + width for p in pos],
            # using df['father'] data,
            df['Father'],
            # of width
            width,
            # with alpha 0.5
            alpha=.70,
            # with color
            color='#F78F1E',
            # with label the second value in first_name
            label=df['Linkage Group'][1])

    ax.set_ylabel('Number of Markers')
    # Set the chart's title
    ax.set_title('Number of Makers Per Linkage Group')
    # Set the position of the x ticks
    ax.set_xticks([p + 2 * width for p in pos])
    # Set the labels for the x ticks
    ax.set_xticklabels(df['Linkage Group'], rotation=45, ha='right')

    # Set x and y limits
    plt.xlim(min(pos) - width, max(pos) + width * 4)
    plt.ylim([0, max(df['Mother']+6000)])


    plt.legend(['Mother', 'Father'], loc='upper right')
    plt.axvline(x=22.90, color='k')

    plt.grid()
    plt.show()


def makedict(cpL_path):
    '''
    This function takes a path to a tsv(CHR POS LG) and creates a dictionary. The key=LG and value=whole line
    :param cpL_path: PATH to cpL file
    :return: dictionary
    '''
    fh = open(cpL_path, 'r')
    dataDict = {}
    for line in fh:
        line = line.strip('\r')
        line = line.strip('\n')
        wline = line
        line = line.split('\t')
        if line[2] in dataDict:
            dataDict[line[2]].append(wline)
        else:
            dataDict.update({line[2]: line})
    return dataDict




if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="VCF to pre-makeped")
    parser.add_argument("cpL_mother", type=str, help="Enter file path to a cpL file", nargs='?') #cpL refers to CHR   POS LG (.tsv)
    parser.add_argument("cpL_father", type=str, help="Enter file path to the cpL to be parsed", nargs='?')
    #parser.add_argument("new_vcf", type=str, help="Enter file name for output", nargs='?')
    args = parser.parse_args()


makeDataFrame(args.cpL_mother, args. cpL_father)
























