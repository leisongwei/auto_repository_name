#-*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait



class Base():
    def __init__(self, driver:webdriver.Firefox):
        self.driver = driver
        self.timeout = 10
        self.t = 0.5

    def findElement(self, loctor):
        ele = WebDriverWait(self.driver, self.timeout, self.t).until(lambda x: x.find_element(*loctor))
        return ele

    def click(self, locator):
        self.findElement(locator).click()

    def sendText(self, locator, text):
        self.findElement(locator).send_keys(text)

    def is_alert(self):
        try:
            return self.driver.switch_to.alert
        except:
            return False

    def is_alert_new(self):
        try:
            return WebDriverWait(self.driver, self.timeout, self.t).until(EC.alert_is_present)
        except:
            return False

    def get_text(self, locator):
        try:
            a = self.findElement(locator).text
            print('获取文本成功，返回文本：%s' % a)
            return a
        except:
            print('获取文本失败，返回空')
            return ''


if __name__ == '__main__':
    driver = webdriver.Firefox()
    driver.get('https://leisongwei.5upm.com/my/')
    a = Base(driver)
    loc1 = (By.ID, 'account')
    a.sendText(loc1,'admin')
    loc2=('id', 'submit')
    a.click(loc2)
