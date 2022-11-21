'''
We use the algorithm presented in this paper:
M. Jha, C. Seshadhri, and A. Pinar, 
A Space-Efficient Streaming Algorithm for Estimating Transitivity and Triangle Counts Using the Birthday Paradox,
ACM TKDD, 9-3, 2015.
Link: https://arxiv.org/pdf/1212.2264.pdf

'''

import random


class TriangleCountsStreamingAlgo:

    def __init__(self, streamGraph):
        self.streamGraph = streamGraph

    def getTriangleCountEstimate(self):
        #TODO return StreamingTriangles. This will return the estimate after the last element in the stream was processed
        return self.streamingTriangles(self.streamGraph, 5, 5)

    '''
    PSEUDO Code (ALGO 1)
    Input: se, sw
    1 Initialize edge res of size se and wedge res of size sw. For each edge et in stream,
    2 Call UPDATE(et).
    3 Let ρ be the fraction of entries in isClosed set to true.
    4 Set κt = 3ρ.
    5 Set Tt = [ρt2/se(se − 1)] × tot wedges.
    '''
    def streamingTriangles(self, stream, se, sw):
        # 1
        edge_res = [[]] * se # edge reservoir maintains a uniform random sample of edges observed so fa
        # 1
        wedge_res = [[]] * sw # maintains a uniform sample of the wedges created by the edge reservoir at any step of the process
        # 1
        t = 1
        isClosed = [False] * sw # default wedge detected as not closed
        for et in stream:
            # 2
            edge_res, wedge_res, isClosed, tot_wedges = self.update(et, t, se, sw, edge_res, wedge_res, isClosed)
            # 3
            p = isClosed.count(True) / len(isClosed)
            # 4
            kt = 3*p
            # 5
            Tt = ((p * (t**2)) / (se * (se - 1))) * tot_wedges
            print('Processing et: {}. Immediate output for Kt: {}. Immedidate output for T_{}: {}.'.format(et, kt, t, Tt))
            # Update t
            t += 1
        return Tt # Return the value for the last value in the stream

    '''
    PSEUDO Code (ALGO 2)
    Input: e.g. et = (u, v), t=0, ...
    1 for i = 1, . . . , sw
    2   if wedge res[i] closed by et
    3       isClosed[i] ← true
    4 for i = 1, . . . , se
    5   Pick a random number x in [0, 1]
    6   if x ≤ 1/t
    7       edge res[i] ← et.
    8 if there were any updates of edge res
    9   Update tot wedges, the number of wedges formed by edge res.
    10  Determine Nt (wedges involving et) and let new wedges = |Nt|.
    11  for i, . . . sw ,
    12      Pick a random number x in [0, 1]
    13      if x ≤ new wedges/tot wedges
    14          Pick uniform random w ∈ Nt.
    15          wedge res[i] ← w.
    16          SisClosed[i] ← false.
    '''
    def update(self, et, t, se, sw, edge_res, wedge_res, isClosed):
        # ----------------------------------------------------------------------------
        # ******************* DETERMINE WEDGES CLOSED BY ET **************************
        # 1
        for i in range(sw):
            # 2 
            wed = wedge_res[i] # e.g. wedge = [(u1, v1), (u2, v2)]   et = (u3, v3)
            if wed != []:
                c1 = wed[0][0] == wed[1][0] and (wed[0][1] in et or wed[1][1] in et)
                c2 = wed[0][0] == wed[1][1] and (wed[0][1] in et or wed[1][0] in et)
                c3 = wed[0][1] == wed[1][0] and (wed[0][0] in et or wed[1][1] in et)
                c4 = wed[0][1] == wed[1][1] and (wed[0][0] in et or wed[1][0] in et)
                # 3
                if c1 or c2 or c3 or c4:
                    isClosed[i] = True
                 
        # ***************** DONE DETERMINE WEDGES CLOSED BY ET ***********************
        # ----------------------------------------------------------------------------
        # *****************   RESERVOIR SAMPLING EDGES *******************************
        # PART OF RESERVOIR SAMPLING (replacing each entry by et with probability 1/t)
        # 4 
        anyUpdateOnEdgeRes = False
        for i in range(se):
            # 5 
            x = random.randint(0, 1)
            # 6
            if x <= 1/t:
                # 7
                edge_res[i] = et
                anyUpdateOnEdgeRes = True
        # ******************* DONE RESERVOIR SAMPLING ******************************** 
        # ----------------------------------------------------------------------------
        # *************************** PERFORM UPDATES ******************************** 
        # 8
        tot_wedges = 0
        if anyUpdateOnEdgeRes:
            # 9 (This is the total number of wedges formed by edges in the current edge res)
            for i in range(len(edge_res)):
                for j in range(i+1, len(edge_res)):
                    if edge_res[j][0] in edge_res[i] or edge_res[j][1] in edge_res[i]:
                        tot_wedges += 1

            # 10
            Nt = []
            if et in edge_res: # if to speed up computation assuming in many cases we don't need for loop as et is not even in edge_res
                for edge in edge_res:
                    if et[0] in edge or et[1] in edge: # et = (u,v); edge = (x,y)
                        Nt.append([edge, et])
            new_wedges = len(Nt)

        # *************************** DONE PERFORM UPDATES ******************************
        # -------------------------------------------------------------------------------
        # *****************   RESERVOIR SAMPLING WEDGES *********************************
            # 11
            for i in range(sw):
                # 12
                x = random.randint(0, 1)
                # 13
                if x <= new_wedges/tot_wedges:
                    # 14
                    w = random.choice(Nt)
                    # 15
                    wedge_res[i] = w
                    # 16
                    isClosed[i] = False

        # *****************   DONE RESERVOIR SAMPLING WEDGES *****************************
        # --------------------------------------------------------------------------------

        return edge_res, wedge_res, isClosed, tot_wedges