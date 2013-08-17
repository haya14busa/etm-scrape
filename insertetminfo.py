#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
#
# Author:   haya14busa
# URL:      http://haya14busa.com
# License:  MIT License
# Created:  2013-08-17
#
from pymongo import Connection
from pymongo.errors import ConnectionFailure

def getFile(fname):
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
    wlist = getFile('etmWordList.txt')
    # MongoDB
    db = connect2mongodb('mydict')

    etmnum = 0
    for word in wlist:
        if word[0] == '[':
            etmnum += 1
            # print etmnum
            continue
        # Search
        wdoc = searchMongo(db, word, 'eword')
        if not wdoc:
            print 'Error occur :' + word + str(etmnum)


if __name__ == '__main__':
    main()
