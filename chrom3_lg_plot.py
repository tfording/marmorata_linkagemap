#author=Tyler Fording


import matplotlib.pyplot as plt


def wrapperfunc(chrom_num, ChromSeq_path, LG_path, out_path):
    chrSeq_scaffolds = importChrSeqdata(chrom_num, ChromSeq_path)
    LGData = importLGdata(LG_path, chrSeq_scaffolds)


    plotFunc(chrSeq_scaffolds, LGData, out_path)


def importChrSeqdata(chrom_num, chromSeq_path):
    fh_in = open(chromSeq_path, 'r')
    chrSeq_scaffolds = []
    for line in fh_in:
        if line[0] =='#':
            pass
        else:
            line = line.strip('\n')
            line = line.split(',')
            if line[4][-1] == str(chrom_num):
                chrSeq_scaffolds.append(line[0])
    return chrSeq_scaffolds

def importLGdata(LG_path, chrSeq_scaffolds):
    fh_in = open(LG_path, 'r')
    lg_dict = {}

    for line in fh_in:
        line = line.strip('\n')
        line = line.split('\t')
        if line[2] == '0':
            pass
        else:
            if line[0] in chrSeq_scaffolds:
                if str(line[2]) in lg_dict:

                    for key in lg_dict:
                        if lg_dict[key][0] != line[0]:
                            #print 'Scaffolds do not match'
                            pass
                        else:
                            #print 'scaffolds match, adding one to count'
                            lg_dict[key][1] += 1
                else:
                    lg_dict[str(line[2])] = [line[0], 1]
                    #print lg_dict
            else:
                pass

    print lg_dict
    return

def plotFunc(chromSeq, LGData, out_path):
    pass















wrapperfunc(1, '/Volumes/projects/tfording/marmorata/bin/single_chrom_scaffold_groupings_0.5cutoff.csv', '/Volumes/projects/tfording/marmorata/bin/R13_cpl.out', 'cats')
#importChrSeqdata(3, '/Volumes/projects/tfording/marmorata/bin/single_chrom_scaffold_groupings_0.5cutoff.csv')



'''
Chromosome 1
{'10': ['Scpiz6a_122', 946], '13': ['Scpiz6a_72', 16169], '12': ['Scpiz6a_72', 14690], '15': ['Scpiz6a_47', 9689], 
'14': ['Scpiz6a_11', 5037], '16': ['Scpiz6a_72', 6247], '19': ['Scpiz6a_27', 21289], '1': ['Scpiz6a_122', 1], 
'3': ['Scpiz6a_72', 13692], '2': ['Scpiz6a_27', 5389], '5': ['Scpiz6a_65', 18713], '4': ['Scpiz6a_122', 12], 
'7': ['Scpiz6a_122', 1], '6': ['Scpiz6a_122', 1532], '9': ['Scpiz6a_27', 5310]}

Chromosome 2
{'11': ['Scpiz6a_117', 857], '10': ['Scpiz6a_117', 758], '13': ['Scpiz6a_74', 19], '12': ['Scpiz6a_1453', 2], 
'15': ['Scpiz6a_118', 11945], '14': ['Scpiz6a_1453', 4], '16': ['Scpiz6a_117', 1938], '19': ['Scpiz6a_60', 1695], 
'20': ['Scpiz6a_37', 5835], '1': ['Scpiz6a_26', 30907], '3': ['Scpiz6a_90', 438], '2': ['Scpiz6a_117', 1980], 
'5': ['Scpiz6a_74', 19], '4': ['Scpiz6a_102', 9], '7': ['Scpiz6a_117', 879], '6': ['Scpiz6a_117', 857], 
'9': ['Scpiz6a_74', 27], '8': ['Scpiz6a_90', 1030]}

Chromosome 3
{'24': ['Scpiz6a_34', 3676], '10': ['Scpiz6a_73', 15978], '13': ['Scpiz6a_73', 25360], '12': ['Scpiz6a_73', 6847], 
'15': ['Scpiz6a_45', 24], '14': ['Scpiz6a_782', 1356], '22': ['Scpiz6a_39', 4479], '16': ['Scpiz6a_86', 2591], 
'19': ['Scpiz6a_34', 2382], '18': ['Scpiz6a_45', 6], '23': ['Scpiz6a_39', 3060], '20': ['Scpiz6a_39', 2086], 
'1': ['Scpiz6a_45', 4], '3': ['Scpiz6a_73', 13], '2': ['Scpiz6a_66', 3], '5': ['Scpiz6a_73', 26338], 
'4': ['Scpiz6a_170.1', 4], '7': ['Scpiz6a_45', 25], '6': ['Scpiz6a_73', 40], '9': ['Scpiz6a_73', 13], '8': ['Scpiz6a_45', 25]}

'''