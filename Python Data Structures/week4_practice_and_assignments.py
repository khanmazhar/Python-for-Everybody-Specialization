# ALGORITHM: A set of rules or steps used to solve a problem
# DATA STRUCTURES: A particluar way of organizing data in a computer
# abc = 'With three words'
# stuff = abc.split()
# print(stuff)

# for w in stuff:
#     print(w)


# fhand = open('mbox-short.txt')
# for line in fhand:
#     line = line.rstrip()
#     # print(line)
#     if not line.startswith('From '):
#         continue
#     words = line.split()
#     print(words[2])


# fhand = open('mbox-short.txt')
# for line in fhand:
#     line = line.rstrip()
#     if not line.startswith('From '):
#         continue
#     words = line.split()
#     email = words[1]
#     email = email.split('@')
#     uni = email[1]
#     print(uni)


# ASSIGNMENT 8.5: 8.4 Open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split() method. The program should build a list of words. For each word on each line check to see if the word is already in the list and if not append it to the list. When the program completes, sort and print the resulting words in alphabetical order.
# You can download the sample data at http://www.py4e.com/code3/romeo.txt
fname = input("Enter file name: ")
fh = open(fname)
all_words = list()
lst = list()
for line in fh:
    words = line.split()
    all_words += words


for word in all_words:
    if not word in lst:
        lst.append(word)

print(sorted(lst))

# ASSIGNMENT 8.5: Open the file mbox-short.txt and read it line by line. When you find a line that starts with 'From ' like the following line:
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# You will parse the From line using split() and print out the second word in the line (i.e. the entire address of the person who sent the message). Then print out a count at the end.
# Hint: make sure not to include the lines that start with 'From:'. Also look at the last line of the sample output to see how to print the count.
fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

fh = open(fname)
count = 0

for line in fh:
    if line.startswith("From "):
        words = line.split()
        print(words[1])
        count += 1

print("There were", count, "lines in the file with From as the first word")
