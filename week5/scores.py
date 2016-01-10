scoreTxt = raw_input("What's the score? (from 0 to 1)")
try:
    score = float(scoreTxt)
except:
    print "Your text is not a number!"
    quit()

if score > 1:
    print "Score should be between 0 and 1. (" + score + ") is too high!"
elif score >= 0.9:
    print "A"
elif score >= 0.8:
    print "B"
elif score >= 0.7:
    print "C"
elif score >= 0.6:
    print "D"
elif score >= 0 and score < 0.6:
    print "F"
else:
    print "Score should be between 0 and 1. (" + score + ") is too low!"
