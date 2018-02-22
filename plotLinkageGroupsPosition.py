
import matplotlib.pyplot as plt
import seaborn

chromLenList = [['Scpiz6a_49', 85027298], ['Scpiz6a_55.1', 77407970], ['Scpiz6a_26', 75278123], ['Scpiz6a_73', 74911545], ['Scpiz6a_37', 69231668], ['Scpiz6a_28', 67865306], ['Scpiz6a_146', 60930128], ['Scpiz6a_30.1', 51341299], ['Scpiz6a_65', 49352604], ['Scpiz6a_27', 43800890], ['Scpiz6a_72', 42780895], ['Scpiz6a_11.1', 42073645], ['Scpiz6a_1', 38404124], ['Scpiz6a_43', 37802860], ['Scpiz6a_17.2', 32220929], ['Scpiz6a_120', 32121594], ['Scpiz6a_74', 32018458], ['Scpiz6a_147', 28108939], ['Scpiz6a_118', 27130724], ['Scpiz6a_122', 26623134], ['Scpiz6a_45', 26422714], ['Scpiz6a_47', 25451955], ['Scpiz6a_44', 25365721], ['Scpiz6a_29', 24966792], ['Scpiz6a_44.1', 24597102], ['Scpiz6a_86', 24594407], ['Scpiz6a_75', 23201744], ['Scpiz6a_148', 22570672], ['Scpiz6a_113', 20260096], ['Scpiz6a_173', 19551695], ['Scpiz6a_11', 18755222], ['Scpiz6a_117', 16663636], ['Scpiz6a_39', 15903008], ['Scpiz6a_170.1', 15414158], ['Scpiz6a_32.1', 15074303], ['Scpiz6a_253', 14342376], ['Scpiz6a_90', 14219928], ['Scpiz6a_201', 13494561], ['Scpiz6a_66', 12898218], ['Scpiz6a_115', 12824703], ['Scpiz6a_23', 12282005], ['Scpiz6a_22', 11838671], ['Scpiz6a_696', 11702065], ['Scpiz6a_30', 10722422], ['Scpiz6a_232', 10671227], ['Scpiz6a_18.1', 9776040], ['Scpiz6a_378', 9339577], ['Scpiz6a_593', 8611425], ['Scpiz6a_423', 8340160], ['Scpiz6a_150', 7979424], ['Scpiz6a_34', 7947102], ['Scpiz6a_264', 7851285], ['Scpiz6a_55', 7784176], ['Scpiz6a_81.1', 7447263], ['Scpiz6a_263', 6940994], ['Scpiz6a_119', 6732129], ['Scpiz6a_1453', 6154658], ['Scpiz6a_136.1', 4894235], ['Scpiz6a_60', 4656254], ['Scpiz6a_32', 4632030], ['Scpiz6a_17', 3725668], ['Scpiz6a_19', 3503723], ['Scpiz6a_115.1', 3477553], ['Scpiz6a_782', 3439947], ['Scpiz6a_382', 3278768], ['Scpiz6a_16', 2929255], ['Scpiz6a_152.1', 2823190], ['Scpiz6a_136', 2726834], ['Scpiz6a_55.2', 2689334], ['Scpiz6a_87', 2686163], ['Scpiz6a_745', 2447111], ['Scpiz6a_393', 2360768], ['Scpiz6a_462', 2313997], ['Scpiz6a_391.1', 2211095], ['Scpiz6a_23.1', 2086365], ['Scpiz6a_99', 2025120], ['Scpiz6a_102', 1880828], ['Scpiz6a_105', 1873381], ['Scpiz6a_565', 1843408], ['Scpiz6a_434', 1729324], ['Scpiz6a_1005', 1723421], ['Scpiz6a_970', 1685018], ['Scpiz6a_2672', 1677683], ['Scpiz6a_1376', 1656332], ['Scpiz6a_68', 1654872], ['Scpiz6a_185', 1540780], ['Scpiz6a_8', 1484258], ['Scpiz6a_393.1', 1382077], ['Scpiz6a_3382', 1174852], ['Scpiz6a_423.1', 1139734], ['Scpiz6a_269', 979664], ['Scpiz6a_31', 855192], ['Scpiz6a_458', 839327], ['Scpiz6a_126.1', 791743], ['Scpiz6a_338', 790808], ['Scpiz6a_642', 750404], ['Scpiz6a_1476', 665959], ['Scpiz6a_126', 658703], ['Scpiz6a_597', 561906], ['Scpiz6a_1590', 519127], ['Scpiz6a_447', 484501], ['Scpiz6a_746', 479959], ['Scpiz6a_177', 471552], ['Scpiz6a_368', 427953], ['Scpiz6a_289', 425324], ['Scpiz6a_52', 419112], ['Scpiz6a_53.1', 404948], ['Scpiz6a_291', 376675], ['Scpiz6a_391', 371359], ['Scpiz6a_328', 370512], ['Scpiz6a_3673', 349917], ['Scpiz6a_401', 296338], ['Scpiz6a_295', 295078], ['Scpiz6a_85.1', 251664], ['Scpiz6a_1276', 251648], ['Scpiz6a_53', 240630], ['Scpiz6a_435', 234711], ['Scpiz6a_85', 228626], ['Scpiz6a_666', 225051], ['Scpiz6a_1742', 220549], ['Scpiz6a_5', 194631], ['Scpiz6a_808', 183855], ['Scpiz6a_1511', 172252], ['Scpiz6a_746.1', 169521], ['Scpiz6a_2423', 160299], ['Scpiz6a_435.1', 159679], ['Scpiz6a_960', 156083], ['Scpiz6a_7', 154896], ['Scpiz6a_1185', 142693], ['Scpiz6a_627', 117264], ['Scpiz6a_5.1', 105534], ['Scpiz6a_255', 104322], ['Scpiz6a_231', 103231], ['Scpiz6a_21', 96978], ['Scpiz6a_408', 94806], ['Scpiz6a_610', 86730], ['Scpiz6a_396', 80031], ['Scpiz6a_656', 78199], ['Scpiz6a_177.1', 76378], ['Scpiz6a_132', 74619], ['Scpiz6a_415', 73457], ['Scpiz6a_428', 71177], ['Scpiz6a_455', 71053], ['Scpiz6a_2379', 68125], ['Scpiz6a_1473', 63143], ['Scpiz6a_964', 61868], ['Scpiz6a_428.1', 60368], ['Scpiz6a_10', 53321], ['Scpiz6a_1049', 52688], ['Scpiz6a_1172', 51249], ['Scpiz6a_3445', 50902], ['Scpiz6a_442', 49450], ['Scpiz6a_1520', 45059], ['Scpiz6a_2465', 40349], ['Scpiz6a_383', 39906], ['Scpiz6a_141', 39436], ['Scpiz6a_1123', 36794], ['Scpiz6a_1204', 35494], ['Scpiz6a_339', 34868], ['Scpiz6a_18', 34568], ['Scpiz6a_707', 32198], ['Scpiz6a_1255', 32139], ['Scpiz6a_1801', 32128], ['Scpiz6a_667', 31316], ['Scpiz6a_781', 29042], ['Scpiz6a_132.1', 28177], ['Scpiz6a_1492', 26991], ['Scpiz6a_2065', 26498], ['Scpiz6a_1122', 25953], ['Scpiz6a_1863', 24922], ['Scpiz6a_2735', 24482], ['Scpiz6a_121', 24242], ['Scpiz6a_400', 24016], ['Scpiz6a_1036', 23857], ['Scpiz6a_1583', 23731], ['Scpiz6a_318', 23618], ['Scpiz6a_927', 23259], ['Scpiz6a_3236', 21926], ['Scpiz6a_60.1', 20957], ['Scpiz6a_2597', 20367], ['Scpiz6a_579', 20308], ['Scpiz6a_17.1', 20024], ['Scpiz6a_840', 19473], ['Scpiz6a_989', 19426], ['Scpiz6a_765', 19296], ['Scpiz6a_859', 18304], ['Scpiz6a_2124', 18063], ['Scpiz6a_894', 17909], ['Scpiz6a_700', 16916], ['Scpiz6a_1314', 16868], ['Scpiz6a_760', 16777], ['Scpiz6a_2089', 16710], ['Scpiz6a_163', 16461], ['Scpiz6a_2886', 16388], ['Scpiz6a_758', 16089], ['Scpiz6a_2136', 15918], ['Scpiz6a_1085', 15811], ['Scpiz6a_2425', 15688], ['Scpiz6a_875', 15364], ['Scpiz6a_1315', 14984], ['Scpiz6a_804', 13912], ['Scpiz6a_1226', 13732], ['Scpiz6a_589', 13667], ['Scpiz6a_1557', 13590], ['Scpiz6a_1436', 13138], ['Scpiz6a_951', 12998], ['Scpiz6a_202', 12824], ['Scpiz6a_2536', 12743], ['Scpiz6a_456', 12376], ['Scpiz6a_1298', 12204], ['Scpiz6a_218', 12128], ['Scpiz6a_1592', 12017], ['Scpiz6a_449', 11998], ['Scpiz6a_2349', 11680], ['Scpiz6a_1840', 11457], ['Scpiz6a_3432', 11405], ['Scpiz6a_2483', 11366], ['Scpiz6a_1391', 10901], ['Scpiz6a_943', 10757], ['Scpiz6a_548', 10576], ['Scpiz6a_1278', 10540], ['Scpiz6a_2365', 10445], ['Scpiz6a_2025', 10129]]



### Plot linkage groups from the two files used by lepmap. The original LOD file with the snps in order. The output file with the linkage group each marker belongs to in the same order as the LOD file ###
def plotLinkageGroupsPositions(lodFile, linkageGroupFile, chromNumberStart, chromNumberStop, chromLengthList,
                               linkageNumber):
    lodFile = open(lodFile, 'r')
    linkageGroupFile = open(linkageGroupFile, 'r')

    ### Read the header Lines from these two files ###
    lodFile.readline()
    lodFile.readline()
    lodFile.readline()
    lodFile.readline()
    lodFile.readline()
    lodFile.readline()
    lodFile.readline()
    linkageGroupFile.readline()
    ### Read our snps into memory. {chrom:[[plottingInformation],...]}
    plotDict = {}
    counter = 1
    while True:
        counter += 1
        lodLine = lodFile.readline()
        if counter % 1000000 == 0:
            print counter
        if not lodLine:
            break
        lodLine = lodLine.strip('\r')
        lodLine = lodLine.strip('\n')
        linkageLine = linkageGroupFile.readline()
        linkageLine = linkageLine.strip('\r')
        linkageLine = linkageLine.strip('\n')

        lodCols = lodLine.split('\t')
        chrom = lodCols[0]
        pos = int(lodCols[1])

        if chrom not in plotDict:
            plotDict.update({chrom: [[pos, int(linkageLine)]]})
        else:
            plotDict[chrom].append([pos, int(linkageLine)])
    ###################################################################
    # print "info read into mem"
    ### Plotting the linkageGroup marker distributions across chromNumber of scaffolds (largest to smallest)
    ### This is to get the acutal color palette ###
    palMan = seaborn.color_palette("hls", linkageNumber)
    figMan = plt.figure()
    figMan.set_size_inches(16, 16)
    axMan = plt.subplot2grid((1, 2), (0, 0), colspan=2)
    axMan.grid("off")
    seaborn.set_style("white")
    yTicks = []
    yLabs = []
    chromNumber = chromNumberStop - chromNumberStart
    for chrom in chromLengthList[chromNumberStart:chromNumberStop]:
        if chrom[0] in plotDict:
            print chrom[0]
            chromNumber -= 1
            # print len(plotDict[chrom[0]])
            for plotVals in plotDict[chrom[0]]:
                if plotVals[1] != 0:
                    axMan.bar(int(plotVals[0] / 1000), 1, 1, chromNumber, color=palMan[plotVals[1]], linewidth=0)
            axMan.plot([0, chrom[1] / 1000], [chromNumber, chromNumber], color="Black")
            yTicks.append(chromNumber + .5)
            yLabs.append(chrom[0])
    axMan.set_xlabel("Scaffold Position")
    axMan.set_yticklabels(yLabs)
    axMan.set_yticks(yTicks)
    ########################################################################################################
    ##plt.show(figMan)
    figMan.savefig('/Volumes/projects/tfording/marmorata/figures/father_R2_LGbyPos.png')

plotLinkageGroupsPositions('/Volumes/projects/tfording/marmorata/bin/100MapQpPairs/father_mapQ100_propPair100_R2_parentCall2.out', \
                            '/Volumes/projects/tfording/marmorata/bin/100MapQpPairs/father_mapQ100_propPair100_R2_SepIden.out', 0, 20, \
                               chromLenList,51)

