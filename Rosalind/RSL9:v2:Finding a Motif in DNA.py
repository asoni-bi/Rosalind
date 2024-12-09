dnaSeq = "GATATATGCATATACTT"
subSeq = "ATAT"

r = 0
while r != -1:
    r = dnaSeq.find(subSeq, r+1)
    print(r+1)
