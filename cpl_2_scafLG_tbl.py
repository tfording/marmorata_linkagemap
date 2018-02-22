#author=Tyler Fording




def import_cpl(cpl_path):  # import data function
    '''
    imports and stores cpl file into a dictionary
    :param cpl_path: path to cpl file
    :return: dictionary
    '''
    fh_in = open(cpl_path, 'r')

    scaff_LG_dict = {}

    for line in fh_in:
        line = line.strip('\n')
        line = line.split('\t')

        if line[0] in scaff_LG_dict:
            if int(line[2]) in scaff_LG_dict[line[0]] or int(line[2] == 0):
                pass
            else:
                scaff_LG_dict[line[0]].append(int(line[2]))
        else:
            scaff_LG_dict[line[0]] = [int(line[2])]

    #print scaff_LG_dict
    fh_in.close()
    return scaff_LG_dict


def scaffold_lg_tbl(cpl_path, out_path1, out_path2):  # Table 1 + wrapper
    '''
    This function takes in a cpl (chromosome, position, linkage group) file and returns two tables in tsv format.
    The first table (out_path1) is in the format (scaffold \t lg1 \t lg2..)
    The second table (out_path2) is in the opposite format (LG \t scaffold1 \t scaffold2...)
    :param cpl_path: path to cpl file
    :param out_path1: output path for tbl 1
    :param out_path2: output path for tbl 2
    :return: dictionary to be used for tbl 2
    '''
    working_dict = import_cpl(cpl_path)
    fh_out = open(out_path1, 'w')

    #header line
    fh_out.write('#Scaffold'+'\t'+'LG1'+'\t'+'LG2'+'\t'+'LG3'+'\t'+'...'+'\n')

    for item in working_dict:  # this loop prints the scaffolds and the LGs they're associated with.
        if len(working_dict[item]) == 1:
            if working_dict[item] == [0]:
                pass
            else:
                continue
        else:
            current_list = working_dict[item]
            current_list = sorted(current_list)
            fh_out.write(item+'\t')
            for lg in current_list:
                fh_out.write(str(lg)+'\t')
            fh_out.write('\n')
    fh_out.close()
    lg_scaffold_tbl(working_dict, out_path2)

def lg_scaffold_tbl(scaffold_lg_dict, out_path2):  # table 2
    working_dict = {}
    fh_out = open(out_path2, 'w')
    fh_out.write('#LG #'+'\t'+'Scaffold1'+'\t'+'Scaffold2'+'\t'+'Scaffold3'+'\t'+'...'+'\n')
    ### TEMP LINES FOR TESTING########################################
    #scaffold_lg_dict = import_cpl(cpl_path)

    ##################################################################
    ############## This loop inverts the dictionary ##################

    for key in scaffold_lg_dict:
        for value in scaffold_lg_dict[key]:
            if value in working_dict:
                if key in working_dict[value]:
                    pass
                else:
                    working_dict[value].append(key)
            else:
                working_dict[value] = [key]
    #################################################################
    ########### This loop writes the new dict to tsv ################

    for key in working_dict:
        if key != 0:
            fh_out.write(str(key)+'\t')
            for value in working_dict[key]:
                fh_out.write(value+'\t')
            fh_out.write('\n')


scaffold_lg_tbl('/Volumes/projects/tfording/marmorata/bin/R13_cpl.out', '/Volumes/projects/tfording/marmorata/bin/scaffold_LG_R13.tsv', '/Volumes/projects/tfording/marmorata/bin/LG_scaffold_R13.tsv')