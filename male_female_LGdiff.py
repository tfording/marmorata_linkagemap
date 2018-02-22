#author=Tyler Fording

import argparse






def func2(cpl_PATH1, cpl_PATH2):
    mother_LGDict, mother_ChrDict = loadCPL(cpl_PATH1)
    father_LGDict, father_ChrDict = loadCPL(cpl_PATH2)

    #for Chr in mother_ChrDict:
     #d   print Chr, mother_ChrDict[Chr]

    sharedDict = {}

    for LG in mother_LGDict:
        for Chr in mother_LGDict[LG]:
            if Chr in father_LGDict[LG]:
                pass
            else:
                if LG in sharedDict:
                    sharedDict[LG].append(Chr)
                else:
                    sharedDict[LG] = Chr

    print sharedDict

'''something = {'30': ['Scpiz6a_2552'], '36': ['Scpiz6a_1997'], '28': ['Scpiz6a_1698'], '22': ['Scpiz6a_552'],
             '29': ['Scpiz6a_647'], '60': ['Scpiz6a_2088'], '61': ['Scpiz6a_2423'], '62': ['Scpiz6a_3610'],
             '63': ['Scpiz6a_3447'], '64': ['Scpiz6a_1168'], '53': ['Scpiz6a_696'], '34': ['Scpiz6a_3444'],
             '24': ['Scpiz6a_1761'], '25': ['Scpiz6a_420'], '26': ['Scpiz6a_2296'], '27': ['Scpiz6a_696'],
             '20': ['Scpiz6a_1693'], '21': ['Scpiz6a_1695'], '48': ['Scpiz6a_347'], '49': ['Scpiz6a_3444'],
             '46': ['Scpiz6a_1960'], '47': ['Scpiz6a_2423'], '44': ['Scpiz6a_1762'], '45': ['Scpiz6a_1761'],
             '42': ['Scpiz6a_346'], '43': ['Scpiz6a_1763'], '40': ['Scpiz6a_696'], '41': ['Scpiz6a_391'],
             '1': ['Scpiz6a_1761'], '3': ['Scpiz6a_347'], '2': ['Scpiz6a_1760'], '5': ['Scpiz6a_1764'],
             '4': ['Scpiz6a_696'], '7': ['Scpiz6a_3610'], '6': ['Scpiz6a_1767'], '9': ['Scpiz6a_1697'],
             '8': ['Scpiz6a_696'], '56': ['Scpiz6a_3064'], '13': ['Scpiz6a_1762'], '38': ['Scpiz6a_1768'],
             '15': ['Scpiz6a_735'], '32': ['Scpiz6a_1761'], '14': ['Scpiz6a_1359'], '11': ['Scpiz6a_1761'],
             '10': ['Scpiz6a_1166'], '39': ['Scpiz6a_2425'], '12': ['Scpiz6a_1766'], '59': ['Scpiz6a_347'],
             '58': ['Scpiz6a_391'], '17': ['Scpiz6a_3066'], '16': ['Scpiz6a_730'], '19': ['Scpiz6a_1761'],
             '18': ['Scpiz6a_1764'], '31': ['Scpiz6a_2423'], '23': ['Scpiz6a_1766'], '51': ['Scpiz6a_696'],
             '50': ['Scpiz6a_1167'], '35': ['Scpiz6a_696'], '52': ['Scpiz6a_462'], '33': ['Scpiz6a_1764'],
             '55': ['Scpiz6a_344'], '37': ['Scpiz6a_1762'], '54': ['Scpiz6a_269'], '57': ['Scpiz6a_1764']}
                '''


def loadCPL(PATH):
    fh = open(PATH, 'r')
    LGDict = {}
    ChrDict = {}

    for line in fh:
        line = line.strip('\r')
        line = line.strip('\n')
        line2 = line.split('\t')
        LG = line2[2]
        Chr = line2[0]
        Pos = line2[1]
        if LG not in LGDict:
            LGDict[LG] = [Chr]
        else:
            LGDict[LG].append([Chr])
        if Chr not in ChrDict:
            ChrDict[Chr] = [LG]
        else:
            ChrDict[Chr].append([LG])
    return LGDict, ChrDict


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="VCF to pre-makeped")
    parser.add_argument("cpL_path1", type=str, help="Enter file path to a cpL file1", nargs='?')
    parser.add_argument("cpL_path2", type=str, help="Enter file path to a cpL file2", nargs='?')
    #parser.add_argument("new_vcf", type=str, help="Enter file name for output", nargs='?')
    args = parser.parse_args()


func2(args.cpL_path1, args.cpL_path2)
