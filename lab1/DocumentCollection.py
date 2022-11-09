'''
Contains our document collection
'''

class DocumentCollection:

    def __init__(self, documents):
        #TODO add source path and do the data loading and processing here
        self.documents = documents


    def getDocuments(self):
        #TODO use self.documents path to load data
        documents = ['This is a wonderful document. And so...', 'This is a terrible document', 'This is about python', 'This document works just fine']
        #contains a list of (list of words/strings)
        documentsProcessed = []
        for i in range(len(documents)):
            if documents[i] == '':
                continue
            documentsProcessed.append(documents[i].split())

        return documentsProcessed