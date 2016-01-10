text = "X-DSPAM-Confidence:    0.8475";
pos = text.find(":")
numStr = text[pos+1:].strip()
try:
    num = float(numStr)
except:
    print "no number found!"
    quit()
print num