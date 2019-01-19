# coding: utf-8
from time import sleep

import time

from selenium import webdriver
from case.add_bug_zentao import AddBug
import unittest
from case.login_zentao import Login


class TestAddBug(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get('https://leisongwei.5upm.com/my/')
        self.a = Login(self.driver)
        self.a.login()
        self.b = AddBug(self.driver)

    def test1(self):
        str = time.strftime('%Y_%m_%d_%H_%M_%S')
        title = '标题'+str
        self.b.add_bug(title)
        sleep(2)
        a = self.b.is_add_success(title)
        self.assertTrue(a)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()