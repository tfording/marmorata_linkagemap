#author=Tyler Fording


def import_parentcall(PC2_path):
    '''
    This function loads the scaffold and position from a ParentCall2 output file into a dictionary and returns it. 
    :param PC2_path: PATH to ParentCall2 output file
    :return: Dictionary of scaffolds (key) and positions (values)
    '''
    fh = open(PC2_path, 'r')
    parentcall_dict = {}
    for line in fh:
        if line[0] == '#' or line[0:3] == 'CHR':
            pass
        else:
            line = line.strip('\n')
            line = line.split('\t')
            if line[0] not in parentcall_dict:
                parentcall_dict[line[0]] = [line[1]]
            elif line[0] in parentcall_dict and line[1] not in parentcall_dict[line[0]]:
                parentcall_dict[line[0]].append(line[1])
            else:
                print line[:2], 'This SNP is already in the dictionary. SOMETHING IS WRONG.'
    return parentcall_dict


def import_vcf(vcf_path, parentcall_dict, pathtowrite):
    '''
    This function writes a vcf made of all the positions in the ParentCall2 output.
    :param vcf_path: PATH to vcf
    :param parentcall_dict: Dictionary generated with import_parentcall
    :param pathtowrite: PATH to output file
    :return: No return. Writes a vcf file.
    '''
    counter = 0
    fh = open(vcf_path, 'r')
    fh_out = open(pathtowrite, 'w')
    for line in fh:
        if line[0] == '#':
            fh_out.write(line)
        else:
            if counter % 100000 == 0:
                print counter
            line1 = line.strip('\n')
            line1 = line.split('\t')
            counter += 1
            if line1[0] in parentcall_dict and line1[1] in parentcall_dict[line1[0]]:
                fh_out.write(line)
            else:
                pass

parentcall_dict = import_parentcall('/Volumes/projects/tfording/marmorata/bin/hetHom/father_hetHomsubset_parentCall2.out')
import_vcf('/Volumes/projects/tfording/marmorata/bin/hetHom/father_hetHom_cleaned.vcf', parentcall_dict, '/Volumes/projects/tfording/marmorata/bin/hetHom/father_hetHom_parentcall_matched.vcf')
