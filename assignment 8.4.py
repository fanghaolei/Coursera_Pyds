# 8.4
fname = raw_input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
  words = list()
  words = line.split()
  for word in words:
    if not word in lst: lst.append(word)
    else: continue
print sorted(lst)
