# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 21:10:57 2019

@author: Keshi Shen
"""

import requests
from bs4 import BeautifulSoup

page = requests.get("https://www.immobiliare.it/agenzie-immobiliari/79365/tft-building/")
soup = BeautifulSoup(page.content, 'html.parser')



tags = soup.find_all('div', class_='listing-item_body--content') 


filename = "soup.txt"
f=open(filename,"w")

headers="Name,Price,Locals,URL,ID"

f.write(headers)

#print(soup)


#print(tags)
for tag in tags:

  Name=tag.a.text.strip()
#Name
  Price=tag.li.text.strip()
#price
  Locals=tag.span.text.strip()
#Locals
  URL=tag.a["href"]
#URL
  ID=tag.a["id"][-8:]
#ID
  
  f.write("\n"+Name + "," +Price+","+Locals+","+URL+","+ID)

f.close()
