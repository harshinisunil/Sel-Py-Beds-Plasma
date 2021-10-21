from idlelib import window

from selenium import webdriver
import time
import pandas as pd


driver = webdriver.Chrome(executable_path="C:\\Program Files\\Google\\Chrome\\Application\\chromedriver.exe")
url = "https://covid.wechaar.com/"
driver.get(url)
#driver.maximize_window()

driver.find_element_by_xpath('//*[@id="listItems"]/li[1]/a/button').click()
Oxygen = driver.find_element_by_xpath("/html/body/div/div/div[1]/a").click()
time.sleep(2)
list= driver.find_elements_by_css_selector(".https://airtable.com/embed/shrvBF1I4rURyzalS?backgroundColor=blue&viewControls=on")


