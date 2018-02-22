#author: Tyler Fording
import argparse


adapter_id_dict = {'CGATGT':'17115', 'TGACCA':'17118', 'ACAGTG':'21321', 'ACTTGA':'22151', 'ATCACG':'21545', 'CAGATC':'21323', 'CTTGTA':'21544', 'GCCAAT':'21322', 'TTAGGC':'21546'}

makeped_dict = {}
variant_position_dict = {}
scaffolds_list = []
gcount = 1

def pull_meta(fileloc):
    '''
    This function creates a dictionary of meta data from an input file
    :param fileloc: location to a file with metadata
    :return: dictionary of meta data
    '''
    fh = open(fileloc, "r")
    meta_list = []
    for line in fh:
        line = line.strip('\r')
        line = line.strip('\n')
        temp = line.split(',')
        #print temp[1], line
        meta_list.append([temp[1], line])
    return meta_list


def parse_vcf_list(vcflist, meta_list):
    '''
    This function parses a list of vcf files and sends the files to create_makeped()
    :param vcflist: txt file that contains a list of vcf locations
    :return: None
    '''
    global out_fh
    out_fh = open("out_put.linkage", 'w')
    fh = open(vcflist, 'r')
    for line in fh:
        if line[-1] == '\n':
            position_index(line[0:-1])
        else:
            position_index(line)
    #print(variant_position_dict)
    fh.close()
    fh = open(vcflist, 'r')
    counter = 1
    for line in fh:
        print "File " + str(counter) + ' in vcflist sent to create_makeped'
        line1 = line.split('/')
        line1 = line1[-1]
        adapter = line1[0:6]
        if line[-1] == '\n':
            create_makeped(line[0:-1], meta_list, adapter)
        else:
            create_makeped(line, meta_list, adapter)
        counter += 1


def position_index(vcfloc):
    '''
    This function iterates through a vcf file and creates a dictionary of variance positions
    :param vcfloc: Location of file to
    :return:
    '''
    fh = open(vcfloc, "r")
    counter = 0
    for line in fh:
        counter += 1
        if counter % 10000 == 0:
            print "Line " + str(counter) + ' passed'
        elif line[0] == '#':
            pass
        else:
            line = line.split('\t')
            if line[0] in variant_position_dict and line[1] in variant_position_dict[line[0]]:
                continue
            elif line[0] in variant_position_dict:
                variant_position_dict[line[0]].append(line[1])
            else:
                variant_position_dict[line[0]] = [line[1]]
                scaffolds_list.append(line[0])
    fh.close()
    variant_count = 0
    for key in variant_position_dict:
        variant_count += len(variant_position_dict[key])
        #print key, len(variant_position_dict[key])
    print "TOTAL NUMBER OF VARIANTS: "+str(variant_count)  # 9147 for 10k data set (all 9 individauls)


def create_makeped(vcfloc, meta_list, adapter):  # MAIN Pay-Load Function
    '''
    This is the main function in this program. This function passes data to 4 other functions in the program.
    See in-line comments for more detail.
    :param vcfloc: PATH to vcf file
    :param meta_list: PATH to meta.csv
    :param adapter: adapter seq, passed to output_makeped()
    :return: n/a
    '''
    for item in scaffolds_list:  # This loop creates a list of ordered positions for a scaffold and then sends it to other functions
        scaffold = item  # holds scaffold name
        all_position_list = variant_position_dict[item]  # This stores all possible positions on the scaffold
        all_position_list = [int(x) for x in all_position_list]  # converts everything in the list to an int so it can be sorted
        all_position_list.sort()  # Sorts the list
        all_position_list = [str(x) for x in all_position_list]  # converts all the items in the list back to strings for ease of use

        current_positions = current_scaffold_pos_list(vcfloc, scaffold)  # this portion creates a list of positions on the current scaffold
        current_positions = [int(x) for x in current_positions]  # converts everything in the list to an int so it can be sorted
        current_positions.sort()  # Sorts the list
        current_positions = [str(x) for x in current_positions]  # converts all the items in the list back to strings for ease of use

        if current_positions == all_position_list:  # If the current individual has all possible variant positions
            genotype_list = ez_scaffold_geneotype_list(vcfloc, scaffold)
            makeped_dict[scaffold] = genotype_list

        elif current_positions != all_position_list:
            new_current_pos = hard_scaffold_genotype_list(vcfloc, all_position_list, current_positions, scaffold)
            makeped_dict[scaffold] = new_current_pos

    output_makeped(makeped_dict, scaffolds_list, meta_list, adapter)


def current_scaffold_pos_list(vcfloc, scaffold_name):
    '''
    This function takes a vcf file and a scaffold name creates a list of variant positions on that scaffold
    :param vcfloc: PATH to vcf file
    :param scaffold_name: name of current scaffold being looked at
    :return: List of variant positions on scaffold_name
    '''
    current_positions = []
    fh = open(vcfloc, 'r')
    for line in fh:  # This loop creates a list of positions associated with the current scaffold
        line = line.split("\t")
        if line[0] == '#':
            pass
        elif line[0] == scaffold_name:
            current_positions.append(line[1])
    return current_positions


def ez_scaffold_geneotype_list(vcfloc, scaffold_name):
    '''
    This function will take a scaffold name and pull all genotypes associated with varaince on that scaffold. This is
    the simple case in which all positions are the same, so order will be taken as in the vcf file.
    :param vcfloc: PATH to vcf file
    :param scaffold_name: name of current scaffold
    :return: List of genotypes on a scaffold
    '''
    fh = open(vcfloc, 'r')
    genotypes_list = []

    for line in fh:
        if line[0] == '#':
            pass
        else:
            line = line.split('\t')
            if line[0] == scaffold_name:
                working_line = line[9]
                working_line = working_line[0:3]
                working_line = working_line[0]+' '+working_line[2]
                genotypes_list.append(working_line)
    return genotypes_list


def hard_scaffold_genotype_list(vcfloc, all_position_list, current_positions, scaffold_name):
    '''
    This function takes two position lists with different numbers of positions in them and returns a list with the
    length discrepancies filled with calls homozygous to the reference.
    :param vcfloc: PATH to vcf
    :param all_position_list: List of all positions being looked at
    :param current_positions: List of all variant positions on current scaffold
    :param scaffold_name: name of the scaffold being looked at
    :return: A list of all genotype calls
    '''
    fh = open(vcfloc, 'r')
    vcf_position_genotype_list = []
    genotypes_list = []
    counter = 0

    for line in fh:  # this loop stores all relevant positions and genotypes
        if line[0] == '#':
            pass
        else:
            line = line.split('\t')
            if line[0] == scaffold_name:
                gt = line[9]
                gt = gt[0:3]
                gt = gt[0]+' '+gt[2]
                vcf_position_genotype_list.append([line[1], gt])
        # print vcf_position_genotype_list

    for item in current_positions:
        if item != all_position_list[counter]:
            genotypes_list.append('0 0')
            counter += 1
        elif item == all_position_list[counter]:  # simple case, in which the position in the individual matches the master list
            for thing in vcf_position_genotype_list:
                if thing[0] == item:
                    genotypes_list.append(thing[1])
            counter += 1
    return genotypes_list


def output_makeped(makeped_dict, scaffolds_list, meta_list, adapter):
    '''
    This function will write a dictionary of scaffolds and genotype calls to an output file, then move the cursor to the
    next line, so the subsequent individual's genotypes can be written. After the line is written to a new file, the
    dictionary is then erased to be used in the next iteration.
    :param makeped_dict: Dictionary of scaffolds and variant genotypes on that scaffold
    :param scaffolds_list: List of scaffolds (used for consistent ordering)
    :param meta_list: PATH to meta txt
    :param adapter: adapter associated with individual ID
    :return: 
    '''
    if adapter in adapter_id_dict:
        id = adapter_id_dict[adapter]
    else:
        print "Adapter not found in ID dictionary"

    meta_data = pull_meta(meta_list)
    print meta_data

    for line in meta_data:
        if line[0] == id:
            temp = line[1]
            temp = temp.split(',')

            for i in temp:
                out_fh.write(i)
                out_fh.write('\t')

            for item in scaffolds_list:
                if item in makeped_dict:
                    for genotype in makeped_dict[item]:
                        out_fh.write(genotype)
                        out_fh.write('\t')
    out_fh.write('\n')




if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="VCF to pre-makeped")
    parser.add_argument("vcf_list", type=str, help="Enter file path to a txt file containing a list of vcf files", nargs='?')
    parser.add_argument("meta_list", type=str, help="Enter file path to a txt file containing a list of tsv metadata", nargs='?')
    #parser.add_argument("out_put", type=str, help="Enter file name for output", nargs='?')
    args = parser.parse_args()

parse_vcf_list(args.vcf_list, args.meta_list)






