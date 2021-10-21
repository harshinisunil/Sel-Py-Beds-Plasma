import csv
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
            time_detail['time'] = val
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
Button=driver.find_element_by_xpath('/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[3]/div[1]/button[1]')
while(True):
    try:
        Button.click()
    except:
        break
outer_list = [['State', 'Dist Name', 'Contact', 'Description', 'Category', 'Updated Time']]
Hosp_Name = driver.find_elements_by_tag_name('strong')
#l = len(Hosp_Name)
l = 5
i = 1
for a in range(l):
    print("loop" + str(a))
    inner_list = ['Telangana']
    Hosp_Name[a].click()
    Hosp_Name1 = Hosp_Name[a].text

    Dist_Name = driver.find_elements_by_xpath("//span[@class = 'm-1 p-1 info-chip badge badge-info']")
    Dist_Name1 = Dist_Name[a].text
    inner_list.append(Dist_Name1)

    phone_Num = driver.find_elements_by_xpath('//tbody/tr/td[1]/p[2]/span[1]')
    #"phone :" is in 0 index & number in 1 index
    phone_Num1 = phone_Num[a].text
    phone_Num2 = phone_Num1.split(": ")[1]
    inner_list.append(phone_Num2)

    Available_beds = driver.find_elements_by_xpath("//*[@id='root']/div/div/div[2]/div[2]/div/div/div/div[2]/div/div/table/tbody/tr/td[3]/span[1]/span")
    Available_beds1 = Available_beds[a].text
    inner_list.append(Available_beds1 + " Bed available in " + Hosp_Name1)
    inner_list.append("Bed")

    Last_Updated = driver.find_elements_by_xpath('//tbody/tr/td[1]/p[1]/span[1]')
    Last_updated1 = Last_Updated[i].text
    getUpdatedTimeStamp(Last_updated1)
    lastTime = convertedTimeStamp()
    inner_list.append(lastTime)

    outer_list.append(inner_list)
    i = i+2
    with open("C:\\Users\\harsh\\Dropbox\\My PC (LAPTOP-0G6HE4M9)\\Desktop\\telanganaupd.csv", 'w', newline='') as CSVfile:
        work = csv.writer(CSVfile, delimiter=',')
        for row in outer_list:
          work.writerow(row)
print(outer_list)
