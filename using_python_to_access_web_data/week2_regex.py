# ^  -> Matches the beginning of a line
# $  -> Matches the end of the line
# .  -> Matches any character
# \s -> Matches whitespace
# \S -> Matches any non-whitespace character
# *  -> Repeats a character zero or more times
# *? -> Repeats a character zero or more times(non-greedy)
# +  -> Repeats a character one or more times
# +? -> Repeats a character one or more times (non-greedy)
# [aeiou] -> Matches a single character in the listed set
# [^XYZ] -> Matches a  single character not in the listed set
# [a-z0-1] -> The set of character can include a range
# (  -> Indicates where string extraction is to start
# ) -> Indicates where sting extraction is to end

# USING re.search() Like find()

# hand = open('mbox-short.txt')
# for line in hand:
#     line = line.strip()
#     if line.find('From:') >= 0:
#         print(line)

# import re
# hand = open('mbox-short.txt')
# for line in hand:
#     line = line.strip()
#     if re.search('From:', line):
#         print(line)

# for line in hand:
#     line = line.rstrip()
#     if re.search('^X.*:', line):
#         print(line)

# for line in hand:
#     line = line.rstrip()
#     if re.search('^X-\S+:', line):
#         print(line)

import re
# x = 'my 2 fAvourite numbers are 19 and 42'
# y = re.findall('[0-9]+', x)
# print(y)

# y = re.findall('[AEIOU]+', x)
# print(y)

# x = 'From: Using the : character'
# y = re.findall('^F.+?:', x)
# print(y)

fhand = open('mbox-short.txt')
# for line in fhand:
#     line = line.rstrip()
#     email = re.findall('[a-z]\S+@\S+', line)
#     if len(email) > 0:
#         print(email)

for line in fhand:
    line = line.rstrip()
    email = re.findall('\S+?@\S+', line)
    if len(email) > 0:
        print(email)

# for line in fhand:
#     line = line.rstrip()
#     uni = re.findall('^From .*@([^ ]*)', line)
#     if len(uni) > 0:
#         print(uni)

# CALCULATING SPAM CONFIDENCE
# numlist = list()
# for line in fhand:
#     line = line.rstrip()
#     spam = re.findall('^X-DSPAM-Confidence: ([0-9.]+)', line)
#     if len(spam) != 1:
#         continue
#     spam = float(spam[0])
#     numlist.append(spam)

# print(numlist)

# ESCAPE CHARACTER
# x = 'we just received $10.00 for cookies.'
# y = re.findall('\$[0-9.]+', x)
# print(y)
