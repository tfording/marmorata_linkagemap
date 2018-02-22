#author=Tyler Fording


'''
Scpiz6a_1021	118     Coverage:8 	    A:5	    C:0	    T:0	    G:3	    N:0	    INDELReads:0
Scpiz6a_1021	343     Coverage:12 	A:8	    C:0	    T:0	    G:4	    N:0	    INDELReads:0
Scpiz6a_1021	703     Coverage:25 	A:0	    C:16    T:9	    G:0	    N:0	    INDELReads:0
Scpiz6a_1021	896     Coverage:34 	A:0	    C:14    T:0	    G:20    N:0	    INDELReads:0
'''


def main(file_list_path):
    fh = open(file_list_path, 'r')
    for line in fh:
        line = line.strip('\n')
        filter_snpsCoverage(line)



def filter_snpsCoverage(snp_cov_path):
    fh_in = open(snp_cov_path, 'r')
    #name = snp_cov_path[]

    for line in fh_in:
        working_line = line.strip('\n')
        working_line = working_line.split('\t')
        total_coverage = int(working_line[2][9:])

        if total_coverage <= 60 and total_coverage >= 8:
            a_coverage = int(working_line[3][2:])
            c_coverage = int(working_line[4][2:])
            t_coverage = int(working_line[5][2:])
            g_coverage = int(working_line[6][2:])
            n_coverage = int(working_line[7][2:])









        else:
            pass











filter_snpsCoverage('/Volumes/projects/tfording/marmorata/data/SNP_COVERAGE/test_data.txt')



















































