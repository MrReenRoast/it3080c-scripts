import requests, re
from bs4 import BeautifulSoup

data = requests.get("https://www.blippi.gg").content
soup = BeautifulSoup(data, 'lxml')
span = soup.find("h2")
title = span.text
span2 = soup.find("a", {"href":re.compile('^https://dvdv.kim')})
link = span2
print("Here's where to find the " + title + ": " + link.get('href'))
