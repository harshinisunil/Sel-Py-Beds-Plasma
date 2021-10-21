import datetime
import time

from selenium import webdriver

driver = webdriver.Chrome(executable_path='C:\\Program Files\\Google\\Chrome\\Application\\chromedriver.exe')
driver.get("https://covidtelangana.com")
time_detail = {"time": [], "T": []}
def getUpdatedTimeStamp(lastUpdated):
    values = lastUpdated.split(" ")
    for val in values:
        if val.isdigit():
            time_detail['time']=val
        elif val == 'minutes':
            time_detail['T'] = 0
        elif val == 'hours':
            time_detail['T'] = 1
        elif val == 'months':
            time_detail['T'] = 2

def convertedTimeStamp():
  if time_detail['T']==0:
      return time.time()*1000 - float(time_detail['time'])*60*1000
  elif time_detail['T']==1:
      return time.time()*1000- float(time_detail['time']) *60*60*1000
  else:
      return time.time()*1000 - float(time_detail['time']) *2629743*100

driver.maximize_window()
time.sleep(2)
#Xpath t0 "Load Next 20"
element = driver.find_element_by_xpath('/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[3]/div[1]/button[1]')
while(True):
    try:
        element.click()
    except:
        break

# Plusbutton=driver.find_elements_by_xpath('//tbody/tr[1]/td[1]/div[1]/button[1]/*[1]')
Hosp_Name = driver.find_elements_by_tag_name('strong')
#Dist_Name = driver.find_elements_by_xpath("//span[@class = 'm-1 p-1 info-chip badge badge-info']")
#Address_name=driver.find_elements_by_xpath("//*[@id='root']/div/div/div[2]/div[2]/div/div/div/div[2]/div/div/table/tbody/tr[2]/td/p[4]/span")
#Last_updated = driver.find_elements_by_xpath("//tbody/tr/td/p[1]/span[1]")
Ph_name = driver.find_elements_by_xpath("//tbody/tr/td[1]/p[2]/span[1]")
l1 = len(Hosp_Name)
print(l1)
l=5
for a in range(l):
    Hosp_Name[a].click()
    print(Hosp_Name[a].text)
    Ph_name = driver.find_elements_by_xpath("//tbody/tr/td[1]/p[2]/span[1]")
    phone_Num1 = Ph_name[a].text
    phone_Num2 = phone_Num1.split(": ")[1]
    print(phone_Num2)
    Dist_Name = driver.find_elements_by_xpath("//span[@class = 'm-1 p-1 info-chip badge badge-info']")
    print(Dist_Name[a].text)
    Last_updated = driver.find_elements_by_xpath("//tbody/tr/td[1]/p[1]/span")
    Last_updated1 = Last_updated[a].text
    getUpdatedTimeStamp(Last_updated1)





