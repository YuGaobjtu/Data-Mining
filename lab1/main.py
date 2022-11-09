
'''
OBJECTIVES
1.    A class Shingling that constructs k–shingles of a given length k (e.g., 10) from a given document, computes a hash value for each unique shingle and represents the document in the form of an ordered set of its hashed k-shingles.
2.    A class CompareSets computes the Jaccard similarity of two sets of integers – two sets of hashed shingles.
3.    A class MinHashing that builds a minHash signature (in the form of a vector or a set) of a given length n from a given set of integers (a set of hashed shingles).
4.    A class CompareSignatures estimates the similarity of two integer vectors – minhash signatures – as a fraction of components in which they agree.
5.    (Optional task for extra 2 bonus points) A class LSH that implements the LSH technique: given a collection of minhash signatures (integer vectors) and a similarity threshold t, the LSH class (using banding and hashing) finds candidate pairs of signatures agreeing on at least a fraction t of their components.

'''
# Optimization of code: 
# -- Only calculate shinglingA and B once


from CompareSets import CompareSets
from CompareSignatures import CompareSignatures
from DocumentCollection import DocumentCollection
from MinHashing import MinHashing
from Shingling import Shingling


def isPrime(p):
    if p<2: return False
    for i in range(2,p):
        if (p%i) == 0:
            return False
    return True

def getK():
    return 2

def getShinglets(documentA, documentB):
    #STEP 1 Shingling
    shinglingA = Shingling(getK(), documentA).construct_shinglets()
    shinglingB = Shingling(getK(), documentB).construct_shinglets()
    return shinglingA, shinglingB

def calculateSimilarityJaccard(documentA, documentB):
    #STEP 1 Shingling
    shinglingA, shinglingB = getShinglets(documentA, documentB)
    #STEP 2 Compare Shingling A and B
    return CompareSets(shinglingA, shinglingB).compareHashedShingles()

def getN():
    return 20

primes = [i for i in range(getN()) if isPrime(i)]

def calculateSimilarityMinHash(documentA, documentB):
    shinglingA, shinglingB = getShinglets(documentA, documentB)
    minHashSignatureA = MinHashing(getN(), shinglingA, primes).getMinHashSignature()
    minHashSignatureB = MinHashing(getN(), shinglingB, primes).getMinHashSignature()
    return CompareSignatures(minHashSignatureA, minHashSignatureB).getMinHashSimilarity()

def main():
    #Load Data and Process it
    #Position in the List determines document ID
    documents = DocumentCollection('path/...').getDocuments()
    similarities = []
    for i in range(len(documents)):
        for j in range(i + 1 , len(documents)):
            if(i == j):
                continue
            simJaccard = calculateSimilarityJaccard(documents[i], documents[j])
            simMinHash = calculateSimilarityMinHash(documents[i], documents[j])

            similarities.append((i, j, simJaccard, simMinHash))

    #Print results
    print('Similarity List')
    for i in range(len(similarities)):
        print('docID:{}, docID:{}, Jaccard Similarity:{}. MinHash Signature Similarity {}'.format(similarities[i][0], similarities[i][1], similarities[i][2], similarities[i][3]))
    
    
if __name__ == "__main__":
    main()



