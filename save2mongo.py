#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
#
# Author:   haya14busa
# URL:      http://haya14busa.com
# License:  MIT License
# Created:  2013-08-16
#

def getWordsList():
    objFile = open('wordList.txt','r')
    try:
        text = objFile.read()
    finally:
        objFile.close()
    return text.splitlines()

def main():
    words = getWordsList()
    print words


if __name__ == '__main__':
    main()
