fileName = "mbox-short.txt"
fh = open(fileName)

mailCount = dict()
for line in fh:
    if not line.startswith("From "): continue
    email = line.split()[1]
    mailCount[email] = mailCount.get(email, 0) + 1

maxCount = 0
maxKey = None
for key, value in mailCount.items():
    if value > maxCount:
        maxCount = value
        maxKey = key

print maxKey, maxCount
