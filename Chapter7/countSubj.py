fname = raw_input("Enter file name:")
try:
    file = open(fname)
except:
    print "File cannot be opened:", fname
    exit()

header = "Subject:"
count = 0
for line in file:
    if line.startswith(header): count += 1

file.close()
print "There were "+ str(count) +" subject lines in " + fname
