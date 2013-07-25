objFile = open('wordList.txt','r')
try:
    text = objFile.read()
finally:
    objFile.close()

print text
