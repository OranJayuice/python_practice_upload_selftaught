import requests
from bs4 import BeautifulSoup

url = "https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture"
headers = {'User-Agent': 'Mozilla/5.0'} 
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

# 文章內容在 class 為 "body__inner-container" 的 div 裡(利用左上的inspecter尋找)
content = soup.find('div', class_='body__inner-container')

# 找出裡面所有的段落 <p>
paragraphs = content.find_all('p')

for p in paragraphs:
    print(p.text)
