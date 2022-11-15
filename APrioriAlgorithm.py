


class APrioriAlgorithm:

    def __init__(self, T, minSupport) :
        self.baskets = list(map(set, T))
        self.amountOfBaskets = len(self.baskets)
        self.minSupport = minSupport

        C = []
        for basket in T:
            for item in basket:
                if not [item] in C:
                    C.append([item])

        self.C_1 = list(map(frozenset, C))
        # list of {singelton} i.e. all singleton candidates in a list where every item is a set  
    
    '''
    return: list of {k-tupel} where every k-tupel is a candidate to be frquent and therefor placed in Lk later
    '''
    def createCandidates(self, prev_L_k, k): #creates Ck
        C_k = []
        for i in range(len(prev_L_k)):
            for j in range(i+1, len(prev_L_k)): 
                a = list(prev_L_k[i])[:k]; a.sort() # sort so that you can compare what was previous a (unsorted) set
                b = list(prev_L_k[j])[:k]; b.sort()

                if a==b: #if first k-2 elements are equal merge the sets that have a shared intersection
                    C_k.append(prev_L_k[i].union(prev_L_k[j])) #set union
        return C_k
    

    def getFrequentItems(self, C_k):
        countDic = {}
        for basket in self.baskets:
            for candidate in C_k:
                if candidate.issubset(basket):
                    if not candidate in countDic: 
                        countDic[candidate] = 1
                    else: 
                        countDic[candidate] += 1
        frequentItemList = []
        for candidate in countDic:
            support = countDic[candidate]/self.amountOfBaskets
            if support >= self.minSupport:
                frequentItemList.insert(0,candidate)
        return frequentItemList

    '''
    return: list of {frequent k-tupels}
    '''
    def runApriori(self):
        L_1 = self.getFrequentItems(self.C_1)
        L = [L_1]
        k = 0
        while (len(L[k]) > 0): # stop when no more k-frequent items were found
            C_k = self.createCandidates(L[k], k-2)
            L_k = self.getFrequentItems(C_k)
            L.append(L_k)
            k += 1
        return L