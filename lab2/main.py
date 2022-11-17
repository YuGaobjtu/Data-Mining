'''
Introduction

The problem of discovering association rules between itemsets in a sales transaction database (a set of baskets) 
includes the following two sub-problems [R. Agrawal and R. Srikant, VLDB '94 Links to an external site.]:
- Finding frequent itemsets with support at least s;
- Generating association rules with confidence at least c from the itemsets found in the first step.

Remind that an association rule is an implication X → Y, where X and Y are itemsets such that X∩Y=∅.
Support of rule X → Y is the number of transactions that contain X⋃Y. Confidence of rule X → Y is the fraction
of transactions containing X⋃Y in all transactions that contain X.

'''

'''
TASK 1
You are to solve the first sub-problem: to implement the A-Priori algorithm for finding frequent itemsets
with support at least s in a dataset of sales transactions. Remind that support of an itemset is the number
of transactions containing the itemset. To test and evaluate your implementation, write a program that uses
your A-Priori algorithm implementation to discover frequent itemsets with support at least s in a given dataset
of sales transactions.

TASK 2
Solve the second sub-problem, i.e., develop and implement an algorithm for generating association rules between
frequent itemsets discovered using the A-Priori algorithm in a dataset of sales transactions. The rules must have
the support of at least s and confidence of at least c, where s and c are given as input parameters.

'''

from TransactionCollection import TransactionCollection
from AssociationRules import AssociationRules
from APrioriAlgorithm import APrioriAlgorithm

'''
Performance improvements:
- print frequent items and rules as they are found so that the item and rule list doesn't have to be iterated again
- use vectorized approach for fast computation
'''


def main():
    print(' *** starting to run script *** ')
    
    #LOAD Data into Transaction Collection
    baskets = TransactionCollection('T10I4D100K.dat').getTransactions()

    #TASK 1: Finding frequent itemsets
    minSupport = 0.3
    frequentItems = APrioriAlgorithm(baskets, minSupport).runApriori()
    print('frequent items:\n{}'.format(frequentItems))

    #TASK 2: Find association rules
    confidence = 0.75
    assocationRules = AssociationRules(frequentItems, confidence).getAssociationRules()
    print('frequently bought together:')
    for rule in assocationRules:
        print('{} --> {}'.format(rule[0], rule[1]))

if __name__ == "__main__":
    main()
