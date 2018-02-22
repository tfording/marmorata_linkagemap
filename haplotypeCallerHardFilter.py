#author=Tyler Fording

def vcfHardFilter(vcf_path):
    '''
    This fucntion iterates through a vcf file and looks at the 6th column. If the column indicates a pass or '.'
    the line is kept, otherwise the line is not written to the new filtered file.
    :param vcf_path: PATH to vcf
    :return: Outputs filtered vcf
    '''
    fh_in = open(vcf_path, 'r')
    fh_out = open('snps_haplotypeCaller_hardFiltered.vcf', 'w')

    for line in fh_in:
        if line[0] == "#":
            fh_out.write(line)
        else:
            line1 = line.strip('\n')
            line1 = line1.split()
            print line1[6]
            if line1[6] == 'PASS' or line1[6] == '.':
                fh_out.write(line)

#vcfHardFilter('/n/projects/tfording/marmorata/data/COVERAGE_FILTERED/snps_haplotypeCallerVariants_hardFilterTAGGED.vcf')















































