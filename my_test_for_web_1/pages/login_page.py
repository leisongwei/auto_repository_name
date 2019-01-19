#-*- coding: utf-8 -*-
from selenium import webdriver
from base.base import Base


class LoginPage(Base):
    loc_user = ('id', 'account')
    loc_password = ('name', 'password')
    loc_submit = ('id', 'submit')
    loc_login_name = ('css selector', '.user-name')

    def send_user(self, user):
        self.sendText(self.loc_user, user)

    def send_password(self, password):
        self.sendText(self.loc_password, password)

    def click_submit(self):
        self.click(self.loc_submit)

    def confirm_alert(self):
        a = self.is_alert_new()
        if a:
            a.accept()

    def get_user_name(self):
        return self.get_text(self.loc_login_name)

    def login(self, user='admin123', password='admin123'):
        self.driver.get('https://leisongwei.5upm.com/user-login.html')
        self.send_user(user)
        self.send_password(password)
        self.click_submit()


if __name__ == '__main__':
    driver = webdriver.Firefox()
    driver.get('https://leisongwei.5upm.com/user-login.html')
    login = LoginPage(driver)
    login.send_user('admin123')
    login.send_password('admin123')
    login.click_submit()
    login.get_user_name()