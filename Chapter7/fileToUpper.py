# Use words.txt as the file name
fname = raw_input("Enter file name: ")
fh = open(fname)

text = fh.read()

fh.close()
print text.upper().rstrip()
