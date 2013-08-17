#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
#
# Author:   haya14busa
# URL:      http://haya14busa.com
# License:  MIT License
# Created:  2013-08-17
#
from nltk.corpus import stopwords
from nltk import tokenize
from nltk import stem

from pymongo import Connection
from pymongo.errors import ConnectionFailure



def getStopset(lang='english'):
    return set(stopwords.words(lang))

def getAIOText(fname):
    objFile = open(fname,'r')
    try:
        text = objFile.read()
    finally:
        objFile.close()
    return text.splitlines()

def connect2mongodb(db):
    try:
        c = Connection(host="localhost", port=27017)
        print "Connected successfully"
    except ConnectionFailure, e:
        sys.stderr.write("Could not connect to MongoDB: %s" % e)
        sys.exit(1)
    return c[db]

def searchMongo(dbh, searchword, field):
    # db = connect2mongodb('mydict')
    return dbh.words.find_one({field:searchword},{'alc_etm.unum':1})

def main():
    # Get text
    sentences = getAIOText('aio.txt')
    # MongoDB
    db = connect2mongodb('mydict')
    # NLTK
    stopset = getStopset('english')
    stemmer = stem.LancasterStemmer()
    pstemmer = stem.PorterStemmer()
    lemmatizer = stem.WordNetLemmatizer()
    # ALC etymology dictionary's base link format
    wlink = "<a href=\"http://home.alc.co.jp/db/owa/etm_sch?unum={num}&stg=2\" target='_blank'>{w}</a>"
    # Prepare for result sentences
    rsentences = []

    for num, sentence in enumerate(sentences):
        rsentence = [] # result sentence
        print num+1 # for debug
        for word in tokenize.wordpunct_tokenize(sentence):
            # Continue if word is in stopset
            if len(word) < 3 or word in stopset:
                rsentence.append(word)
                continue
            # Make word lowercase
            lword = word.lower()
            # Search lowercase , lemma, stem
            wdoc = searchMongo(db, lword, 'lemma') or \
                   searchMongo(db, lemmatizer.lemmatize(lword), 'lemma') or \
                   searchMongo(db, stemmer.stem(lword), 'stem') or \
                   searchMongo(db, pstemmer.stem(lword), 'stem')
            if wdoc:
                rsentence.append(wlink.format(num=wdoc['alc_etm']['unum'],w=word))
            else:
                rsentence.append(word)

        sentence_text = '<dt>{n}</dt><dd><p>{text}</p></dd>\n'.format(
                    n    = str(num+1).rjust(3,'0'),
                    text = ' '.join(rsentence)
                )
        rsentences.append(sentence_text)
    wtext = "<h1>Link from ALL IN ONE to ALC's Online Etymology Dictionary</h1>\n \
            <dl>{contents}</dl>".format(contents='\n'.join(rsentences))

    f = open('LearnAIObyEtm.html', 'w')
    f.write(wtext)
    f.close()

if __name__ == '__main__':
    main()
