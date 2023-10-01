import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

name=['Priscillia']
for i in range(7):
    url = "http://py4e-data.dr-chuck.net/known_by_"+name[0]+".html"
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    count = 0
    for tag in tags:
        count += 1
        print(count)
        if count == 18:
            # print(re.findall("http.*html",tag))
            print(tag)
            name=[x for x in tag]
            break
    print(i+1,name)

