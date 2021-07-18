fhand = open('mbox-short.txt', 'r')
print(fhand)

count = 0
for line in fhand:
    count += 1
print("Count:", count)

# using the .read() function
fhand = open('mbox-short.txt', 'r')

file = fhand.read()
print(file)

#searching and printing
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if line.startswith('From:'):
        print(line)

fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if not '@uct.ac.za' in line:
        continue
    print(line)


# take input file name and print it
fname = input("Enter file name: ")

try:
    fhand = open(fname)
except:
    print("Invalid file name!")
    quit()

for line in fhand:
    line = line.rstrip()
    if not line.startswith('From:'):
        continue
    print(line)

# ASSIGNMENT 7.1: Write a program that prompts for a file name, then opens that file and reads through the file, and print the contents of the file in upper case. Use the file words.txt to produce the output below.
# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)

for line in fh:
    line = line.upper().rstrip()
    print(line)

# ASSIGNMENT 7.2: 7.2 Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
# X-DSPAM-Confidence:    0.8475
# Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below. Do not use the sum() function or a variable named sum in your solution.
# You can download the sample data at http://www.py4e.com/code3/mbox-short.txt when you are testing below enter mbox-short.txt as the file name.
# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
total = 0
count = 0
for line in fh:
    if line.startswith("X-DSPAM-Confidence:"):
        index = line.find(":") + 1
        total += float(line[index:].strip())
        count += 1

avg = total / count
print("Average spam confidence:", avg)
