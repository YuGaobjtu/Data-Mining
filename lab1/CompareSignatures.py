
'''
4.    A class CompareSignatures estimates the similarity of two integer vectors – minhash signatures – 
as a fraction of components in which they agree.

'''

class CompareSignatures:

    def __init__(self, minHashSignature1, minHashSignature2):
        self.minHashSignature1 = minHashSignature1
        self.minHashSignature2 = minHashSignature2
    
    def getMinHashSimilarity(self):
        agreeCount = 0
        for i in range(len(self.minHashSignature1)):
            if self.minHashSignature1[i] == self.minHashSignature2[i]:
                agreeCount += 1
        return agreeCount/len(self.minHashSignature1)