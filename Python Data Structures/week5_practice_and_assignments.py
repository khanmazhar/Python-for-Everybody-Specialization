# counts = dict()
# names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
# for name in names:
#     if name not in counts:
#         counts[name] = 1
#     else:
#         counts[name] += 1
# print(counts)

# counts = dict()
# names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
# for name in names:
#     counts[name] = counts.get(name, 0)+1
# print(counts)

# counts = dict()
# line = input('Enter a line of text:')
# words = line.split()

# print('Words:', words)

# for word in words:
#     counts[word] = counts.get(word, 0)+1

# for word, count in counts.items():
#     print(word, count)

# COUNTING AND PRINTING NUMBER OF WORDS IN A FILE
count_of_words = dict()
fname = input('Enter filename:')
fhand = open(fname)
for line in fhand:
    words = line.split()
    for word in words:
        count_of_words[word] = count_of_words.get(word, 0)+1

biggest_count = None
biggest_word = None
for word, count in count_of_words.items():
    if biggest_count is None or biggest_count < count:
        biggest_count = count
        biggest_word = word
print(biggest_word, biggest_count)

# ASSIGNMENT 9.4: 9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.
name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

counts = dict()

for line in handle:
    if not line.startswith('From '):
        continue
    words = line.split()
    email = words[1]
    counts[email] = counts.get(email, 0)+1


biggest_count = None
biggest_word = None
for word, count in counts.items():
    if biggest_count is None or biggest_count < count:
        biggest_count = count
        biggest_word = word
print(biggest_word, biggest_count)
