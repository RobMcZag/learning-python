fileName = "mbox-short.txt"
fh = open(fileName)

count = 0
for line in fh:
    if not line.startswith("From "): continue
    tokens = line.split()
    print tokens[1]
    count += 1

print "There were " + str(count) + " lines in the file with From as the first word"
