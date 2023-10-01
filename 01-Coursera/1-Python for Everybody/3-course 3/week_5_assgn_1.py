import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup
import ssl
# http://py4e-data.dr-chuck.net/comments_1375315.xml
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "http://py4e-data.dr-chuck.net/comments_1375315.xml"
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
stuff=str(soup)

tree = ET.fromstring(stuff)
lst=tree.findall('comments/comment')
numbers=[]
for item in lst:
    numbers.append(int(item.find('count').text))
print(sum(numbers))