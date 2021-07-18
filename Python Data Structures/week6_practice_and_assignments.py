# c = {'a': 10, 'b': 1, 'c': 22}
# tmp = list()
# for k, v in c.items():
#     tmp.append((v, k))

# print(tmp)

# tmp = sorted(tmp, reverse=True)
# print(tmp)

fname = input('Enter file name:')
fhand = open(fname)
counts = dict()

for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0)+1

lst = list()
for k, v in counts.items():
    lst.append((v, k))

lst = sorted(lst, reverse=True)
for v, k in lst[:10]:
    print(v, k)

# THE SHORT WAY
print(sorted([(v, k) for k, v in counts.items()], reverse=True))

# ASSIGNMENT 10.2: Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.
name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

counts = dict()
for line in handle:
    line = line.rstrip()
    if not line.startswith('From '):
        continue
    words = line.split()
    time = words[5]
    hrs = time[:2]
    counts[hrs] = counts.get(hrs, 0)+1

lst = sorted([k, v] for k, v in counts.items())
for k, v in lst:
    print(k, v)
