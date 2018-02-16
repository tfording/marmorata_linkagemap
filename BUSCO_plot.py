#author=Tfording

import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import seaborn as sns


def plot_buscos(path_LIST, name_list):

    BUSCO_list = [[] for i in path_LIST]

    counter = 0
    for file in path_LIST:
        fh_open = open(file, 'r')

        for line in fh_open:
            if line[0] == '#':
                pass
            else:
                line = line.strip('\n')
                line = line.strip()
                line = line.split('\t')
                if line == ['']:
                    pass
                else:
                    BUSCO_list[counter].append(line)
        counter += 1
        fh_open.close()

    C_list = []
    S_list = []
    D_list = []
    F_list = []
    M_list = []

    for i in range(len(BUSCO_list)):
        parsepercentages = BUSCO_list[i][0]
        parsepercentages = parsepercentages[0].split(',')
        #print parsepercentages
        C_list.append(float(parsepercentages[0][2:6]))
        #print C
        S_list.append(float(parsepercentages[0][-5:-1]))
        #print S
        D_list.append(float(parsepercentages[1][2:-2]))
        #print D
        F_list.append(float(parsepercentages[2][2:-1]))
        #print F
        M_list.append(float(parsepercentages[3][2:-1]))

    pos_list = [i for i in range(len(path_LIST))]
    width = 0.75

    S_D_list = []
    for i in range(len(S_list)):
        S_D_list.append((S_list[i]+D_list[i]))

    S_D_F_list = []
    for i in range(len(S_list)):
        S_D_F_list.append((S_list[i]+D_list[i]+F_list[i]))

    fig = plt.figure(figsize=(16, 8))

    p1 = plt.barh(pos_list, S_list, width, color='#d7191c')

    p2 = plt.barh(pos_list, D_list, width, color="#fdae61", left=S_list)

    p3 = plt.barh(pos_list, F_list, width, color="#abd9e9", left=S_D_list)

    p4 = plt.barh(pos_list, M_list, width, color="#2c7bb6", left=S_D_F_list)

    ytick_list = [.4, 1.35, 2.4]



    fontP = FontProperties()
    fontP.set_size('small')


    plt.xlabel("Percentage of BUSCOs (2548)", fontsize=14)
    plt.title("Gularis Vertebrate BUSCO Score Plots", fontsize=20)
    plt.yticks(ytick_list, name_list, fontsize=14)
    #plt.legend([p1, p2, p3, p4], ('Complete', "Duplicated", "Fragmented", "Missing"), loc='lower left')
    plt.show()



#plot_buscos(['/Volumes/projects/tfording/a_inornata/run_ino_masked_vert_BUSCO.out/short_summary_ino_masked_vert_BUSCO.out.txt', \
#             '/Volumes/projects/tfording/a_inornata/transcriptome/BUSCO/run_ino_trans_VERT_BUSCO.out/short_summary_ino_trans_VERT_BUSCO.out.txt', \
#             '/Volumes/projects/tfording/a_inornata/BRAKER/braker_v2/AIno/run_VERT_maker_1_BUSCO.out/short_summary_VERT_maker_1_BUSCO.out.txt'],\
#            ['Masked Genome', 'Transcriptome', 'BRAKER Predictions'])

#plot_buscos(['/Volumes/projects/tfording/a_inornata/run_ino_masked_vert_BUSCO.out/short_summary_ino_masked_vert_BUSCO.out.txt', \
#            '/Volumes/projects/tfording/a_inornata/transcriptome/BUSCO/run_ino_trans_VERT_BUSCO.out/short_summary_ino_trans_VERT_BUSCO.out.txt', \
#            '/Volumes/projects/tfording/a_inornata/BRAKER/braker_v2/AIno/run_VERT_maker_1_BUSCO.out/short_summary_VERT_maker_1_BUSCO.out.txt'], \
#            ['Masked Genome', 'Transcriptome', 'BRAKER Predictions'])

plot_buscos(['/Volumes/projects/tfording/gularis/run_gularis_masked_vert_BUSCO.out/short_summary_gularis_masked_vert_BUSCO.out.txt', \
            '/Volumes/projects/tfording/gularis/transcriptome/run_gularis_VERT_alltissues_trinity_2.3.2/short_summary_gularis_VERT_alltissues_trinity_2.3.2.txt'], \
            ['Masked Genome', 'Transcriptome'])








