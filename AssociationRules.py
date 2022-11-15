'''
Solve the second sub-problem, i.e., develop and implement an algorithm for generating association rules between
frequent itemsets discovered using the A-Priori algorithm in a dataset of sales transactions. The rules must have
the support of at least s and confidence of at least c, where s and c are given as input parameters.

'''
from itertools import permutations

class AssociationRules:

    def __init__(self, frequentItems, confidence):
        self.frequentItems = frequentItems
        self.confidence = confidence

    #FIXME
    def getBinaryPartitioning(self, frequentItemset):
        frequentItemset = list(frequentItemset)
        # frequentItemset = {Milk, Diaper, Beer}
        # return [({Milk,Diaper}, {Beer}), ({Milk,Beer}, {Diaper}),({Diaper,Beer}, {Milk}),({Beer}, {Milk,Diaper}),({Diaper}, {Milk,Beer}),({Milk}, {Diaper,Beer})]
        
        # helpful?? l = list(permutations({1,2,3}))
        return [(frequentItemset[0], frequentItemset[1:])]

    def ruleHasConfidence(self, rule):
        #TODO check if rules as confidence level: self.confidence
        return True

    '''
    description: returns high confidence rules from each frequent itemset, where each rule is a binary partitioning of a 
    frequent itemset

    return: list of tupel with two entries: X, Y such that later X->Y can be printed 
    example: return [({123, 125}, {345}), ({234}, {'786'})]
    '''
    def getAssociationRules(self):
        confidentRules = []
        for frequentItem in self.frequentItems:
            if len(frequentItem) > 1:
                candidateRules = self.getBinaryPartitioning(frequentItem)
                for candidateRule in candidateRules:
                    if self.ruleHasConfidence(candidateRule):
                        confidentRules.append(candidateRule)
        #return [({123, 125}, {345}), ({234}, {'786'})] #TODO remove this line after making getBinaryPartition and rule has confidence work
        return confidentRules
