fileName = raw_input("Enter file:")
if len(fileName) < 1 : fileName = "../Chapter8/romeo.txt"
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
print "Sorted by frequency\n",byFreq, "\n"
