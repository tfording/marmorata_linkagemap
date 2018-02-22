



fh = open('/Volumes/projects/tfording/marmorata/bin/father_10k_hetHom_JoinIdenLG_clean_cpL.out', 'r')
cplDict = {}


for line in fh:
    line = line.strip('\n')
    line = line.split('\t')
    if line[0] in cplDict and line[2] in cplDict[line[0]]:
        pass
    elif line[0] in cplDict and line[2] not in cplDict[line[0]]:
        cplDict[line[0]].append(line[2])
    else:
        cplDict[line[0]] = [line[2]]

for key in cplDict:
    print 'The LG associated with scaffold', key, 'are:',cplDict[key]










