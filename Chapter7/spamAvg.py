# Use the file name mbox-short.txt as the file name
fname = raw_input("Enter file name: ")
fh = open(fname)

sum = 0
count = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    pos = line.find(":")
    numStr = line[pos+1:].strip()
    try:
        num = float(numStr)
    except:
        continue
    sum += num
    count += 1

fh.close()
print "Average spam confidence:", sum / count
