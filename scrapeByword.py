from bs4 import BeautifulSoup
import sys
import codecs

sys.stdout = codecs.getwriter('utf_8')(sys.stdout)
sys.stdin = codecs.getreader('utf_8')(sys.stdin)

wordList = []
for i in xrange(9404):
    if(i == 3265):
        word = 'NONE'  # 3266 page doesn't exist
    else:
        rfile = 'wordhtml/word{num}.html'.format(num=str(i+1).rjust(4, '0'))
        objFile = open(rfile, 'r')
        try:
            html = objFile.read()
        finally:
            objFile.close()
        soup = BeautifulSoup(html)
        word = soup.find_all(attrs={"color": "darkblue"})[0].text
    wordList.append(word)


wtext = '\n'.join(wordList).encode('utf-8')
f = open('wordList.txt', "w")
f.write(wtext)
f.close()
