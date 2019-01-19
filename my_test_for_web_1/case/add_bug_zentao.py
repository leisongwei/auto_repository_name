# coding: utf-8
from time import sleep

import time

from selenium import webdriver
from case.login_zentao import Login
from base.base import Base


class AddBug(Base):

    loc_test = ('css selector', '#navbar>.nav.nav-default>li:nth-child(4)>a')
    loc_bug = ('css selector', '[data-id="bug"]>a')
    loc_add_bug = ('css selector', '.btn.btn-primary>.icon.icon-plus')

    loc_version = ('css selector', '#openedBuild_chosen>.chosen-choices')
    loc_version_add = ('css selector', '.active-result')
    loc_title = ('id', 'title')
    # 需要切换iframe
    loc_body = ('class name', 'article-content')
    loc_submit = ('id', 'submit')

    # loc_bug_name = ('xpath', "/html/body/main/div/div[3]/div[2]/form/div[2]/table/tbody/tr[1]/td[5]/span")
    loc_bug_name1 = ('xpath', "/html/body/main/div/div[3]/div[2]/form/div[2]/table/tbody/tr[1]/td[3]/a")

    def add_bug(self, title='title'):

        self.click(self.loc_test)
        self.click(self.loc_bug)
        self.click(self.loc_add_bug)
        self.click(self.loc_version)
        self.click(self.loc_version_add)
        self.sendText(self.loc_title, title)
        sleep(2)
        self.driver.switch_to.frame(1)
        self.sendText(self.loc_body, '一二三呢女')
        self.driver.switch_to.default_content()
        self.click(self.loc_submit)

    def is_add_success(self, title):

            # a = self.findElement(self.loc_bug_name).get_attribute('class')
            # b = self.findElement(self.loc_bug_name).text
            # a1 = self.findElement(self.loc_bug_name1).get_attribute('class')
            b1 = self.findElement(self.loc_bug_name1).text
            print(b1)
            # print(a, b)
            # print(a1,b1)
            if title == b1:
                return True
            else:
                return False




if __name__ == '__main__':
    profile_directory=r'C:\Users\Administrator\AppData\Roaming\Mozilla\Firefox\Profiles\s6qtifzn.default'
    profile = webdriver.FirefoxProfile(profile_directory)
    driver = webdriver.Firefox()

    driver.get('https://leisongwei.5upm.com/user-login-Lw==.html')
    LOGIN = Login(driver)
    LOGIN.login()
    a = AddBug(driver)
    strTime = time.strftime('%Y_%m_%d_%H_%M_%S')
    title = '测试bug' + strTime
    a.add_bug(title)
    sleep(2)
    b =a.is_add_success(title)
    print(b)


