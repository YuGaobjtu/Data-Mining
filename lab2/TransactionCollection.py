'''
Contains our transaction collection i.e. our baskets
'''

import csv

class TransactionCollection:

    def __init__(self, path):
        self.path = path


    def getTransactions(self):
        # TODO load document from self.path
        with open(self.path, newline = '') as file:
            reader = csv.reader(file, quoting = csv.QUOTE_NONNUMERIC,delimiter = ' ')
            # storing all the rows in an output list
            output = []
            for row in reader:
                output.append(row[:])
        for x in output:
            x.pop()
        #transactions = [[25, 52, 164, 1], [1, 39, 120, 25, 52], [1, 35, 249, 52], [35, 422, 52, 704, 25]]
        return output
