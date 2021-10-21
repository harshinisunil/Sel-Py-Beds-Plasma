import urllib
import urllib.request
from urllib import response

import requests as requests
from bs4 import BeautifulSoup


theurl = "https://covid.wechaar.com/"
thepage = requests.get(theurl)

soup = BeautifulSoup(thepage.content,'html.parser')
#print(soup.prettify())

list = soup.find_all('div', class_='d-flex flex-column vh-50 justify-content-between')
print(list)

list_name = []
for i in range(0, len(list)):
    list_name.append(list[i].get_text())
    print(list_name)








