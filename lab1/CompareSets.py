
'''
2.    A class CompareSets computes the Jaccard similarity of two sets of integers – two sets of hashed shingles.

'''
import numpy as np

class CompareSets:
    
    # e.g. shingle1 [1127474, 72736263, 32723723733, 37273723]
    def __init__(self, hashedShingle1, hashedShingle2):
        self.hashedShingle1 = hashedShingle1
        self.hashedShingle2 = hashedShingle2


    def compareHashedShingles(self):
        # return Number of Shared Items / Total Items.
        set1 = set(self.hashedShingle1)
        set2 = set(self.hashedShingle2)
        numSharedItems = len(set1.intersection(set2))
        numTotalItems = len(set1.union(set2))
        return round(numSharedItems/numTotalItems, 3)