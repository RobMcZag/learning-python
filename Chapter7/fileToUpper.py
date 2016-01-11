# Use words.txt as the file name
fname = raw_input("Enter file name: ")
fh = open(fname)

text = fh.read()

print text.upper().rstrip()
