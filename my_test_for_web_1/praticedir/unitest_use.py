
from time import sleep

from selenium import webdriver
import unittest


class Test_login(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()

    def setUp(self):
        self.driver.get('https://leisongwei.5upm.com/my/')

    def is_login_success(self):
        try:
            a = self.driver.find_element_by_css_selector('.user-name').text
            print("登录成功，账号：%s"% a)
            return a
        except:
            print('没有登录成功')
            return ''

    def test1(self):
        self.driver.find_element_by_id('account').send_keys('admin123')
        self.driver.find_element_by_name('password').send_keys('admin123')
        self.driver.find_element_by_id('submit').click()
        sleep(3)
        a = self.is_login_success()
        self.assertTrue(a == 'admin123')

    def test2(self):
        self.driver.find_element_by_id('account').send_keys('admin123')
        self.driver.find_element_by_name('password').send_keys('a')
        self.driver.find_element_by_id('submit').click()
        sleep(3)
        a = self.is_login_success()
        self.assertTrue(a == '')

    def tearDown(self):
        sleep(1)
        self.driver.delete_all_cookies()
        self.driver.refresh()
        sleep(1)


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()