import urllib.request
import urllib.error
import urllib.parse
import re
# fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

# counts = dict()

# for line in fhand:
#     words = line.decode().split()
#     for word in line:
#         counts = counts.get(word, 0)+1

# print(counts)

fhand = urllib.request.urlopen('http://www.dr-chuck.com/page1.htm')
link = ''
for line in fhand:
    line = line.decode().strip()
    link = re.findall('http.*\.[a-zA-Z]*', line)
    if len(link) > 0:
        print(link)
