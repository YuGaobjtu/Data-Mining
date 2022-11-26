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

def main():
    print('Computing transitivity for Web Google Graph: https://snap.stanford.edu/data/web-Google.html')
    graph = GraphStorage().loadGraph()
    triangleCountEstimate, transitivityEstimate = TriangleCountsStreamingAlgo(graph).getTriangleCountEstimate()
    print('Estimated Triangles: {}. Estimated Transitivity is: {}'.format(triangleCountEstimate, transitivityEstimate))

if __name__ == "__main__":
    main()