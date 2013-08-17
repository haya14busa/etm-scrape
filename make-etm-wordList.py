# coding:utf-8
from bs4 import BeautifulSoup
import sys, codecs

sys.stdout = codecs.getwriter('utf_8')(sys.stdout)
sys.stdin = codecs.getreader('utf_8')(sys.stdin)

basefile = 'etmhtml/etm{num}.html'

etmWlist = []
for num in xrange(607):
    rfile = basefile.format(num=str(num+1).rjust(3, '0'))
    objFile = open(rfile,'r')
    try:
        html = objFile.read()
    finally:
        objFile.close()
    soup = BeautifulSoup(html)

    etmWlist.append('[{num}]'.format(num=str(num+1).rjust(3,'0')))
    print num+1 # for debug

    for i in xrange(len(soup.find_all(attrs={"color" : "darkblue"}))):
        etmWlist.append(soup.find_all(attrs={"color" : "darkblue"})[i].text) # English

wtext = '\n'.join(etmWlist).encode('utf-8')
f = open('etmWordList.txt', "w")
f.write(wtext)
f.close()
