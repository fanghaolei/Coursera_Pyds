#assignment 10.2
name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
time = list()
for line in handle:
    if line.startswith('From '):
        line = line.rstrip().split()[5]
        time.append(line.split(':')[0])       

count = dict()
for hour in time:
    count[hour] = count.get(hour, 0) + 1

nl = sorted(count.items())          
for k, v in nl:
    print k, v
            