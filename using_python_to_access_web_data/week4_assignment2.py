import urllib.request
import urllib.error
import urllib.parse
from bs4 import BeautifulSoup
import ssl
import re

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

e_url = input('Enter url: ')
e_index = int(input('Enter the link number you want to follow:'))-1
e_repeat = int(
    input('Enter the number of times you want to repeat the process:'))


def findurl(url, e_url):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')

    for i in range(len(tags)):
        if i == e_url:
            new_url = tags[i].get('href', None)
    return new_url


i = 0
while i < e_repeat:
    url = findurl(e_url, e_index)
    e_url = url
    i += 1

name = re.findall('_([A-Z].+)\.', e_url)[0]
print(name)
