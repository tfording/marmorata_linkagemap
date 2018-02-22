#author=Tyler Fording

import argparse


def file_parse(PATH):
    '''
    This function iterates through the file creating two lists of numbers (str) from the output file of JoinIdenLGs. 
    It then stores the before and after LG assignment to an array.
    :param PATH: PATH to JoinIdenLG output file
    :return: calls next function.
    '''
    fh = open(PATH, 'r')
    original_LG = []
    new_LG = []

    for line in fh:
        if line[0] == '#':
            pass
        else:
            line = line.strip('\n')
            line = line.split('\t')
            print 'OG LG: ', line[1], 'New LG: ', line[0]
            original_LG.append(line[1])
            new_LG.append(line[0])
    file_stats(original_LG, new_LG)
    return new_LG


def file_stats(original_LG, new_LG):
    num_old = len(set(original_LG))
    print 'There were ', num_old, ' linkage groups before JoinIdenLG was run'
    num_new = len(set(new_LG))
    print 'There were ', num_new, ' linkage groups after JoinIdenLG was run'
    new_lg_set = set(new_LG)
    print 'The number identifiers for the new LG set are', new_lg_set



def main(LG_file, ped_path, out_path):
    '''
    This function takes a pedigree, a LinkageGroup file and an output name. It sends the LG file to read_LG_assignments
    then iterates through the pedigree, creating a new file with 'scaffold \t position \t LG'
    :param LG_file: PATH to LG file
    :param ped_path: PATH to pedigree file (ParentCall2 Output file)
    :param out_path: PATH and name for output file
    :return: none
    '''
    LG_list = file_parse(LG_file)

    ped_in = open(ped_path, 'r')
    ped_out = open(out_path, 'w')
    counter = 0

    for line in ped_in:
        if line[0:3] == 'CHR' or line[0] =='#':
            pass
        else:
            line = line.split('\t')
            # print line[0], line[1], LG_list[counter], counter

            to_print = line[0] +'\t'+ line[1] +'\t'+ str(LG_list[counter]) +'\n'
            ped_out.write(to_print)
            counter += 1


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Clean VCF")
    parser.add_argument("LG_filepath", type=str, help="Enter file path to a txt file containing a list of vcf files", nargs='?')
    parser.add_argument("PED_filepath", type=str, help="Enter file path for output file", nargs='?')
    parser.add_argument("out_path", type=str, help="Enter file name for output", nargs='?')
    args = parser.parse_args()

main(args.LG_filepath, args.PED_filepath, args.out_path)





















