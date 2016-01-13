DEFAULT_FILE = "../Chapter8/romeo.txt"
fileName = raw_input("Enter file name [" + DEFAULT_FILE + "]:")
if len(fileName) < 1 : fileName = DEFAULT_FILE

DEFAULT_NUM = 5
num = raw_input("Enter number for Top selection [" + str(DEFAULT_NUM) + "]:")
if len(num) < 1 : num = DEFAULT_NUM
else:
    try: num = int(num)
    except: num = DEFAULT_NUM


fh = open(fileName)

wordFreq = dict()
for line in fh:
    words = line.split()
    for w in words:
        word = w.lower()
        wordFreq[word] = wordFreq.get(word, 0) + 1

byWord = sorted(wordFreq.items())
print "Sorted by word\n", byWord, "\n"

byFreq = sorted([ (count, wrd) for wrd,count in wordFreq.items()], reverse=True)
print "Top", num, "sorted by frequency\n",byFreq[:num], "\n"
