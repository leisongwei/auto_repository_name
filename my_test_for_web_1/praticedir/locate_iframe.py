# coding:utf-8
from time import sleep
from selenium import webdriver
profile_directory = r'C:\Users\Administrator\AppData\Roaming\Mozilla\Firefox\Profiles\s6qtifzn.default'
profile = webdriver.FirefoxProfile(profile_directory)
driver = webdriver.Firefox(profile)
# driver.get('https://mail.126.com/')
# myframe = driver.find_element_by_css_selector(3)
# driver.switch_to.frame(2)
# driver.find_element_by_css_selector('.j-inputtext.dlemail').send_keys('123456')
# driver.switch_to.default_content()
# print(driver.title)
# try:
#     sleep(2)
#     driver.find_element_by_partial_link_text('你的专业电子邮局')
#     print(driver.title)
# except:
#     driver.quit()

driver.get('http://bj.ganji.com/')
driver.find_element_by_css_selector('.tab-category:nth-child(7) .dd>a:nth-child(1)').click()
all_handle = driver.window_handles
print(all_handle)
driver.close()
driver.switch_to.window(all_handle[1])
a = driver.title
print(a)
