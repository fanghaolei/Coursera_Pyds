# assignment 8.5
fname = raw_input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
fh = open(fname)
par = list()
count = 0
for line in fh:
  if line.startswith('From:'): 
    par = line.split()
    count = count + 1
  else: continue
  print par[1]
print 'There were', count, 'lines in the file with From as the first word'
