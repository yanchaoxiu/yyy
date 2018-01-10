# coding:utf-8
from appium import webdriver
from time import sleep
import unittest


def test11(self):
    try:
        print u"四小建设-新设施入库"
        self.driver.find_element_by_xpath("//*[@text='四小建设']").click()
        sleep(3)
        self.driver.find_element_by_xpath("//*[@text='需求提出']").click()
        sleep(3)
        self.driver.find_element_by_xpath("//*[@text='新设施入库']").click()
        sleep(10)
        acc_1 = 'new UiSelector().description("请选择")'
        self.driver.find_element_by_xpath("//android.widget.ListView/android.view.View[1]/android.view.View[1]/android.view.View[2]").click()
        sleep(3)
        self.driver.find_element_by_xpath("//*[@text='内部测试']").click()
        sleep(3)
        self.driver.tap([(640,236)],100)
        self.driver.find_element_by_xpath("//android.widget.ListView/android.view.View[2]/android.view.View[1]/android.view.View[2]").click()
        sleep(3)
        self.driver.find_element_by_accessibility_id("阿佩营销中心").click()
        sleep(3)
        self.driver.tap([(511,860)],100)
        sleep(3)
        self.driver.find_element_by_xpath\
            ("//android.widget.ListView/android.view.View[3]/android.view.View[1]/android.view.View[2]").click()
        sleep(3)
        self.driver.find_element_by_accessibility_id("小休息室").click()
        sleep(3)
        self.driver.tap([(515,960)],100)
        sleep(2)
        self.driver.find_element_by_xpath\
            ("//android.widget.ListView/android.view.View[4]/android.view.View[1]/android.view.View[2]").click()
        sleep(2)
        self.driver.tap([(580,590)],100)
        sleep(3)
        self.driver.tap([(515,960)],100)
        sleep(2)
        # 品牌
        self.driver.find_element_by_xpath\
            ("//android.widget.ListView/android.view.View[5]/android.view.View[1]/android.view.View[2]").click()
        sleep(2)
        self.driver.tap([(600,725)],100)
        sleep(3)
        self.driver.tap([(515,823)],100)
        sleep(3)
        # 规格
        self.driver.find_element_by_xpath\
            ("//android.widget.ListView/android.view.View[6]/android.view.View[1]/android.view.View[2]").click()
        sleep(3)
        self.driver.tap([(576,725)],100)
        sleep(3)
        self.driver.tap([(510,820)],100)
        sleep(3)
        # 数量
        self.driver.find_element_by_accessibility_id("请输入").click()
        sleep(3)
        loc_15 = 'new UiSelector().className("android.widget.EditText")'
        self.driver.find_element_by_xpath\
            ("//android.view.View[@content-desc=\"台账入库申请\"]/android.view.View[2]/android.widget.EditText[1]").send_keys("1")
        sleep(2)
        self.driver.find_element_by_xpath("//android.view.View/android.widget.EditText[2]").send_keys(u"台")
        sleep(3)
        self.driver.tap([(515,780)],100)
        sleep(3)
        self.driver.find_element_by_xpath\
            ("//android.widget.ListView/android.view.View[8]/android.view.View[1]/android.widget.EditText[1]")\
            .click()
        sleep(3)
        self.driver.find_element_by_accessibility_id("确定").click()
        sleep(3)
        self.driver.find_element_by_xpath("//android.widget.ListView/android.view.View[9]/android.view.View[1]/android.view.View[2]").click()
        sleep(3)
        self.driver.find_element_by_xpath("//*[@text='需要更换']").click()
        sleep(3)
        self.driver.find_element_by_xpath("//android.widget.ListView/android.view.View[10]/android.view.View[1]/android.view.View[2]").click()
        sleep(3)
        self.driver.find_element_by_xpath("//*[@text='工会']").click()
        sleep(3)
        self.driver.find_element_by_xpath("//android.widget.ListView/android.view.View[11]/android.view.View[1]/android.view.View[2]").click()
        sleep(3)
        self.driver.find_element_by_xpath("//*[@text='工会经费']").click()
        sleep(3)
        self.driver.find_element_by_xpath\
            ("//android.widget.ListView/android.view.View[12]/android.view.View[1]/android.widget.EditText[1]").click()
        sleep(3)
        self.driver.find_element_by_accessibility_id("确定").click()
        sleep(3)
        self.driver.find_element_by_xpath\
            ("//android.widget.ListView/android.view.View[13]/android.view.View[1]/android.widget.EditText[1]").send_keys("0")
        sleep(2)
        self.driver.find_element_by_xpath\
            ("//android.widget.ListView/android.view.View[14]/android.view.View[1]/android.widget.EditText[1]").send_keys("1000")
        sleep(3)
        swipeUp(self.driver,n=2)
        sleep(3)
        self.driver.tap([(80,866)],100)
        sleep(2)
        self.driver.find_element_by_id("com.tencent.wework:id/tr").click()
        sleep(2)
        self.driver.find_element_by_id("com.tencent.wework:id/cb7").click()
        sleep(3)
        self.driver.find_element_by_xpath("//android.view.View/android.view.View[2]/android.widget.EditText[1]").send_keys(u"无")
        sleep(2)
        self.driver.tap([(350,1245)],100)
        sleep(8)
        self.driver.tap([(34, 70)], 100)
        sleep(3)
        print "ok"
    except:
        pass

def test12(self):
    print u"新增设施需求"
    self.driver.find_element_by_xpath("//*[@text='需求提出']").click()
    sleep(3)
    self.driver.find_element_by_xpath("//*[@text='新增设施需求']").click()
    sleep(10)
    self.driver.find_element_by_xpath\
        ("//android.widget.ListView/android.view.View[1]/android.view.View[1]/android.view.View[2]").click()
    sleep(3)
    self.driver.find_element_by_xpath("//*[@text='内部测试']").click()
    sleep(3)
    self.driver.find_element_by_xpath\
        ("//android.widget.ListView/android.view.View[2]/android.view.View[1]/android.view.View[2]").click()
    sleep(3)
    self.driver.find_element_by_accessibility_id("阿佩营销中心").click()
    self.driver.tap([(515,855)],100)
    sleep(3)
    # 项目
    self.driver.find_element_by_xpath\
        ("//android.widget.ListView/android.view.View[3]/android.view.View[1]/android.view.View[2]").click()
    sleep(3)
    self.driver.tap([(574,517)],100)
    sleep(3)
    self.driver.tap([(515,960)],100)
    sleep(3)
    # 项目内容
    self.driver.find_element_by_xpath\
        ("//android.widget.ListView/android.view.View[4]/android.view.View[1]/android.view.View[2]").click()
    sleep(3)
    self.driver.tap([(580,590)],100)
    sleep(3)
    self.driver.tap([(515,960)],100)
    sleep(3)
    # 品牌
    self.driver.find_element_by_xpath\
        ("//android.widget.ListView/android.view.View[5]/android.view.View[1]/android.view.View[2]").click()
    sleep(3)
    self.driver.tap([(578,726)],100)
    sleep(3)
    self.driver.tap([(515,821)],100)
    sleep(3)
    # 规格型号
    self.driver.find_element_by_xpath\
        ("//android.widget.ListView/android.view.View[6]/android.view.View[1]/android.view.View[2]").click()
    sleep(3)
    self.driver.tap([(578,726)],100)
    sleep(3)
    self.driver.tap([(515,821)],100)
    sleep(3)
    self.driver.find_element_by_accessibility_id("请输入").click()
    sleep(3)
    self.driver.find_element_by_xpath\
        ("//android.view.View[@content-desc=\"新增需求申请\"]/android.view.View[2]/android.widget.EditText[1]").send_keys("1")
    sleep(3)
    self.driver.find_element_by_xpath("//android.view.View/android.widget.EditText[2]").send_keys(u"台")
    sleep(3)
    self.driver.tap([(515,780)],100)
    sleep(3)
    self.driver.find_element_by_xpath("//android.view.View/android.view.View[1]/android.widget.EditText[1]").send_keys("1000")
    sleep(3)
    self.driver.find_element_by_xpath("//android.view.View/android.view.View[2]/android.widget.EditText[1]").send_keys(u"无")
    sleep(3)
    self.driver.find_element_by_accessibility_id("立即发布").click()
    sleep(8)
    self.driver.tap([(34, 70)], 100)
    sleep(5)
    print "ok"
    self.driver.keyevent(keycode=4)
    sleep(5)

    def test12(self):
        print u"兴趣协会添加成果"
        self.driver.find_element_by_xpath("//*[@text='我的协会']").click()
        sleep(3)
        self.driver.tap([(308,175)],100)
        sleep(5)
        self.driver.find_element_by_xpath("//android.view.View[@content-desc=\"\"]").click()
        sleep(3)
        # 添加活动成果
        self.driver.tap([(630,1056)],100)
        sleep(5)
        self.driver.find_element_by_accessibility_id("请选择").click()
        sleep(3)
        self.driver.find_element_by_xpath("//*[@text='剪纸小活动']").click()
        sleep(3)
        self.driver.find_element_by_class_name("android.widget.EditText").send_keys(u"一等奖")
        sleep(3)
        self.driver.find_element_by_xpath("//android.view.View/android.view.View[2]/android.widget.EditText[1]").send_keys(u"荣获一等奖")
        sleep(3)
        self.driver.find_element_by_accessibility_id("Link").click()
        sleep(3)
        self.driver.find_element_by_id("com.tencent.wework:id/tr").click()
        self.driver.find_element_by_id("com.tencent.wework:id/cb7").click()
        sleep(3)
        self.driver.find_element_by_accessibility_id("立即发布").click()
        sleep(5)
        print "ok"

if __name__ == "__main__":
    unittest.main()
