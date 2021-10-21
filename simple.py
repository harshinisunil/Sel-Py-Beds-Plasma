import urllib
import urllib.request
from urllib import response

from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome(executable_path="C:\\Program Files\\Google\\Chrome\\Application\\chromedriver.exe")
url = "https://covid.wechaar.com/"
driver.get(url)
#driver.maximize_window()

driver.find_element_by_xpath('//*[@id="listItems"]/li[1]/a/button').click()
Oxygen = driver.find_element_by_xpath("/html/body/div/div/div[1]/a").click()
page = driver.find_elements_by_xpath('//*[@id="view"]/div/div[1]/div[2]/div[1]/div[2]/div')
soup = BeautifulSoup(page.content, 'html.parser').text
list = soup.find_all('iframe', class_='desktop-view')

#list = driver.find_element_by_xp('//*[@id="view"]/div/div[1]/div[2]/div[1]/div[2]')
#print(len(list))

list_name = []
for i in range(0, len(list)):
    list_name.append(list[i].get_text())
    print(list_name)

