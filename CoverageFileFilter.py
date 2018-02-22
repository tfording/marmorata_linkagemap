#author=Tyler Fording

from __future__ import division


def filter(vcf_path, output, Dict_list, propPair, mapQ):
    fh_in = open(vcf_path, 'r')
    fh_out = open(output, 'w')
    for line in fh_in:
        check_array = []
        # print len(check_array)
        if line[0] == "#":
            pass
            # fh_out.write(line)
        else:
            line1 = line.strip('\n')
            line1 = line1.split()
            chrpos = str(line1[0]) + ' ' + str(line1[1])

            for dict in Dict_list:
                if chrpos in dict:
                    for item in dict[chrpos]:
                        if float(item[0][9:]) != 0.0 and float(item[7][9:]) != 0.0:
                            coverage = float(item[0][9:])
                            mapQ = float(item[7][9:])
                            properPairs = float(item[8][14:])
                            mapQPerc = float(mapQ / coverage)
                            propPairsPerc = float(properPairs / coverage)
                            print chrpos, propPairsPerc, mapQPerc
                            if propPairsPerc >= float(propPair) and mapQPerc >= float(mapQ):
                                check_array.append(1)
                                print len(check_array)
                            else:
                                pass
        print(len(check_array))
        if len(check_array) == 9:
            print chrpos, 'Passed filter'
            fh_out.write(line)


#filter('/n/projects/tfording/marmorata/data/COVERAGE_FILTERED/snps_haplotypeCaller_hardFiltered_nullsRemoved.vcf', 'test.vcf', Dict_list)


#filter('/Volumes/projects/tfording/marmorata/data/COVERAGE_FILTERED/snps_haplotypeCaller_hardFiltered_nullsRemoved.vcf', 'test.vcf', Dict_list)


