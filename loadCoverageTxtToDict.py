#author=Tyler Fording


def load2Dict(file_path):
    fh = open(file_path, 'r')
    coverage_dict = {}
    counter = 0

    for line in fh:
        line1 = line.strip('\n')
        line1 = line.split()
        chrpos = str(line1[0]) + ' ' + str(line1[1])
        if chrpos not in coverage_dict:
            coverage_dict[chrpos] = [line1[2:]]
        else:
            coverage_dict[chrpos].append(line1[2:])
    return coverage_dict

#load2Dict('/Volumes/projects/tfording/marmorata/data/COVERAGE_FILTERED/ACAGTG_snpsCoverage.txt')













































