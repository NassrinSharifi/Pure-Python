import json
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
url = "http://py4e-data.dr-chuck.net/comments_1375316.json"
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
stuff=str(soup)
# print(stuff)

info = json.loads(stuff)
# print(info)
print('User count:', len(info))

numbers=[]
for item in info["comments"]:
        numbers.append(int(item['count']))
print(sum(numbers))

