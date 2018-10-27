from bs4 import BeautifulSoup
from urllib import request
import fileinput

url="https://www.chelseafc.com/zh"

headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:62.0) Gecko/20100101 Firefox/62.0'}

page=request.Request(url,headers=headers)
page_info=request.urlopen(page).read().decode('utf-8')

soup=BeautifulSoup(page_info,'html.parser')
titles=soup.find_all('h3','tile__description__heading')

try:
    files=open(r'test.txt','w')
    for title in titles:
        files.write(title.string + '\n')
finally:
    if files:
        files.close()


