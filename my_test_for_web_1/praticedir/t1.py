from time import sleep
from selenium import webdriver
driver = webdriver.Firefox()
driver.get('https://www.baidu.com')
a = driver.find_element_by_xpath('html/body/div[1]/div[1]/div/div[3]/a[8]').text
b = driver.find_element_by_xpath('html/body/div[1]/div[1]/div/div[3]/a[8]').get_attribute('name')
print(a, b)