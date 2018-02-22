#author=Tyler Fording


import argparse


def main(LG_list, out_file):
    '''
    This function takes a tsv(CHR POS LG) and removes all markers that were not assigned to a linkage group
    :param LG_list: TSV PATH
    :param out_file: name of output file
    :return: none
    '''
    fh = open(LG_list, 'r')
    fh_out = open(out_file, 'w')
    for line in fh:
        check = line.strip('\r')
        check = check.strip('\n')
        check = check.split('\t')
        #print check
        if check[2] == '0':
            pass
        else:
            to_print = check[0] + '\t' + check[1] + '\t' + check[2] + '\n'
            fh_out.write(to_print)




if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Removes singles from cpL")
    parser.add_argument("LG_list", type=str, help="Enter file path to a LG file", nargs='?')
    #parser.add_argument("ped_path", type=str, help="Enter file path to the ped to be parsed", nargs='?')
    parser.add_argument("out_file", type=str, help="Enter file name for output", nargs='?')
    args = parser.parse_args()


main(args.LG_list, args.out_file)