# assignment 7.2
fname = raw_input("Enter file name: ")
fh = open(fname)
total = 0
count = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    start = line.find('0')
    num = float(line[start:])
    total = total + num
    count = count + 1
avg = total/count
print "Average spam confidence:", avg
