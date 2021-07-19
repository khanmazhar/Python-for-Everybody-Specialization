import re

fhand = open('regex_sum_1300637.txt', 'r')
sum = 0
for line in fhand:
    line = line.rstrip()
    numbers = re.findall('[0-9]+', line)
    if len(numbers) > 0:
        numbers = [int(x) for x in numbers]
        for y in numbers:
            sum += y
print(sum)
