#author=Tyler Fording

import argparse


def main(vcf_filepath, out_filepath):
    '''
    This function takes a vcf file, iterates through each line checking for null calls. If a null call is found,
    it skips the line, if the line doesn't have a null call it prints it to a new file.
    :param vcf_filepath: PATH to vcf
    :param out_filepath: PATH to output file
    :return:
    '''
    fh = open(vcf_filepath, 'r')
    fh_out = open(out_filepath, 'w')
    counter = 0
    for line in fh:
        counter += 1
        if counter % 100000 == 0:
            print counter
        if line[0] == '#':
            fh_out.write(line)
        else:
            working_line = line.split('\t')
            line2print = working_line[:-9]
            for item in working_line[-9:]:
                if item[0:3] == './.':
                    break
                else:
                    line2print.append(item)
                    if item[-1] == '\n':
                        readyline = ''
                        for item in line2print:
                            if len(readyline) == 0:
                                readyline = readyline + str(item)
                            else:
                                readyline = readyline + '\t' + str(item)
                        fh_out.write(readyline)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Clean VCF")
    parser.add_argument("vcf_filepath", type=str, help="Enter file path to a txt file containing a list of vcf files", nargs='?')
    parser.add_argument("out_filepath", type=str, help="Enter file path for output file", nargs='?')
    #parser.add_argument("out_put", type=str, help="Enter file name for output", nargs='?')
    args = parser.parse_args()

main(args.vcf_filepath, args.out_filepath)