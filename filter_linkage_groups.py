#author=Tyler Fording
from __future__ import division
# Largest 199 scaffolds (>= 15kb)
scaffolds_list = ['Scpiz6a_49', 'Scpiz6a_55.1', 'Scpiz6a_26', 'Scpiz6a_73', 'Scpiz6a_37', 'Scpiz6a_28', 'Scpiz6a_146', 'Scpiz6a_30.1', 'Scpiz6a_65', 'Scpiz6a_27', 'Scpiz6a_72', 'Scpiz6a_11.1', 'Scpiz6a_1', 'Scpiz6a_43', 'Scpiz6a_17.2', 'Scpiz6a_120', 'Scpiz6a_74', 'Scpiz6a_147', 'Scpiz6a_118', 'Scpiz6a_122', 'Scpiz6a_45', 'Scpiz6a_47', 'Scpiz6a_44', 'Scpiz6a_29', 'Scpiz6a_44.1', 'Scpiz6a_86', 'Scpiz6a_75', 'Scpiz6a_148', 'Scpiz6a_113', 'Scpiz6a_173', 'Scpiz6a_11', 'Scpiz6a_117', 'Scpiz6a_39', 'Scpiz6a_170.1', 'Scpiz6a_32.1', 'Scpiz6a_253', 'Scpiz6a_90', 'Scpiz6a_201', 'Scpiz6a_66', 'Scpiz6a_115', 'Scpiz6a_23', 'Scpiz6a_22', 'Scpiz6a_696', 'Scpiz6a_30', 'Scpiz6a_232', 'Scpiz6a_18.1', 'Scpiz6a_378', 'Scpiz6a_593', 'Scpiz6a_423', 'Scpiz6a_150', 'Scpiz6a_34', 'Scpiz6a_264', 'Scpiz6a_55', 'Scpiz6a_81.1', 'Scpiz6a_263', 'Scpiz6a_119', 'Scpiz6a_1453', 'Scpiz6a_136.1', 'Scpiz6a_60', 'Scpiz6a_32', 'Scpiz6a_17', 'Scpiz6a_19', 'Scpiz6a_115.1', 'Scpiz6a_782', 'Scpiz6a_382', 'Scpiz6a_16', 'Scpiz6a_152.1', 'Scpiz6a_136', 'Scpiz6a_55.2', 'Scpiz6a_87', 'Scpiz6a_745', 'Scpiz6a_393', 'Scpiz6a_462', 'Scpiz6a_391.1', 'Scpiz6a_23.1', 'Scpiz6a_99', 'Scpiz6a_102', 'Scpiz6a_105', 'Scpiz6a_565', 'Scpiz6a_434', 'Scpiz6a_1005', 'Scpiz6a_970', 'Scpiz6a_2672', 'Scpiz6a_1376', 'Scpiz6a_68', 'Scpiz6a_185', 'Scpiz6a_8', 'Scpiz6a_393.1', 'Scpiz6a_3382', 'Scpiz6a_423.1', 'Scpiz6a_269', 'Scpiz6a_31', 'Scpiz6a_458', 'Scpiz6a_126.1', 'Scpiz6a_338', 'Scpiz6a_642', 'Scpiz6a_1476', 'Scpiz6a_126', 'Scpiz6a_597', 'Scpiz6a_1590', 'Scpiz6a_447', 'Scpiz6a_746', 'Scpiz6a_177', 'Scpiz6a_368', 'Scpiz6a_289', 'Scpiz6a_52', 'Scpiz6a_53.1', 'Scpiz6a_291', 'Scpiz6a_391', 'Scpiz6a_328', 'Scpiz6a_3673', 'Scpiz6a_401', 'Scpiz6a_295', 'Scpiz6a_85.1', 'Scpiz6a_1276', 'Scpiz6a_53', 'Scpiz6a_435', 'Scpiz6a_85', 'Scpiz6a_666', 'Scpiz6a_1742', 'Scpiz6a_5', 'Scpiz6a_808', 'Scpiz6a_1511', 'Scpiz6a_746.1', 'Scpiz6a_2423', 'Scpiz6a_435.1', 'Scpiz6a_960', 'Scpiz6a_7', 'Scpiz6a_1185', 'Scpiz6a_627', 'Scpiz6a_5.1', 'Scpiz6a_255', 'Scpiz6a_231', 'Scpiz6a_21', 'Scpiz6a_408', 'Scpiz6a_610', 'Scpiz6a_396', 'Scpiz6a_656', 'Scpiz6a_177.1', 'Scpiz6a_132', 'Scpiz6a_415', 'Scpiz6a_428', 'Scpiz6a_455', 'Scpiz6a_2379', 'Scpiz6a_1473', 'Scpiz6a_964', 'Scpiz6a_428.1', 'Scpiz6a_10', 'Scpiz6a_1049', 'Scpiz6a_1172', 'Scpiz6a_3445', 'Scpiz6a_442', 'Scpiz6a_1520', 'Scpiz6a_2465', 'Scpiz6a_383', 'Scpiz6a_141', 'Scpiz6a_1123', 'Scpiz6a_1204', 'Scpiz6a_339', 'Scpiz6a_18', 'Scpiz6a_707', 'Scpiz6a_1255', 'Scpiz6a_1801', 'Scpiz6a_667', 'Scpiz6a_781', 'Scpiz6a_132.1', 'Scpiz6a_1492', 'Scpiz6a_2065', 'Scpiz6a_1122', 'Scpiz6a_1863', 'Scpiz6a_2735', 'Scpiz6a_121', 'Scpiz6a_400', 'Scpiz6a_1036', 'Scpiz6a_1583', 'Scpiz6a_318', 'Scpiz6a_927', 'Scpiz6a_3236', 'Scpiz6a_60.1', 'Scpiz6a_2597', 'Scpiz6a_579', 'Scpiz6a_17.1', 'Scpiz6a_840', 'Scpiz6a_989', 'Scpiz6a_765', 'Scpiz6a_859', 'Scpiz6a_2124', 'Scpiz6a_894', 'Scpiz6a_700', 'Scpiz6a_1314', 'Scpiz6a_760', 'Scpiz6a_2089', 'Scpiz6a_163', 'Scpiz6a_2886', 'Scpiz6a_758', 'Scpiz6a_2136', 'Scpiz6a_1085', 'Scpiz6a_2425', 'Scpiz6a_875']


def load_vcf(ParentCall_path, SepIden_path):
    '''
    Reads ParentCall.out and SeparateIdenticals.out and creates a dictionary {Scaffold: [Pos, LG]}
    :param ParentCall_path: PATH to ParentCall2.out
    :param SepIden_path: Path to SeparateIdenticals.out
    :return: Dict {Scaffold: [Pos, LG]}
    
    #java -cp LEP_map3/bin/ ParentCall2 vcfFile=father_hetHom_filtered.vcf data=ped_t.txt removeNonInformative=1 > father_hetHom_round2_parentCall2.out
    '''
    fh1 = open(ParentCall_path, 'r')
    fh2 = open(SepIden_path, 'r')
    template_dict = {}

    fh1.readline()
    fh1.readline()
    fh1.readline()
    fh1.readline()
    fh1.readline()
    fh1.readline()
    fh1.readline()
    fh2.readline()

    while True:
        l1 = fh1.readline()
        if not l1:
            break
        l2 = fh2.readline()

        l1 = l1.strip('\n')
        l1 = l1.split('\t')
        l2 = l2.strip('\n')

        if l1[0] in scaffolds_list:
            if l1[0] not in template_dict:
                template_dict[l1[0]] = [[l1[1], l2]]
            elif l1[0] in template_dict and l1[1] not in template_dict:
                template_dict[l1[0]].append([l1[1], l2])
            else:
                print 'This item already exists in the dictionary. Something is wrong.'
        else:
            pass
    print 'Temp dict created. It contains ', len(template_dict), 'scaffolds'
    return template_dict




def filter_lowQuant_snp(template_dict):
    '''
    Iterates through a dictionary determining how many markers are on each scaffold and what LGs they belong to. It 
    totals the number of markers for each LG and determines the percentage of the scaffold's markers it makes up. If 
    the percentage is lower than the given threshold (1% currently) those markers are excluded from the out put.
    :param template_dict: 
    :return: dictionary of markers to keep in the output vcf
    '''
    keeper_dict = {}
    lg_dict = {}
    for scaffold in template_dict:
        for pos in template_dict[scaffold]:  # This loops through and stores how often a LG occurs on a scaffold
            if pos[1] not in lg_dict:
                lg_dict[pos[1]] = 1
            elif pos[1] in lg_dict:
                lg_dict[pos[1]] += 1

        total = total_func(lg_dict)
        lg_removal_list = []

        for item in lg_dict: # determines if a lg makes up more than 5% of a scaffolds
            #print float(lg_dict[item]), '/', total, '=',  float(lg_dict[item])/float(total)
            if float(lg_dict[item])/float(total) <= 0.02:
                #remove from dataset
                lg_removal_list.append(item)  # if <5% add to list
            else:
                pass
        #print lg_removal_list, len(lg_removal_list)
        for pos1 in template_dict[scaffold]:  #
            #print pos1
            if pos1[1] in lg_removal_list:
                pass
            else:
                if scaffold not in keeper_dict:
                    keeper_dict[scaffold] = [pos1[0]]
                elif scaffold in keeper_dict:
                    keeper_dict[scaffold].append(pos1[0])

    print 'Keeper dict created. It contains:', len(keeper_dict)
    return keeper_dict



def total_func(lg_dict):
    '''
    This function takes a dictionary {LG:#ofoccurances} and calculates the total number of markers on a scaffold
    :param lg_dict: {LG:#ofoccurances}
    :return: total number of markers on a scaffold
    '''
    total = 0
    for lg in lg_dict:
        total += lg_dict[lg]
    print 'The total number of markers: ', total
    return total


def rewrite_gvcf(gvcf_path, keeper_dict, out_path):
    fh1 = open(gvcf_path, 'r')
    fh2 = open(out_path, 'w')

    for line in fh1:
        if line[0] == '#':
            pass
        else:
            line1 = line.strip('\n')
            line1 = line1.split('\t')
            if line1[0] in keeper_dict and line1[1] in keeper_dict[line1[0]]:
                fh2.write(line)
                print '1^'
            else:
                print 'NOPE'



temp_dict = load_vcf('/Volumes/projects/tfording/marmorata/bin/father_hetHom_round2_parentCall2.out', '/Volumes/projects/tfording/marmorata/bin/father_hetHom_round2_SepIden.out')
keeper_dict = filter_lowQuant_snp(temp_dict)
rewrite_gvcf('/Volumes/projects/tfording/marmorata/bin/father_hetHom_filtered_1perc_round2.vcf', keeper_dict, '/Volumes/projects/tfording/marmorata/bin/father_hetHom_filtered_1perc_round3.vcf')





