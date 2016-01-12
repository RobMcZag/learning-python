fileName = "romeo.txt"
fh = open(fileName)

wordSet = list()
for line in fh:
    words = line.split()
    for word in words:
        if (word not in wordSet): wordSet.append(word)

sortedWS = wordSet[:]
sortedWS.sort()

print sortedWS
