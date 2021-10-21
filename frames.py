

import requests
from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\Program Files\\Google\\Chrome\\Application\\chromedriver.exe")
url = "https://covid.wechaar.com/delhi/oxygen.html"
driver.get(url)

params = ()
airtable_records = []
run = True
while run is True:
  response = requests.get(url, params=params, headers=headers)
  airtable_response = response.json()
  airtable_records += (airtable_response['records'])



