# coding:utf-8
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
import unittest
import time
import os
import HTMLTestRunner
# from test_01 import Union

# 用例路径
case_path = os.path.join(os.getcwd(), "gonghui")
# 报告存放路径
report_path = os.path.join(os.getcwd(), "report")

def all_case():
    discover = unittest.defaultTestLoader.discover(case_path,pattern="test*.py",top_level_dir=None)
    print(discover)
    return discover
def setUp(self):
    print u"打开登录页面"
    profile_directory = r'C:\Users\Administrator\AppData\Roaming\Mozilla\Firefox\Profiles\geik64xc.default'
    profile = webdriver.FirefoxProfile(profile_directory)
    self.driver = webdriver.Firefox(profile)
    url = "http://etongwang.net:8088/wxgh/admin/index.html"
    self.driver.get(url)
def login(self,username,psw):
    print u"登录"
    # 登录
    self.driver.find_element_by_xpath(".//*[@id='loginForm']/div[1]/input").send_keys(username)
    time.sleep(2)
    self.driver.find_element_by_xpath(".//*[@id='loginForm']/div[2]/input").send_keys(psw)
    time.sleep(2)
    self.driver.find_element_by_xpath(".//*[@id='loginForm']/button").click()
    time.sleep(2)
    # login(u"admin", "123456")
if __name__ == "__main__":
    report_abspath = os.path.join(report_path, "result.html")
fp = open(report_abspath, "wb")
runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title=u'自动化测试报告,测试结果如下：', description=u'用例执行情况：')
runner.run(all_case())
fp.close()
