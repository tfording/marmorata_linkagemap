# author=Tyler Fording

import seaborn as sns
import matplotlib.pyplot as plt

listoflargescaffolds = ['Scpiz6a_49', 'Scpiz6a_55.1', 'Scpiz6a_26', 'Scpiz6a_73', 'Scpiz6a_37', 'Scpiz6a_28',
                        'Scpiz6a_146', 'Scpiz6a_30.1', 'Scpiz6a_65', 'Scpiz6a_27', 'Scpiz6a_72', 'Scpiz6a_11.1']
newList = ['Scpiz6a_11.1', 'Scpiz6a_72', 'Scpiz6a_27', 'Scpiz6a_65', 'Scpiz6a_30.1', 'Scpiz6a_146', 'Scpiz6a_28',
           'Scpiz6a_37', 'Scpiz6a_73', 'Scpiz6a_26', 'Scpiz6a_55.1', 'Scpiz6a_49']


def plotLGonScaf(scaffDict):
    fig, ax = plt.subplots(figsize=(25, 25))
    palette = sns.color_palette("husl", 65)
    sns.set_palette(palette)
    plt.ylim([0, len(listoflargescaffolds)])
    width = 1
    ypossub = 0
    variantsplotted = 0

    for item in listoflargescaffolds:
        current_scaf_poslg = scaffDict[item]
        pos_list = [i[0] for i in current_scaf_poslg]
        LG_list = [i[1] for i in current_scaf_poslg]

        posy = [(len(listoflargescaffolds) - ypossub)] * len(current_scaf_poslg)
        posx = list(range(len(pos_list)))
        print posy[0], '\t', 'Currently processing scaffold', item, "which has", len(scaffDict[item]), "variants"
        variantsplotted += len(scaffDict[item])

        for i in range(0, len(posx)):
            ax.bar(posx[i], 1, width, (posy[i] - 1), color=palette[LG_list[i]], edgecolor=palette[LG_list[i]])
            ax.plot([0, len(posx)], [(posy[i] - 1), (posy[i] - 1)], "k")
        ypossub += 1

    ax.set_yticks([0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5, 11.5])
    ax.set_yticklabels(newList, rotation=45)

    ax.set_xlabel('Number of Markers')
    ax.set_ylabel('Scaffold Name')
    ax.set_title('Markers on 12 Largest Scaffolds by Linkage Group')

    plt.show()
    plt.savefig("father_round2_LG_plot.pdf", bbox_inches='tight')

    print "A total of ", variantsplotted, " variants were plotted"


def importData(cpl_path):
    '''
    This function iterates through a cpl(CHR\tPOS\tLG) file and if the CHR in the file corresponds to the scaffold_name
     given in the arguments, it stores the position and LG in a 2D array. [POS, LG]
    :param cpl_path: PATH to cpl file
    :param scaffold_name: Name of the scaffold you want to look at
    :return: Dictionary of scaffolds with a array of [POS, LG] for values
    '''
    fh = open(cpl_path, 'r')
    scaffDict = {}

    for line in fh:
        line = line.strip('\n')
        line = line.split('\t')
        if line[0] in listoflargescaffolds and line[0] in scaffDict:
            scaffDict[line[0]].append([int(line[1]), int(line[2])])
        elif line[0] in listoflargescaffolds and line[0] not in scaffDict:
            scaffDict[line[0]] = [[int(line[1]), int(line[2])]]
        else:
            pass
    plotLGonScaf(scaffDict)


importData('/Volumes/projects/tfording/marmorata/bin/father_hetHom_round2_clean_cpL.out')
