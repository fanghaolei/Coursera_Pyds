# assignment 9.4
name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
count = dict()
for line in handle:
  if line.startswith("From:"):
    line = line.rstrip().split()[1]
    count[line] = count.get(line, 0) + 1
bmail = None
bvalue = None
for key, value in count.items():
  if bvalue == None or value > bvalue:
    bmail = key
    bvalue = value
print bmail, bvalue
