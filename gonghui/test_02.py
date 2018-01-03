# coding:utf-8
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
import unittest
import time

class Union1(unittest.TestCase):
    # def setUp(self):
    #     print u"打开登录页面"
    #     profile_directory = r'C:\Users\Administrator\AppData\Roaming\Mozilla\Firefox\Profiles\geik64xc.default'
    #     profile = webdriver.FirefoxProfile(profile_directory)
    #     self.driver = webdriver.Firefox(profile)
    #     url = "http://etongwang.net:8088/wxgh/admin/index.html"
    #     self.driver.get(url)
    # def login(self,username,psw):
    #     print u"登录"
    #     # 登录
    #     self.driver.find_element_by_xpath(".//*[@id='loginForm']/div[1]/input").send_keys(username)
    #     time.sleep(2)
    #     self.driver.find_element_by_xpath(".//*[@id='loginForm']/div[2]/input").send_keys(psw)
    #     time.sleep(2)
    #     self.driver.find_element_by_xpath(".//*[@id='loginForm']/button").click()
    #     time.sleep(2)
    def test_1(self):
        try:
            print u"添加法律法规"
            # 点击微信公会
            self.driver.find_element_by_xpath(".//*[@id='navbarList']/li[1]/a").click()
            time.sleep(2)
            # 点击工会家园
            self.driver.find_element_by_xpath(".//*[@id='mainPanel']/div[1]/div[1]/h4/a/span[2]").click()
            time.sleep(2)
            # 点击法律法规
            self.driver.find_element_by_xpath(".//*[@id='collapse_0']/ul/li[3]/a").click()
            time.sleep(3)
            # 点击添加法律法规
            js1 = 'document.getElementsByClassName("btn-empty-theme")[1].click();'
            self.driver.execute_script(js1)
            time.sleep(2)
            # 输入信息点击提交
            self.driver.find_element_by_class_name("form-group").click()
            self.driver.find_element_by_class_name("form-control").send_keys("1")
            time.sleep(2)
            self.driver.find_element_by_class_name("edui-editor-body").click()
            self.driver.find_element_by_class_name("edui-body-container").send_keys("2")
            time.sleep(2)
            self.driver.find_element_by_class_name("form-group").click()
            self.driver.find_element_by_xpath(".//*[@id='addForm']/div[3]/input").send_keys("1")
            time.sleep(2)
            self.driver.find_element_by_class_name("form-group").click()
            self.driver.find_element_by_class_name("btn-theme").click()
            time.sleep(3)
            # 弹窗点击确定
            self.driver.find_element_by_xpath("html/body/div[3]/div/div/div[3]/button[1]").click()
        except Exception as msg:
            print(u"异常原因%s"%msg)
            nowTime = time.strftime("%Y%m%d.%H.%M.%S")
            self.driver.get_screenshot_as_file('%s.jpg' % nowTime)
            raise
            def tearDown(self):
                self.driver.quit()

