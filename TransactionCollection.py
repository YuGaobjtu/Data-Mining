'''
Contains our transaction collection i.e. our baskets
'''

class TransactionCollection:

    def __init__(self, path):
        self.path = path


    def getTransactions(self):
        # TODO load document from self.path
        transactions = [[1444, 2, 1, 25, 52, 164, 240, 274, 328, 368, 448, 538, 561, 630, 687, 730, 775, 825, 834], [1444, 2, 1, 39, 120, 124, 205, 401, 581, 704, 814, 825, 834], [1444, 2, 1, 35, 249, 674, 712, 733, 759, 854, 950], [1444, 2, 1, 39, 422, 449, 704, 25, 857, 895, 937, 954, 964]]
        #transactions = [[25, 52, 164, 1], [1, 39, 120, 25, 52], [1, 35, 249, 52], [35, 422, 52, 704, 25]]
        return transactions