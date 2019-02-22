# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 17:37:19 2019

@author: Sanjay-Sir
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd

r = requests.get("https://www.flipkart.com/search?q=iphone&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_6&otracker1=AS_QueryStore_OrganicAutoSuggest_1_6&as-pos=1&as-type=RECENT&as-searchtext=iphone")
c = r.content

soup = BeautifulSoup(c,"html.parser")

all = soup.find_all("div",{"class":"_1UoZlX"})

all[0].find("div",{"class":"_3wU53n"}).text

l=[]

base_url = "https://www.flipkart.com/search?q=iphone&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_HistoryAutoSuggest_0_6&otracker1=AS_QueryStore_HistoryAutoSuggest_0_6&as-pos=0&as-type=HISTORY&as-searchtext=iphone&page="
for page in range(1,9,1):
    print(base_url+str(page))
    c=r.content
    soup=BeautifulSoup(c,"html.parser")
    all = soup.find_all("div",{"class":"_1UoZlX"})
    print(all)
    for item in all:
        d={}
        d['Phone Name']=item.find("div",{"class":"_3wU53n"}).text
        d["Price"]=item.find("div",{"class":"_1vC4OE _2rQ-NK"}).text.replace("₹","")
        d["Rating"]=item.find("div",{"class":"hGSR34"}).text
        d["ROM Size"]=item.find("ul",{"class":"vFw0gD"}).find_all("li",{"class":"tVe95H"})[0].get_text(strip=True)
        d["Display Specification"]=item.find("ul",{"class":"vFw0gD"}).find_all("li",{"class":"tVe95H"})[1].get_text(strip=True)
        d["Camera Specification"]=item.find("ul",{"class":"vFw0gD"}).find_all("li",{"class":"tVe95H"})[2].get_text(strip=True)
        d["Processor Specification"]=item.find("ul",{"class":"vFw0gD"}).find_all("li",{"class":"tVe95H"})[3].get_text(strip=True)
        
        l.append(d)
        
        print(l)
        len(l)
    
import pandas

df =pandas.DataFrame(l)

df

df.to_csv("F:/4th Blog/phone_data.csv")


#below code is used above for the web page crawling

base_url = "https://www.flipkart.com/search?q=iphone&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_HistoryAutoSuggest_0_6&otracker1=AS_QueryStore_HistoryAutoSuggest_0_6&as-pos=0&as-type=HISTORY&as-searchtext=iphone&page="
for page in range(1,9,1):
    print(base_url+str(page))
    c=r.content
    soup=BeautifulSoup(c,"html.parser")
    all = soup.find_all("div",{"class":"_1UoZlX"})
    print(all)
    