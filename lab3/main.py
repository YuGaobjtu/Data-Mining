'''
TASK 1
First, implement the reservoir sampling or the Flajolet-Martin algorithm used in the graph algorithm 
presented in the paper you have selected;

TASK 2
Second, implement the streaming graph algorithm presented in the paper that uses the algorithm
implemented in the first step. 

--> It makes more sense for us to implement the Algo in one implementation.
'''

from GraphStorage import GraphStorage
from TriangleCountsStreamingAlgo import TriangleCountsStreamingAlgo

'''
Currently the output looks like this (sample):
Processing et: ('486658', '502407'). Immediate output for Kt: 3.0. Immedidate output for T_1964816: 1930250956928.0.
--> T is extremley high --> Fine tuning needed.
'''


def main():
    print('Computing transitivity for Web Google Graph: https://snap.stanford.edu/data/web-Google.html')
    graph = GraphStorage().loadGraph()
    triangleCountEstimate = TriangleCountsStreamingAlgo(graph).getTriangleCountEstimate()
    print('Transitivity is: {}'.format(triangleCountEstimate))

if __name__ == "__main__":
    main()