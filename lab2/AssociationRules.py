class AssociationRules:

    def __init__(self, frequentItems, confidence, dataset):
        self.frequentItems = frequentItems
        self.confidence = confidence
        self.dataset = dataset

    def getPartitioning(self, frequentItems):
        i = 0
        frequentset = []
        while(frequentItems[i]):
            j = 0
            while j < len(frequentItems[i]):
                frequentset.append(frequentItems[i][j])
                j += 1
            i += 1
        return frequentset

    def countsupport(self,item,dataset):
        baskets = list(map(set, dataset))
        k = 0
        for basket in baskets:
            if item.issubset(basket):
                    k += 1
        return k

    '''
    description: returns high confidence rules from each frequent itemset, where each rule is a binary partitioning of a 
    frequent itemset

    return: list of tupel with two entries: X, Y such that later X->Y can be printed 
    example: return [({123, 125}, {345}), ({234}, {'786'})]
    '''
    def getAssociationRules(self):
        frequentset = self.getPartitioning(self.frequentItems)
        i = 0
        while(i < len(frequentset)):
            j = 0
            while(j < len(frequentset)):
                union = frequentset[i].union(frequentset[j])
                test = self.countsupport(union,self.dataset)/self.countsupport(frequentset[i],self.dataset)
                if frequentset[i].intersection(frequentset[j]) == set() and test >= self.confidence:
                        print(frequentset[i],frequentset[j],test)
                j += 1
            i += 1
        return union