# coding:utf-8
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
import unittest
import time

class Union(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print u"打开登录页面"
        profile_directory = r'C:\Users\Administrator\AppData\Roaming\Mozilla\Firefox\Profiles\geik64xc.default'
        profile = webdriver.FirefoxProfile(profile_directory)
        cls.driver = webdriver.Firefox(profile)
        url = "http://etongwang.net:8088/wxgh/admin/index.html"
        cls.driver.get(url)
        print u"登录"
        cls.driver.find_element_by_xpath(".//*[@id='loginForm']/div[1]/input").send_keys("admin")
        time.sleep(2)
        cls.driver.find_element_by_xpath(".//*[@id='loginForm']/div[2]/input").send_keys("123456")
        time.sleep(2)
        cls.driver.find_element_by_xpath(".//*[@id='loginForm']/button").click()
        time.sleep(2)

    try:
        def test_1(self):
            print u"青年部落添加活动"
            # 点击青年部落
            self.driver.find_element_by_xpath(".//*[@id='navbarList']/li[4]/a").click()
            time.sleep(2)
            # 点击活动管理
            self.driver.find_element_by_xpath(".//*[@id='mainPanel']/div[3]/div[1]/h4/a/span[2]").click()
            time.sleep(4)
            # 点击添加活动
            self.driver.find_element_by_xpath(".//*[@id='collapse_2']/ul/li[2]/a").click()
            time.sleep(4)
            # 输入内容
            self.driver.find_element_by_xpath(".//*[@id='uiMain']/div/form/div[1]/div[1]/div/input").send_keys(u"迎春活动")
            time.sleep(2)
            self.driver.find_element_by_xpath(".//*[@id='uiMain']/div/form/div[1]/div[2]/div/input").send_keys("12")
            time.sleep(2)
            js6 = 'document.getElementById("start_datetimepicker").removeAttribute("readonly");'
            self.driver.execute_script(js6)
            js_value = 'document.getElementById("start_datetimepicker").value="2017-12-12 9:00"'
            self.driver.execute_script(js_value)
            time.sleep(2)
            js7 = 'document.getElementById("end_datetimepicker").removeAttribute("readonly");'
            self.driver.execute_script(js7)
            js_1 = 'document.getElementById("end_datetimepicker").value="2017-12-20 17:00"'
            self.driver.execute_script(js_1)
            time.sleep(2)
            # 输入发起人
            self.driver.find_element_by_xpath(".//*[@id='input-show-1']").click()
            time.sleep(2)
            self.driver.find_element_by_id("input-key").send_keys("13527188046")
            time.sleep(2)
            self.driver.find_element_by_xpath(".//*[@id='searchModal']/div/div/div[2]/ul/li[1]").click()
            time.sleep(2)
            # 选择发起人区公司是省公司
            s2 = self.driver.find_element_by_xpath(".//*[@id='uiMain']/div/form/div[3]/div[2]/div/select")
            Select(s2).select_by_index(4)
            time.sleep(2)
            # 添加联系人
            self.driver.find_element_by_xpath(".//*[@id='input-show-2']").click()
            time.sleep(2)
            self.driver.find_element_by_xpath(".//*[@id='input-key']").clear()
            self.driver.find_element_by_xpath(".//*[@id='input-key']").send_keys("13527188046")
            time.sleep(2)
            self.driver.find_element_by_xpath(".//*[@id='searchModal']/div/div/div[2]/ul/li[1]").click()
            time.sleep(2)
            self.driver.find_element_by_xpath(".//*[@id='uiMain']/div/form/div[4]/div[2]/div/input").clear()
            self.driver.find_element_by_xpath(".//*[@id='uiMain']/div/form/div[4]/div[2]/div/input").send_keys("13527188046")
            time.sleep(2)
            self.driver.find_element_by_xpath(".//*[@id='suggestId']").send_keys(u"南方通信大厦")
            time.sleep(2)
            self.driver.find_element_by_xpath(".//*[@id='uiMain']/div/form/div[5]/div/label").click()
            time.sleep(2)
            self.driver.find_element_by_xpath(".//*[@id='uiMain']/div/form/div[7]/div[1]/div/textarea").send_keys(u"欢迎参与")
            time.sleep(2)
            self.driver.find_element_by_xpath(".//*[@id='uploadNewsImg']").send_keys(r"D:\tupian\1.jpg")
            time.sleep(2)
            self.driver.find_element_by_xpath(".//*[@id='uiMain']/div/form/div[8]/div/div/textarea").send_keys(u"无")
            time.sleep(2)
            self.driver.find_element_by_id("btn-add").click()
            time.sleep(4)
            self.driver.find_element_by_xpath("html/body/div[6]/div/div/div[3]/button[1]").click()
            time.sleep(4)
        def test_2(self):
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
            self.driver.find_element_by_xpath("html/body/div[6]/div/div/div[3]/button[1]").click()
    except Exception as msg:
        print(u"异常原因%s"%msg)
        nowTime = time.strftime("%Y%m%d.%H.%M.%S")
        unittest.TestCase.driver.get_screenshot_as_file('%s.jpg' % nowTime)
        raise
        def tearDown(self):
            self.driver.quit()
if __name__ == "__main__":
    unittest.main()

