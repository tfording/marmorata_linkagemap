#author=Tyler Fording


def compare_singleChromSEQ_2_LGs(single_chom_path, LG_path):
    single_ChromSEQ_dict = singleCromSEQ_import(single_chom_path)
    lg_dict = LG_import(LG_path)

    for key in single_ChromSEQ_dict:
        print 'This starts the comparison for chromosome: '+str(key)
        for lg in lg_dict:
            print'##########################################################################################################'
            print 'The total number of scaffolds associated with chromosome '+str(key)+': '+str(len(single_ChromSEQ_dict[key]))
            print 'The total number of scaffolds associated with linkage group '+str(lg)+': '+str(len(lg_dict[lg]))
            common = set(single_ChromSEQ_dict[key]) & set(lg_dict[lg])
            exclusive_sChrSeq = set(single_ChromSEQ_dict[key]) - set(lg_dict[lg])
            exclusive_lg = set(lg_dict[lg]) - set(single_ChromSEQ_dict[key])
            print 'The number of common scaffolds between chromosome '+str(key)+' and linkage group '+str(lg)+' are: '+str(len(common))
            print 'The number of exclusive scaffolds for the single chromosome seq data: '+str(len(exclusive_sChrSeq))
            print 'The number of exclusive scaffolds for the linkage group data: ' + str(len(exclusive_lg))
            print '##########################################################################################################'


def singleCromSEQ_import(single_chrp_path):
    fh_in = open(single_chrp_path, 'r')
    SingleChromSEQ_dict = {}
    for line in fh_in:
        if line[0] == '#':
            pass
        else:
            line = line.strip('\n')
            line = line.split(',')
            if line[4] == 'chromosome1':
                if line[4][-1] in SingleChromSEQ_dict:
                    SingleChromSEQ_dict[line[4][-1]].append(line[0])
                else:
                    SingleChromSEQ_dict[line[4][-1]] = [line[0]]
            elif line[4] == 'chromosome2':
                if line[4][-1] in SingleChromSEQ_dict:
                    SingleChromSEQ_dict[line[4][-1]].append(line[0])
                else:
                    SingleChromSEQ_dict[line[4][-1]] = [line[0]]
            elif line[4] == 'chromosome3':
                if line[4][-1] in SingleChromSEQ_dict:
                    SingleChromSEQ_dict[line[4][-1]].append(line[0])
                else:
                    SingleChromSEQ_dict[line[4][-1]] = [line[0]]
    fh_in.close()
    return SingleChromSEQ_dict

def LG_import(LG_path):
    fh_in = open(LG_path, 'r')
    lg_dict = {}

    for line in fh_in:
        if line[0] == '#':
            pass
        else:
            line = line.strip('\n')
            line = line.strip('')
            line = line.split('\t')
            lg_dict[line[0]] = line[1:(len(line)-1)]
    fh_in.close()
    return lg_dict

#LG_import('/Volumes/projects/tfording/marmorata/bin/LG_scaffold_R13.tsv')
#singleCromSEQ_import('/Volumes/projects/tfording/marmorata/bin/single_chrom_scaffold_groupings_0.5cutoff.csv')
compare_singleChromSEQ_2_LGs('/Volumes/projects/tfording/marmorata/bin/single_chrom_scaffold_groupings_0.5cutoff.csv','/Volumes/projects/tfording/marmorata/bin/LG_scaffold_R13.tsv')