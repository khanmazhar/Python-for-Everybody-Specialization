# import xml.etree.ElementTree as ET

# data = '''
#     <person>
#         <name>Chuck</name>
#         <phone type='intl'>+92 315 9813580</phone>
#         <email hide='yes' />
#     </person>
# '''

# tree = ET.fromstring(data)
# print("Name:", tree.find('name').text)
# print("Phone:", tree.find('phone').text)
# print("Hide email: ", tree.find('email').get('hide'))

# import xml.etree.ElementTree as ET

# input = '''
# <stuff>
#   <users>
#     <user x="2">
#       <id>001</id>
#       <name>Chuck</name>
#     </user>
#     <user x="7">
#       <id>009</id>
#       <name>Brent</name>
#     </user>
#   </users>
# </stuff>'''

# stuff = ET.fromstring(input)
# lst_users = stuff.findall('users/user')

# for user in lst_users:
#     print("Name:", user.find('name').text)
#     print('ID:', user.find('id').text)
#     print('X value:', user.get('x'))


# ASSIGNMENT

import xml.etree.ElementTree as ET
import urllib.parse
import urllib.request
import urllib.error
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter url:')
response = urllib.request.urlopen(url, context=ctx).read()
xml = ET.fromstring(response)

lst_count = xml.findall('.//count')

sum = 0

for count in lst_count:
    sum += int(count.text)

print(sum)
