# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 19:23:07 2019

@author: clintonngan
"""

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
# Import your functions
import requests
from bs4 import BeautifulSoup

# Put in your variables and urls
# Create crawler
site = 'https://www.facebook.com'
links_found = []
def crawl_page(page, links_found):
    response = requests.get('http://facebook.com')
    soup = BeautifulSoup(response.content, 'html.parser')
    print('link,name')
    for link in soup.find_all('a'):
        href = link.get('href') or ''
        if href.startswith('/'):
            href = site + href
        print(','.join([href, link.get_text() or '']))
        if href not in links_found:
            links_found.append(href)
            crawl_page(href, links_found)

crawl_page(site, links_found)

# print(soup.prettify())
# print(soup.title.string)
# print(soup.find_all('a'))

# Print all link contents
print('link,name')
for link in soup.find_all('a'):
    print(','.join([link.get('href'), link.get_text()]))
    


for link in soup.find_all('a'):
    print(link.get('href'))
print([link.get('href'), link.get('class')[0], link.get_text()])

