import requests, re
from bs4 import BeautifulSoup

r = requests.get("http://webscraper.io/test-sites/e-commerce/allinone/phones").content
soup = BeautifulSoup(r, "lxml")
tags = soup.findAll("div", {"class":re.compile('(ratings)')})
for p in tags:
    a = p.findALL("p",{"class":"pull-right"})
    print (a[0].string)