from bs4 import BeautifulSoup
import urllib.error
import urllib.parse
import urllib.request
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter url: ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

sum = 0
span_tags = soup.find_all('span')
for tag in span_tags:
    num = int(tag.text)
    sum += num

print('Total Sum:', sum)
