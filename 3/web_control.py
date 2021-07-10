#Ref = https://youtu.be/wuykkvpedBw
import selenium
from selenium import webdriver
import time
n=input()
driver=webdriver.Chrome()
driver.get("https://marketdata.set.or.th/mkt/sectorquotation.do?sector=SET50&language=th&country=TH")
driver.find_element_by_xpath('//input[@placeholder="E-mail or Username"]').send_keys('test@gmail.com')
driver.find_element_by_xpath('//input[@placeholder="Password"]').send_keys('234234')
driver.find_element_by_xpath('//input[@type="submit"]').submit
data_link_list=[]
for data in driver.find_elements_by_xpath('//table[@class="table-info"]//tbody//tr//td[@style="text-align: left;"]//a')[8:20]:
    data_link=data.get_attribute("href")
    data_link_list.append(data_link)

for link in data_link_list:
    driver.get(link)
    driver.find_elements_by_xpath('//div[@class="row"]//li[@role="tab"]')[1].click()
    driver.find_elements_by_xpath('//div[@class="col-xs-12 col-md-4 text-center"]')[-1].click()
    driver.find_elements_by_xpath('//td[@height="18"]')[-1].click()

while(input("Enter exit for quit script:")!="exit"):
    time.sleep(5)











