import unittest
from common import HTMLTestRunner_cn

pathCase = 'D:\\all_test_dir\\my_test_for_web_1\\case'
rule = 'test*.py'
discover = unittest.defaultTestLoader.discover(start_dir=pathCase,pattern=rule)
print(discover)

report = "D:\\all_test_dir\\my_test_for_web_1\\report\\"+'report.html'
fp = open(report,'wb')
runner = HTMLTestRunner_cn.HTMLTestRunner(stream=fp,title='我日报告',description='好了吧秒速')
runner.run(discover)



