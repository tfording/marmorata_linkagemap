#author = Tyler Fording
import argparse


def cat_and_cut_main(list, lines_to_cut):
    '''
    This function takes a list of files and a integer number of lines to keep from each file. It will cat that make
    lines and write them to a new file (cut.file)
    :param list: PATH to .txt list of files
    :param lines_to_cut: (int) number of lines to keep from each file
    :return:
    '''
    fh = open(list, 'r')
    gcount = 0
    for file in fh:
        file1 = file.split('/')
        file2 = file1[-1]
        pre_out = '.cut'
        out_handle = file2[0:-1]+pre_out
        fh_out = open(out_handle, 'w')
        counter = 0
        print(out_handle)
        if counter >= int(lines_to_cut):
            break
        else:
            fh2 = open(file[0:-1], 'r')
            for line in fh2:
                if counter >= int(lines_to_cut):
                    break
                else:
                    #print(counter)
                    fh_out.write(line)
                    counter += 1
        gcount += 1
        fh_out.close()
        fh2.close()
    fh.close()



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="VCF to pre-makeped")
    parser.add_argument("list", type=str, help="Enter file path to a txt file containing a list of vcf files", nargs='?')
    parser.add_argument("lines_to_cut", type=str, help="Enter number of lines to keep from each file", nargs='?')
    args = parser.parse_args()

cat_and_cut_main(args.list, args.lines_to_cut)
