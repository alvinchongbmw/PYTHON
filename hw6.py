text = "X-DSPAM-Confidence:    0.8475";
sempos = text.find(":")
if sempos < 0 :
    print("Error")
elif sempos >= len(text) - 1 :
    print("Error")
else :
    fnumstr = text[sempos+1 : len(text)]
    fnum = float(fnumstr.strip())
    print(fnum)
