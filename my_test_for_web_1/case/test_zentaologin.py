import ddt
from time import sleep
import xlrd
from selenium import webdriver
import unittest
from pages.login_page import LoginPage
from common.read_excel import ExcelUtil


path = xlrd .open_workbook('D:\\all_test_dir\\my_test_for_web_1\\common\\databases.xls')
datas = ExcelUtil(path)
testdatas = datas.dict_data()


@ddt.ddt
class Test_login(unittest.TestCase):
    def login_case(self, user, password, expect):
        self.login.send_user(user)
        self.login.send_password(password)
        self.login.click_submit()
        result = self.login.get_user_name()
        print(result)
        self.assertTrue(result == expect)

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.login = LoginPage(cls.driver)

    def setUp(self):
        self.driver.get('https://leisongwei.5upm.com/my/')

    @ddt.data(*testdatas)
    def test1(self,data):
        self.login_case(data['user'],data['password'], data['expect'])

    def tearDown(self):
        sleep(1)
        self.login.is_alert()
        self.driver.delete_all_cookies()
        sleep(1)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()