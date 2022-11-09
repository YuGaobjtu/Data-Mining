
'''
3.    A class MinHashing that builds a minHash signature (in the form of a vector or a set) 
of a given length n from a given set of integers (a set of hashed shingles).

'''

import random


class MinHashing:
    

    def __init__(self, n, hashedShingles, primes):
        self.n = n
        self.hashedShingles = hashedShingles
        self.primes = primes

    def hashFunction(self, a, b, p, x):
        return (a + b*x) % p

    def getMinHashSignature(self):
        signature = []
        for i in range(self.n):
            #apply hash function to every value in hashedShinglet
            shakeBasket = [] # contains the hash of every hashedShinglet
            for hashedShinglet in self.hashedShingles:
                shakeBasket.append(self.hashFunction(random.randrange(self.n), random.randrange(self.n), random.choice(self.primes), hashedShinglet))
                #shakeBasket.append(self.hashFunction(i, i%10, self.primes[i%len(self.primes)], hashedShinglet))

            signature.append(min(shakeBasket))
        return signature
