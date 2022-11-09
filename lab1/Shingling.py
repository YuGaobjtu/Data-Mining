

'''
1.    A class Shingling that constructs k–shingles of a given length k (e.g., 10) from a given document,
computes a hash value for each unique shingle and represents the document in the form of
an ordered set of its hashed k-shingles.

'''


class Shingling:

    def __init__(self, k, document):
        self.k = k
        self.document = document
    
    '''
    Constructs K-Shinglets read more here:
    https://towardsai.net/p/l/text-similarity-using-k-shingling-minhashing-and-lshlocality-sensitive-hashing
    '''
    def construct_shinglets(self):
        shinglets = {''}  # note that it's a set so dublicates are not safed when added
        #print(f'constructing shinglet for: {self.document}')
        for i in range(len(self.document)):
            endOfShinglet = i + self.k
            if endOfShinglet <= len(self.document):
                shinglet = self.document[i:endOfShinglet]
                implodedShinglet = ''
                for j in range(len(shinglet)):
                    implodedShinglet += (shinglet[j])
                hasedShinglet = hash(implodedShinglet)
                #print(hasedShinglet)
                shinglets.add(hasedShinglet)
                #print('added')
        shinglets.remove('')
        lst = list(shinglets)
        lst.sort()
        return lst