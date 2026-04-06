import requests
from bs4 import BeautifulSoup
base_url = "https://www.nytimes.com"
r = requests.get(base_url)
soup = BeautifulSoup(r.text, "lxml")

ttl_list = []
title = soup.find_all('a',{'class':'tpl-lbl css-5mgoji'})
print(title)
for row in title:
    ttl_list.append(row.text)
    
print(ttl_list)