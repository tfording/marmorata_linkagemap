#author=Tyler Fording

import collections
import plotly as plotly
import plotly.plotly as py
import plotly.graph_objs as go
import numpy as np

plotly.tools.set_credentials_file(username='tfording@gmail.com', api_key='EKzXldHDmrPQRqgAUsCQ')
plotly.tools.set_config_file(world_readable=False, sharing='secret')

scaf_list = ['Scpiz6a_39', 'Scpiz6a_34', 'Scpiz6a_696', 'Scpiz6a_37', 'Scpiz6a_30', 'Scpiz6a_31', 'Scpiz6a_32', \
             'Scpiz6a_17.2', 'Scpiz6a_408', 'Scpiz6a_1005', 'Scpiz6a_368', 'Scpiz6a_30.1', 'Scpiz6a_11.1', \
             'Scpiz6a_23', 'Scpiz6a_22', 'Scpiz6a_27', 'Scpiz6a_26', 'Scpiz6a_29', 'Scpiz6a_28', 'Scpiz6a_23.1', \
             'Scpiz6a_2672', 'Scpiz6a_60', 'Scpiz6a_55', 'Scpiz6a_126.1', 'Scpiz6a_173', 'Scpiz6a_8', \
             'Scpiz6a_263', 'Scpiz6a_1', 'Scpiz6a_5', 'Scpiz6a_378', 'Scpiz6a_185', 'Scpiz6a_102', 'Scpiz6a_105', \
             'Scpiz6a_45', 'Scpiz6a_44', 'Scpiz6a_47', 'Scpiz6a_136.1', 'Scpiz6a_43', 'Scpiz6a_201', 'Scpiz6a_49', \
             'Scpiz6a_44.1', 'Scpiz6a_782', 'Scpiz6a_73', 'Scpiz6a_118', 'Scpiz6a_593', 'Scpiz6a_291', \
             'Scpiz6a_113', 'Scpiz6a_115', 'Scpiz6a_117', 'Scpiz6a_1204', 'Scpiz6a_55.2', 'Scpiz6a_55.1', \
             'Scpiz6a_745', 'Scpiz6a_120', 'Scpiz6a_170.1', 'Scpiz6a_2423', 'Scpiz6a_3236', 'Scpiz6a_86', \
             'Scpiz6a_1453', 'Scpiz6a_434', 'Scpiz6a_232', 'Scpiz6a_136', 'Scpiz6a_72', 'Scpiz6a_122', \
             'Scpiz6a_74', 'Scpiz6a_75', 'Scpiz6a_970', 'Scpiz6a_11', 'Scpiz6a_16', 'Scpiz6a_17', 'Scpiz6a_382', \
             'Scpiz6a_18.1', 'Scpiz6a_60.1', 'Scpiz6a_147', 'Scpiz6a_146', 'Scpiz6a_141', 'Scpiz6a_68', \
             'Scpiz6a_66', 'Scpiz6a_65', 'Scpiz6a_148', 'Scpiz6a_1476', 'Scpiz6a_393', 'Scpiz6a_32.1', \
             'Scpiz6a_253', 'Scpiz6a_90', 'Scpiz6a_99']

def importData(sepIden_path, parCall_path):
    '''
    Loads scaffolds and every LG assignment associated with the scaffold into a dictionary.
    :param sepIden_path: Path to SeparateIdenticals.out
    :param parCall_path: Path to ParentCall2.out
    :return: Dictionary
    '''
    parCall_fh = open(parCall_path, 'r')
    sepIden_fh = open(sepIden_path, 'r')

    scafLG_dict = {}

    #lines the two files up to be read in order
    parCall_fh.readline()
    parCall_fh.readline()
    parCall_fh.readline()
    parCall_fh.readline()
    parCall_fh.readline()
    parCall_fh.readline()
    parCall_fh.readline()
    sepIden_fh.readline()
    counter = 0
    for line in sepIden_fh:
       if line == "0\n":  # Ignores variants that were not assigned to a linkage group
            parCall_fh.readline()
            pass
       else:
            pCall_line = parCall_fh.readline()
            pCall_line = pCall_line.strip('\n')
            pCall_line = pCall_line.split('\t')
            sIden_line = line.strip('\n')

            if pCall_line[0] not in scafLG_dict:
                scafLG_dict[pCall_line[0]] = [int(sIden_line)]
            else:
                scafLG_dict[pCall_line[0]].append(int(sIden_line))
    parCall_fh.close()
    sepIden_fh.close()
    print "scafLG_dict complete"
    condenseData(scafLG_dict)
    return scafLG_dict


def condenseData(scafLG_dict):
    '''
    This function takes a dictionary and creates a list of the linkage groups and how many markers assigned to 
    them in relation to each scaffold
    :param scafLG_dict: Dictionary from importData
    :return: calls writeCSV returns a list of scaffold names
    '''
    condensedLG_array = []
    for key in scafLG_dict:
        counts = str(collections.Counter(scafLG_dict[key]))
        condensedLG_array.append([key, counts[9:-2]])
    print 'condensed data complete'
    scaf_list = []
    for item in condensedLG_array:
        scaf_list.append(item[0])
    writeCSV(condensedLG_array, 'scatterplot_R10.csv', scaf_list)

    return condensedLG_array, scaf_list  # [['Scpiz6a_39', '9: 4023, 20: 2085, 22: 1417, 23: 975'],...]


def writeCSV(condensedLG_array, fh_out, scaf_list):
    '''
    Writes a csv of scaffold,lg,markernum
    :param condensedLG_array: input array
    :param fh_out: output file name and path
    :param scaf_list: list of scaffold names
    :return: n/a
    '''
    scaf_index = [i for i in range(len(scaf_list))]

    fh_out = open(fh_out, 'w')
    fh_out.write('#scaffold,scafINDEX,LG,NUM_MARKERS\n')
    for scaffold in condensedLG_array:
        item = scaffold[1]
        item = item.split(',')
        for lg in item:
            lg = lg.replace(' ','')
            lg = lg.split(':')
            #print lg
            indexnum = scaf_list.index(scaffold[0])
            to_write = str(scaffold[0]+','+str(indexnum)+','+str(lg[0])+','+str(lg[1]+'\n'))
            fh_out.write(to_write)
    fh_out.close()


def scatterPlot(numLG, scaf_list, csvPath):
    '''
    This function takes a number of LGs, a list of scaffolds, and a csv of LG associations to markers/scaffolds and 
    creates a scatter plot based on the linkage groups the markers from each scaffold are assigned to.
    :param numLG: Number of LGs appearing in the dataset 
    :param scaf_list: List of scaffolds 
    :param csvPath: CSV to the data we're plotting
    :return: Creates a html plot
    '''
    fh_in = open(csvPath, 'r')
    scaffoldNames = []
    y_scaffoldIndex = []
    x_LG = []
    col_markernum = []

    for line in fh_in:  # Creates all of the needed lists to plot the scatter plot
        if line[0] == '#':
            pass
        else:
            line = line.strip('\n')
            line = line.split(',')
            #print line[3]
            if int(line[3]) >= 500:
                scaffoldNames.append(line[0])
                y_scaffoldIndex.append(line[1])
                x_LG.append(line[2])
                col_markernum.append(line[3])
    fh_in.close()

    ############## This creates the graph
    trace1 = go.Scatter(
        y = y_scaffoldIndex,
        x = x_LG,
        hoverinfo=col_markernum,
        mode='markers',
        marker=dict(
            size='22',
            color=col_markernum,
            colorscale='Viridis',
            showscale=True
            )
        )
    ############## This creates the X-Axis
    bandxaxis = go.XAxis(
        title="Linkage Group Assignment",
        range=[0,25],
        showgrid=True,
        showline=True,
        ticks="",
        showticklabels=True,
        tick0=0,
        dtick=1
        )
    ############## This creates the Y-Axis
    bandyaxis = go.YAxis(
        title="Scaffold Name",
        #range=[0, len(y_scaffoldIndex)],
        showgrid=True,
        showline=True,
        ticks="",
        tickangle=-45,
        showticklabels=True,
        mirror=False,
        ticktext=scaffoldNames,
        tickvals=y_scaffoldIndex
        )

    ############## This creates the layout object for the graph
    layout = go.Layout(
        title="Linkage Group Assignment by Scaffold",
        xaxis=bandxaxis,
        yaxis=bandyaxis
        )
    ############## This creates the graph object
    data = [trace1]

    ############## This creates the actual figure
    fig = go.Figure(data=data, layout=layout)
    plotly.offline.plot(fig, filename='scaffold_lg_assignment_R10_500cutoff.html')


















scatterPlot(31, scaf_list, '/Volumes/projects/tfording/marmorata/bin/scatterplot_R10.csv')
#importData('./100MapQpPairs/father_mapQ100_propPair100_R10_SepIden.out', './100MapQpPairs/youfather_mapQ100_propPair100_R10_parentCall2.out')