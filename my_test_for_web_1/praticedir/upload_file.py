# coding:utf-8
from time import sleep

from pykeyboard import PyKeyboard
from selenium import webdriver
from pages.login_page import LoginPage

driver = webdriver.Firefox()
a = LoginPage(driver)
a.login()
driver.get('https://leisongwei.5upm.com/bug-create-1-0-moduleID=0.html')
sleep(2)
# 点击上传图片文件
driver.find_element_by_css_selector('.ke-toolbar-icon.ke-toolbar-icon-url.ke-icon-image').click()
sleep(2)
# 点击本地上传
driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[2]/div/div[1]/ul/li[2]').click()
# 点击浏览
driver.find_element_by_css_selector('.ke-inline-block.ke-upload-button').click()


k = PyKeyboard()
s = r"‪C:\users\administrator\desktop\11.txt"
for i in s:
    k.tap_key(i)
sleep(1)
k.tap_key(k.enter_key)

