#-*- coding: utf-8 -*-
from time import sleep
from selenium import webdriver


class Login():
    def __init__(self, driver):
        self.driver = driver

    def login(self, user='admin123', password='admin123'):
        self.driver.find_element_by_id('account').send_keys(user)
        self.driver.find_element_by_name('password').send_keys(password)
        self.driver.find_element_by_id('submit').click()

    def is_alert(self):
        try:
            sleep(2)
            self.driver.switch_to.alert.accept()
        except:
            return ''

    def get_user_name(self):
        try:
            a = self.driver.find_element_by_css_selector('.user-name').text
            return a
        except:
            return ''

    def is_login_success(self):
        try:
            a = self.driver.find_element_by_css_selector('.user-name').text
            print("登录成功，账号：%s" % a)
            return a
        except:
            print('没有登录成功')
            return ''


if __name__ == '__main__':
    driver = webdriver.Firefox()
    driver.get('https://leisongwei.5upm.com/user-login-Lw==.html')
    a = Login(driver)
    a.login()
    a.is_login_success()
    a.is_alert()