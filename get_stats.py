#!/usr/bin/env python3

from bs4 import BeautifulSoup
import re
import requests
import sys

id = sys.argv[1]

url = "http://archive.org/details/{0}".format(id)
response = requests.get(url)
html = response.text
soup = BeautifulSoup(html)
views = soup.find(text=re.compile("Views")).parent.parent
elems = [x for x in views.contents if x != "\n"]

for elem in elems: 
    if 'boxy-label' in elem.attrs['class'] and 'stealth' not in elem.attrs['class']:
        print("{0} has been viewed {1} times".format(id, elem.text))
