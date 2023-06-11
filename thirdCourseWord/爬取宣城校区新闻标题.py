import random, time, re
import requests
import pandas as pd
from bs4 import BeautifulSoup 

url='http://xc.hfut.edu.cn/1955/list.htm'
req = requests.get(url)

req.encoding = 'utf-8'
#print(req.text)
html = req.text

with open(r'd:\simdata\titlenews.txt', 'w', encoding  = 'utf-8') as f:
    f.write(html)

#print(html)

soup = BeautifulSoup(html,'html.parser')
lst = []
#s = soup.find_all('span', class_= "news_title")
s = soup.find_all('span', attrs={'class':'news_title'})
for i in s:
   lst.append(i.a.string)

print(lst)
