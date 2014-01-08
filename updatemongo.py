#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
#
# Author:   haya14busa
# URL:      http://haya14busa.com
# License:  MIT License
# Created:  2013-08-16
#

import sys

# mongoDB
from pymongo import Connection
from pymongo.errors import ConnectionFailure


def connect2mongodb(db):
    try:
        c = Connection(host="localhost", port=27017)
        print "Connected successfully"
    except ConnectionFailure, e:
        sys.stderr.write("Could not connect to MongoDB: %s" % e)
        sys.exit(1)
    return c[db]


def main():
    db = connect2mongodb('mydict')

    # print 'old: ', db.words.find_one({'eword':'acerbic'})
    # db.words.update({'alc_etm.unum':1},
    #         {'$set':{'alc_etm.er_sn_in':1}}, safe=True)
    # print 'new: ', db.words.find_one({'eword':'acerbic'})
    for word in db.words.find():
        db.words.update(word, {'$inc': {'alc_etm.unum': 'true'}})


if __name__ == '__main__':
    main()
