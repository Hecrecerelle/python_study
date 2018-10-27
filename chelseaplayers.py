from bs4 import BeautifulSoup
from urllib import request
import fileinput

url="https://www.chelseafc.com/zh/teams/first-team?pageTab=players"

headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:62.0) Gecko/20100101 Firefox/62.0'}

page=request.Request(url,headers=headers)
page_info=request.urlopen(page).read().decode('utf-8')

soup=BeautifulSoup(page_info,'html.parser')
FirstName=soup.find_all('span','first-name ng-star-inserted')
LastName=soup.find_all('span','last-name ng-star-inserted')
Number=soup.find_all('span',{"_ngcontent-c37":""},class_=False)
Position=soup.find_all('p','tile__role ng-star-inserted')
Number[0:2]=[]
Number[1:3]=[]
Number[12:13]=[]
Number[-1:-3]=[]
Number[15:17]=[]
Position[1:3]=[]
Position[12:13]=[]
Number[-1:-3]=[]
Position[15:17]=[]
total=-1
try:
    files=open(r'test.txt','w')
    for first in FirstName:
        total=total+1
    for index in range(total):
        name=FirstName[index].string + " " + LastName[index].string + " " + Number[index].string + " " + Position[index].string
        files.write(name + '\n')
finally:
    if files:
        files.close()