from bs4 import BeautifulSoup
import sys, codecs

sys.stdout = codecs.getwriter('utf_8')(sys.stdout)
sys.stdin = codecs.getreader('utf_8')(sys.stdin)


rfile = 'etmhtml/etm001.html'
objFile = open(rfile,'r')
try:
    html = objFile.read()
finally:
    objFile.close()

soup = BeautifulSoup(html)

print soup.find_all(attrs={"bgcolor" : "white"})[0].text

for i in xrange(len(soup.find_all(attrs={"color" : "darkblue"}))):
    print soup.find_all(attrs={"color" : "darkblue"})[i].text # English
    print soup.find_all('dl')[i].text # Japanese


