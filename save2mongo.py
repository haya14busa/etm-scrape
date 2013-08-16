#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
#
# Author:   haya14busa
# URL:      http://haya14busa.com
# License:  MIT License
# Created:  2013-08-16
#

import sys
from datetime import datetime

# mongoDB
from pymongo import Connection
from pymongo.errors import ConnectionFailure
# NLTK
from nltk import stem

def connect2mongodb(db):
    try:
        c = Connection(host="localhost", port=27017)
        print "Connected successfully"
    except ConnectionFailure, e:
        sys.stderr.write("Could not connect to MongoDB: %s" % e)
        sys.exit(1)
    return c[db]

def getWordsList():
    objFile = open('wordList.txt','r')
    try:
        text = objFile.read()
    finally:
        objFile.close()
    return text.splitlines()

def getWordDocList():
    words = getWordsList()

    stemmer = stem.LancasterStemmer()
    lemmatizer = stem.WordNetLemmatizer()

    doclist = []
    for num, word in enumerate(words):
        lword  = word.lower()
        lmword = lemmatizer.lemmatize(lword)
        stword = stemmer.stem(lword)

        word_doc = {
                'eword'    : word,
                'alc_etm'  : {
                                'unum'     : num+1,
                                'er_sn_in' : None
                             },
                'lemma'    : lmword,
                'stem'     : stword,
                'from'     : 'alc_etm',
                'created_at'     : datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        doclist.append(word_doc)
        print num
    return doclist

def main():
    db = connect2mongodb('mydict')

    word_docs = getWordDocList()

    db.words.insert(word_docs, safe=True)
    print "Successfully bulk inserted document"

if __name__ == '__main__':
    main()
