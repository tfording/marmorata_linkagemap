#author=Tyler Fording

import argparse


def main(LG_file, ped_path, out_path):
    '''
    This function takes a pedigree, a LinkageGroup file and an output name. It sends the LG file to read_LG_assignments
    then iterates through the pedigree, creating a new file with 'scaffold \t position \t LG'
    :param LG_file: PATH to LG file
    :param ped_path: PATH to pedigree file (ParentCall2 Output file)
    :param out_path: PATH and name for output file
    :return: none
    '''
    LG_list = read_LG_assignments(LG_file)

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
    ped_out.close()
    ped_in.close()


def read_LG_assignments(LG_file):
    '''
    This function reads in a output from LEPmap3's SeparateIdenticals and stores all the LG values into a list. The
     list is returned.
    :param LG_file: PATH to LinkageGroup file
    :return: list
    '''
    LG_list = []
    fh = open(LG_file, 'r')
    for line in fh:
        if line[0] == '#':
            pass
        else:
            line = line.strip('\r')
            line = line.strip('\n')
            if len(line) >= 3:
                print 'ERROR: Unexpected LG value', line
                break
            else:
                LG_list.append(line)
    #print len(LG_list)
    fh.close()
    return LG_list


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="VCF to pre-makeped")
    parser.add_argument("LG_file", type=str, help="Enter file path to a LG file", nargs='?')
    parser.add_argument("ped_path", type=str, help="Enter file path to the ped to be parsed", nargs='?')
    parser.add_argument("out_path", type=str, help="Enter file name for output", nargs='?')
    args = parser.parse_args()


main(args.LG_file, args.ped_path, args.out_path)























