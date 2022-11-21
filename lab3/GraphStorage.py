'''

use web-google graph: https://snap.stanford.edu/data/web-Google.html

File looks like this:
# Directed graph (each unordered pair of nodes is saved once): web-Google.txt 
# Webgraph from the Google programming contest, 2002
# Nodes: 875713 Edges: 5105039
# FromNodeId	ToNodeId
0	11342
0	824020
0	867923
0	891835
11342	0
11342	27469
11342	38716
...

'''

#TODO retrieve and load graph

import csv


class GraphStorage:

    def __init__(self):
        self.path = 'Lab3\web-Google.txt'
        
    def loadGraph(self):
        # start reading file from the 5th row then for every line edge = (line[0], line[1])
        edges = []
        with open(self.path,'r') as f:
            for line in f.readlines()[4:]:
                edges.append((line.split()[0].strip(), line.split()[1].strip()))
        return edges