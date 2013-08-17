#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
#
# Author:   haya14busa
# URL:      http://haya14busa.com
# License:  MIT License
# Created:  2013-08-17
#
from bs4 import BeautifulSoup
import re

from pymongo import Connection
from pymongo.errors import ConnectionFailure

def getFile(fname):
    objFile = open(fname,'r')
    try:
        text = objFile.read()
    finally:
        objFile.close()
    return text

def connect2mongodb(db):
    try:
        c = Connection(host="localhost", port=27017)
        print "Connected successfully"
    except ConnectionFailure, e:
        sys.stderr.write("Could not connect to MongoDB: %s" % e)
        sys.exit(1)
    return c[db]

def main():
    # Get text
    html = getFile('LearnAIObyEtm.html')
    soup = BeautifulSoup(html)


    linklist = soup.findAll('a')
    unumSet = set()
    for link in linklist:
        unumSet.add(re.search('\d+',link.attrs['href']).group(0))
    # print unumSet

    # MongoDB
    db = connect2mongodb('mydict')

    er_sn_inSet = set()
    for unum in unumSet:
        er_sn_in = db.words.find_one({'alc_etm.unum':int(unum)})['alc_etm']['er_sn_in']
        er_sn_inSet.add(er_sn_in)
    print 'the number of words : ' , len(unumSet)
    print 'the number of etm   : ' , len(er_sn_inSet)



if __name__ == '__main__':
    main()
