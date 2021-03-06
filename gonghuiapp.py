# coding:utf-8
from appium import webdriver
from time import sleep
import unittest


def swipeUp(driver, t=500, n=1):
    l = driver.get_window_size()
    x1 = l['width'] * 0.5
    y1 = l['height'] * 0.75
    y2 = l['height'] * 0.25
    for i in range(n):
        driver.swipe(x1, y1, x1, y2, t)

def swipeDown(driver, t=500, n=1):
    l = driver.get_window_size()
    x1 = l['width'] * 0.5
    y1 = l['height'] * 0.25
    y2 = l['height'] * 0.75
    for i in range(n):
        driver.swipe(x1, y1, x1, y2, t)


class Union_app(unittest.TestCase):
    desired_caps = {
        'platformName': 'Android',
        'deviceName': '127.0.0.1:62001',
        'platformVersion': '4.4.2',
        'appPackage': 'com.tencent.wework',
        'appActivity': 'com.tencent.wework.launch.LaunchSplashActivity',
        'noReset': 'true',
        'resetKeyboard': 'true',
        'unicodeKeyboard': 'true'
    }
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    sleep(20)
    driver.find_element_by_xpath("//*[@text='工作台']").click()
    sleep(2)
# driver.find_element_by_name(u"工作台").click()
# sleep(2)
# driver.find_element_by_name(u"工会家园").click()
# sleep(2)
# driver.find_element_by_id("com.tencent.wework:id/b6s").click()
# sleep(2)
# driver.find_element_by_id("com.tencent.wework:id/zr").click()
# sleep(5)
# driver.find_element_by_accessibility_id("Link").click()
# sleep(3)
# driver.find_element_by_accessibility_id(u"- 选择 -").click()
# sleep(3)
# driver.find_element_by_name(u"日常工作").click()
# sleep(3)
# driver.find_element_by_class_name("android.widget.EditText").send_keys("123")
# sleep(3)
# driver.find_element_by_xpath("//*[@class='android.view.View'][5]").send_keys("567")
# sleep(3)
# driver.find_element_by_accessibility_id(u"立即发布").click()
# sleep(5)
# driver.find_element_by_accessibility_id(u"关闭页面  Link").click()

# # 发布投票
# driver.find_element_by_name(u"投票").click()
# sleep(8)
# driver.find_element_by_accessibility_id(u" Link").click()
# sleep(3)
# driver.find_element_by_class_name("android.widget.EditText").send_keys(u"语文还是数学")
# sleep(3)
# driver.find_element_by_accessibility_id(u"选择投票开始时间").click()
# sleep(2)
# driver.swipe(360,1272,360,1208)
# sleep(2)
# driver.swipe(535,1272,535,1208)
# sleep(2)
# driver.swipe(711,1272,711,1208)
# sleep(2)
# driver.tap([(650,886),(700,920)],500)
# sleep(2)
# driver.find_element_by_accessibility_id(u"选择投票结束时间").click()
# sleep(2)
# driver.swipe(360,1272,360,1208)
# sleep(2)
# driver.swipe(535,1272,535,1208)
# sleep(2)
# driver.swipe(711,1272,711,1208)
# sleep(2)
# driver.tap([(650,886),(700,920)],500)
# sleep(5)
# driver.find_element_by_xpath("//android.view.View[@content-desc=\"发布投票\"]/android.widget.EditText[1]").send_keys(u"语文")
# sleep(2)
# driver.find_element_by_xpath("//android.view.View[@content-desc=\"发布投票\"]/android.widget.EditText[2]").send_keys(u"数学")
# sleep(2)
# driver.find_element_by_accessibility_id(u"发布").click()
# sleep(3)
# driver.find_element_by_accessibility_id(u"关闭页面  Link").click()

# # 业务申办活动经费申请
# driver.find_element_by_name(u"业务申办").click()
# sleep(2)
# driver.find_element_by_name(u"活动经费申请").click()
# sleep(2)
# driver.find_element_by_class_name("android.widget.EditText").send_keys(u"圣诞节活动")
# sleep(2)
# driver.find_element_by_accessibility_id(u"请选择时间").click()
# sleep(2)
# driver.swipe(360,1272,360,1208)
# sleep(2)
# driver.swipe(535,1272,535,1208)
# sleep(2)
# driver.swipe(711,1272,711,1208)
# sleep(2)
# driver.tap([(650,886),(700,920)],500)
# sleep(5)
# driver.find_element_by_xpath("//android.view.View[@content-desc=\"活动申请\"]/android.widget.EditText[2]").send_keys("12")
# sleep(2)
# driver.find_element_by_xpath("//android.view.View[@content-desc=\"活动申请\"]/android.widget.EditText[3]").send_keys("1500")
# sleep(3)
# driver.find_element_by_xpath("//android.view.View[@content-desc=\"活动申请\"]/android.widget.EditText[4]").send_keys("13527188046")
# sleep(2)
# driver.find_element_by_xpath("//android.view.View[@content-desc=\"活动申请\"]/android.view.View[7]/android.widget.EditText[1]").send_keys(u"华景新城")
# sleep(2)
# driver.find_element_by_xpath("//android.view.View[@content-desc=\"活动申请\"]/android.view.View[9]/android.widget.EditText[1]").send_keys(u"才艺表演和抽奖")
# sleep(2)
# driver.find_element_by_xpath("//android.view.View[@content-desc=\"活动申请\"]/android.view.View[11]/android.widget.EditText[1]").send_keys(u"因为没有钱")
# sleep(2)
# driver.find_element_by_accessibility_id(u"立即申请").click()
# sleep(3)
# driver.find_element_by_accessibility_id(u"关闭页面  Link").click()

# # 工会家园互助资金申请
# driver.find_element_by_name(u"业务申办").click()
# sleep(2)
# driver.find_element_by_name(u"互助资金申请").click()
# sleep(8)
# loc_1 = 'new UiSelector().className("android.widget.EditText")'
# driver.find_elements_by_android_uiautomator(loc_1)[1].send_keys("13527188046")
# sleep(3)
# driver.find_element_by_accessibility_id(u"请选择").click()
# sleep(2)
# driver.find_element_by_name(u"疾病资助").click()
# sleep(2)
# loc_2 = 'new UiSelector().className("android.widget.EditText")'
# driver.find_elements_by_android_uiautomator(loc_2)[2].send_keys("500")
# sleep(2)
# loc_3 = 'new UiSelector().className("android.widget.EditText")'
# driver.find_elements_by_android_uiautomator(loc_3)[3].send_keys("123")
# sleep(3)
# driver.find_element_by_accessibility_id(u"下一步").click()
# sleep(3)
# driver.find_element_by_class_name("android.widget.EditText").send_keys(u"南医三院")
# sleep(3)
# driver.find_element_by_accessibility_id(u"选择就诊时间").click()
# sleep(3)
# driver.swipe(596,1126,596,1040)
# sleep(2)
# driver.tap([(650,886),(700,920)],500)
# sleep(2)
# driver.find_element_by_accessibility_id(u"选择疾病类别").click()
# sleep(2)
# driver.swipe(542,1128,542,1076)
# sleep(2)
# driver.tap([(650,937),(700,960)],500)
# sleep(2)
# driver.find_element_by_accessibility_id(u"提交").click()
# sleep(3)
# driver.find_element_by_accessibility_id(u"关闭页面  Link").click()

# # 热点论坛发布
# driver.find_element_by_name(u"工作台").click()
# sleep(2)
# swipeUp(driver, n=2)
# sleep(2)
# driver.find_element_by_name(u"热点论坛").click()
# sleep(10)
# driver.find_element_by_xpath("//android.view.View[@content-desc=\"热点论坛\"]/android.view.View[2]/android.widget.Image[1]").click()
# sleep(3)
# driver.find_element_by_class_name("android.widget.EditText").send_keys(u"认真")
# sleep(3)
# loc_4 = 'new UiSelector().className("android.widget.EditText")'
# driver.find_elements_by_android_uiautomator(loc_4)[1].send_keys(u"认真是一种什么状态")
# sleep(3)
# driver.find_element_by_accessibility_id("Link").click()
# sleep(3)
# driver.find_element_by_id("com.tencent.wework:id/tr").click()
# sleep(2)
# driver.find_element_by_id("com.tencent.wework:id/cb7").click()
# sleep(2)
# driver.find_element_by_accessibility_id(u"立即发布").click()

# # 添加比赛（模拟器上不能选择时间，时间选择显示不正常）
# driver.find_element_by_name(u"工作台").click()
# sleep(3)
# driver.find_element_by_name(u"比赛").click()
# sleep(3)
# driver.find_element_by_name(u"赛事添加").click()
# sleep(5)
# loc_8 = 'new UiSelector().className("android.widget.Image")'
# driver.find_elements_by_android_uiautomator(loc_8)[0].click()
# sleep(6)
# driver.find_element_by_id("com.tencent.wework:id/tq").click()
# sleep(3)
# driver.find_element_by_name(u"确定").click()
# sleep(3)
# driver.find_element_by_class_name("android.widget.EditText").send_keys(u"篮球比赛")
# sleep(3)
# driver.find_element_by_accessibility_id(u"请选择").click()
# sleep(3)
# driver.find_element_by_name(u"篮球").click()
# sleep(3)
# loc_5 = 'new UiSelector().className("android.widget.EditText")'
# driver.find_elements_by_android_uiautomator(loc_5)[1].send_keys(u"篮球比赛在下周一进行")
# sleep(3)
# loc_6 = 'new UiSelector().className("android.widget.EditText")'
# driver.find_elements_by_android_uiautomator(loc_6)[2].send_keys("13527188046")
# sleep(3)
# loc_7 = 'new UiSelector().className("android.widget.EditText")'
# driver.find_elements_by_android_uiautomator(loc_7)[3].click()
# sleep(3)
# driver.find_element_by_accessibility_id("29 Link").click()
# sleep(3)
# driver.find_element_by_accessibility_id(u"确定").click()
# sleep(3)


# # 添加大型活动
# driver.find_element_by_name(u"工作台").click()
# sleep(3)
# driver.find_element_by_name(u"大型活动").click()
# sleep(3)
# driver.find_element_by_accessibility_id(" Link").click()
# sleep(3)
# swipeUp(driver,n=2)
# sleep(3)
# driver.tap([(348,1143)],100)
# sleep(6)
# driver.find_element_by_xpath("//android.view.View[@content-desc=\"Link\"]").click()
# sleep(3)
# driver.find_element_by_id("com.tencent.wework:id/tr").click()
# sleep(3)
# driver.find_element_by_id("com.tencent.wework:id/cb7").click()
# sleep(3)
# driver.find_element_by_class_name("android.widget.EditText").send_keys(u"奥利匹克")
# sleep(3)
# loc_9 = 'new UiSelector().className("android.widget.EditText")'
# driver.find_elements_by_android_uiautomator(loc_9)[1].send_keys("https://baike.baidu.com/item/%E5%A5%A5%E6%9E%97%E5%8C%B9%E5%85%8B/823095?fr=aladdin")
# sleep(3)
# loc_10 = 'new UiSelector().className("android.widget.EditText")'
# driver.find_elements_by_android_uiautomator(loc_10)[2].send_keys(u"无")
# sleep(3)
# driver.find_element_by_accessibility_id(u"立即发布").click()
# sleep(5)
# driver.find_element_by_accessibility_id(u"关闭页面  Link").click()

# # 大型活动添加常规活动，已将name定位更改为xpath 定位
# driver.find_element_by_xpath(u"//*[@text='工作台']").click()
# sleep(3)
# driver.find_element_by_xpath(u"//*[@text='大型活动']").click()
# sleep(10)
# driver.find_element_by_accessibility_id(" Link").click()
# sleep(3)
# driver.tap([(348,1070)],100)
# sleep(6)
# driver.find_element_by_accessibility_id("Link").click()
# sleep(3)
# driver.find_element_by_id("com.tencent.wework:id/tr").click()
# sleep(3)
# driver.find_element_by_id("com.tencent.wework:id/cb7").click()
# sleep(3)
# sleep(3)
# driver.find_element_by_class_name("android.widget.EditText").send_keys(u"拔河比赛")
# sleep(3)
# loc_11 = 'new UiSelector().className("android.widget.EditText")'
# driver.find_elements_by_android_uiautomator(loc_11)[1].send_keys("13527188046")
# sleep(3)
# driver.find_elements_by_android_uiautomator(loc_11)[2].click()
# driver.keyevent(keycode=16)
# sleep(3)
# driver.find_element_by_accessibility_id(u"选择时间").click()
# sleep(3)
# driver.swipe(369,1133,369,1037)
# sleep(3)
# driver.tap([(654,890),(365,917)],500)
# sleep(3)
# driver.find_element_by_xpath\
#     ("//android.view.View[@content-desc=\"活动发布\"]/android.widget.ListView[3]"
#      "/android.view.View[2]/android.view.View[2]").click()
# sleep(3)
# driver.swipe(358,1130,358,992)
# sleep(3)
# driver.tap([(654,890),(365,917)],500)
# sleep(3)
# driver.find_element_by_accessibility_id(u"活动地点选择地点 Link").click()
# sleep(16)
# driver.tap([(636,597)],100)
# sleep(6)
# driver.tap([(356,1238)],100)
# sleep(5)
# driver.find_element_by_xpath\
#     ("//android.widget.ListView/android.view.View[2]/android.view.View[2]/android.widget.EditText[1]").send_keys(u"无")
# sleep(3)
# swipeUp(driver,n=2)
# sleep(3)
# driver.tap([(629,954)],100)
# sleep(3)
# driver.find_element_by_xpath(u"//*[@text='有积分']").click()
# sleep(3)
# driver.find_element_by_accessibility_id(u"积分规则选择规则 Link").click()
# sleep(5)
# driver.tap([(193,453)],100)
# sleep(3)
# # driver.tap([(13,1213),(705,1270)],500)
# driver.tap([(356,1238)],100)
# sleep(3)
# driver.find_element_by_xpath\
#     ("//android.widget.ListView/android.view.View[1]/android.view.View[2]/android.widget.EditText[1]")\
#     .send_keys(u"活动没介绍")
# sleep(5)
# driver.find_element_by_accessibility_id(u"立即发布").click()
# sleep(8)
# driver.find_element_by_accessibility_id(u"关闭页面  Link").click()

# # 岗位创新
# driver.find_element_by_xpath("//*[@text='工作台']").click()
# sleep(3)
# driver.find_element_by_xpath("//*[@text='岗位创新']").click()
# sleep(3)
# driver.find_element_by_accessibility_id(" 申报创新项目 Link").click()
# sleep(3)
# driver.find_element_by_accessibility_id("创新建议").click()
# sleep(3)
# driver.find_element_by_accessibility_id("选择建议类别").click()
# sleep(3)
# driver.find_element_by_xpath("//*[@text='技能']").click()
# sleep(3)
# driver.find_element_by_class_name("android.widget.EditText").send_keys(u"技术创新")
# sleep(3)
# loc_12 = 'new UiSelector().className("android.widget.EditText")'
# driver.find_elements_by_android_uiautomator(loc_12)[1].send_keys(u"啥标题")
# sleep(3)
# driver.find_element_by_accessibility_id("提交").click()
# sleep(5)
# driver.find_element_by_accessibility_id(u"关闭页面  Link").click()

# # 岗位创新工作坊添加劳模工作室
# driver.find_element_by_accessibility_id("工作坊").click()
# sleep(3)
# loc_13 = 'new UiSelector().className("android.widget.EditText")'
# driver.find_elements_by_android_uiautomator(loc_13)[0].send_keys(u"娱乐小天地")
# sleep(3)
# driver.find_elements_by_android_uiautomator(loc_13)[1].send_keys(u"小小天")
# sleep(3)
# driver.find_element_by_accessibility_id("请选择").click()
# sleep(3)
# driver.find_element_by_xpath("//*[@text='劳模工作室']").click()
# sleep(3)
# driver.find_elements_by_android_uiautomator(loc_13)[2].send_keys(u"南方通信大厦")
# sleep(3)
# driver.find_elements_by_android_uiautomator(loc_13)[3].send_keys(u"冠军")
# sleep(3)
# driver.find_element_by_accessibility_id("添加图片附件").click()
# sleep(2)
# driver.find_element_by_id("com.tencent.wework:id/tr").click()
# sleep(2)
# driver.find_element_by_id("com.tencent.wework:id/cb7").click()
# sleep(2)
# driver.find_element_by_accessibility_id("提交").click()
# sleep(5)
# driver.find_element_by_accessibility_id(u"关闭页面  Link").click()

# # 魅美影像发布活动
# driver.find_element_by_xpath("//*[@text='工作台']").click()
# sleep(3)
# swipeUp(driver,n=2)
# sleep(2)
# driver.find_element_by_xpath("//*[@text='魅美影像']").click()
# sleep(3)
# driver.find_element_by_xpath("//*[@text='活动汇总']").click()
# sleep(2)
# driver.find_element_by_xpath("//*[@text='发布活动']").click()
# sleep(8)
# loc_14 = 'new UiSelector().className("android.widget.EditText")'
# driver.find_elements_by_android_uiautomator(loc_14)[0].send_keys(u"最逗比同事")
# sleep(3)
# driver.find_element_by_accessibility_id("Link").click()
# sleep(5)
# driver.find_element_by_id("com.tencent.wework:id/tq").click()
# sleep(2)
# driver.find_element_by_id("com.tencent.wework:id/cb7").click()
# sleep(3)
# driver.find_element_by_xpath("//android.widget.ListView/android.view.View[4]/android.widget.EditText[1]").send_keys("13527188046")
# sleep(3)
# driver.tap([(600,635)],100)
# sleep(3)
# driver.swipe(600,1130,600,1083)
# sleep(2)
# driver.tap([(680,900)],100)
# sleep(3)
# driver.tap([(600,735)],100)
# sleep(3)
# driver.swipe(600,1130,600,1035)
# sleep(2)
# driver.tap([(680,900)],100)
# sleep(3)
# driver.find_elements_by_android_uiautomator(loc_14)[5].send_keys(u"南方通信大厦")
# sleep(3)
# driver.find_elements_by_android_uiautomator(loc_14)[6].send_keys(u"我不知道活动内容")
# sleep(3)
# driver.find_elements_by_android_uiautomator(loc_14)[7].send_keys(u"没有备注")
# sleep(3)
# driver.tap([(354,1154)],100)
# sleep(8)
# driver.tap([(360,755)],100)

# # 热点论坛发布
# driver.find_element_by_xpath("//*[@text='工作台']").click()
# sleep(3)
# swipeUp(driver,n=2)
# sleep(2)
# driver.find_element_by_xpath("//*[@text='热点论坛']").click()
# sleep(3)
# driver.find_element_by_xpath("//android.view.View[@content-desc=\"热点论坛\"]/android.view.View[2]/android.widget.Image[1]").click()
# sleep(6)
# loc_15 = 'new UiSelector().className("android.widget.EditText")'
# driver.find_elements_by_android_uiautomator(loc_15)[0].send_keys(u"哪里好玩")
# sleep(3)
# driver.find_elements_by_android_uiautomator(loc_15)[1].send_keys(u"我什么都不想说")
# sleep(3)
# driver.find_element_by_accessibility_id("Link").click()
# sleep(5)
# driver.find_element_by_id("com.tencent.wework:id/tq").click()
# sleep(2)
# driver.find_element_by_id("com.tencent.wework:id/cb7").click()
# sleep(3)
# driver.find_element_by_accessibility_id("立即发布").click()

# # 四小建设
# driver.find_element_by_xpath("//*[@text='工作台']").click()
# sleep(3)
# swipeUp(driver,n=2)
# sleep(2)
# driver.find_element_by_xpath("//*[@text='四小建设']").click()
# sleep(3)
# driver.find_element_by_xpath("//*[@text='需求提出']").click()
# sleep(3)
# driver.find_element_by_xpath("//*[@text='新设施入库']").click()
# sleep(10)
# acc_1 = 'new UiSelector().description("请选择")'
# driver.find_element_by_xpath("//android.widget.ListView/android.view.View[1]/android.view.View[1]/android.view.View[2]").click()
# sleep(3)
# driver.find_element_by_xpath("//*[@text='内部测试']").click()
# sleep(3)
# driver.tap([(640,236)],100)
# driver.find_element_by_xpath("//android.widget.ListView/android.view.View[2]/android.view.View[1]/android.view.View[2]").click()
# sleep(3)
# driver.find_element_by_accessibility_id("阿佩营销中心").click()
# sleep(3)
# driver.tap([(511,860)],100)
# sleep(3)
# driver.find_element_by_xpath("//android.widget.ListView/android.view.View[3]/android.view.View[1]/android.view.View[2]").click()
# sleep(3)
# driver.find_element_by_accessibility_id("小休息室").click()
# sleep(3)
# driver.tap([(515,960)],100)
# sleep(2)
# driver.find_element_by_xpath("//android.widget.ListView/android.view.View[4]/android.view.View[1]/android.view.View[2]").click()
# sleep(2)
# driver.tap([(580,590)],100)
# sleep(3)
# driver.tap([(515,960)],100)
# sleep(2)
# driver.find_element_by_xpath("//android.widget.ListView/android.view.View[5]/android.view.View[1]/android.view.View[2]").click()
# sleep(2)
# driver.tap([(590,760)],100)
# sleep(3)
# driver.tap([(515,855)],100)
# sleep(3)
# driver.find_element_by_xpath("//android.widget.ListView/android.view.View[6]/android.view.View[1]/android.view.View[2]").click()
# sleep(3)
# driver.tap([(600,722)],100)
# sleep(3)
# driver.tap([(515,821)],100)
# sleep(3)
# driver.find_element_by_accessibility_id("请输入").click()
# sleep(3)
# loc_15 = 'new UiSelector().className("android.widget.EditText")'
# driver.find_element_by_xpath\
#     ("//android.view.View[@content-desc=\"台账入库申请\"]/android.view.View[2]/android.widget.EditText[1]").send_keys("1")
# sleep(2)
# driver.find_element_by_xpath("//android.view.View/android.widget.EditText[2]").send_keys(u"台")
# sleep(3)
# driver.tap([(515,780)],100)
# sleep(3)
# driver.find_element_by_xpath\
#     ("//android.widget.ListView/android.view.View[8]/android.view.View[1]/android.widget.EditText[1]")\
#     .click()
# sleep(3)
# driver.find_element_by_accessibility_id("确定").click()
# sleep(3)
# driver.find_element_by_xpath("//android.widget.ListView/android.view.View[9]/android.view.View[1]/android.view.View[2]").click()
# sleep(3)
# driver.find_element_by_xpath("//*[@text='需要更换']").click()
# sleep(3)
# driver.find_element_by_xpath("//android.widget.ListView/android.view.View[10]/android.view.View[1]/android.view.View[2]").click()
# sleep(3)
# driver.find_element_by_xpath("//*[@text='工会']").click()
# sleep(3)
# driver.find_element_by_xpath("//android.widget.ListView/android.view.View[11]/android.view.View[1]/android.view.View[2]").click()
# sleep(3)
# driver.find_element_by_xpath("//*[@text='工会经费']").click()
# sleep(3)
# driver.find_element_by_xpath\
#     ("//android.widget.ListView/android.view.View[12]/android.view.View[1]/android.widget.EditText[1]").click()
# sleep(3)
# driver.find_element_by_accessibility_id("确定").click()
# sleep(3)
# driver.find_element_by_xpath\
#     ("//android.widget.ListView/android.view.View[13]/android.view.View[1]/android.widget.EditText[1]").send_keys("0")
# sleep(2)
# driver.find_element_by_xpath\
#     ("//android.widget.ListView/android.view.View[14]/android.view.View[1]/android.widget.EditText[1]").send_keys("1000")
# sleep(3)
# swipeUp(driver,n=2)
# sleep(2)
# driver.tap([(80,866)],100)
# sleep(2)
# driver.find_element_by_id("com.tencent.wework:id/tr").click()
# sleep(2)
# driver.find_element_by_id("com.tencent.wework:id/cb7").click()
# sleep(3)
# driver.find_element_by_xpath("//android.view.View/android.view.View[2]/android.widget.EditText[1]").send_keys(u"无")
# sleep(2)
# driver.tap([(350,1245)],100)
# sleep(8)
# driver.find_element_by_accessibility_id("关闭页面  Link").click()
# sleep(3)
# driver.find_element_by_xpath("//*[@text='需求提出']").click()
# sleep(3)
# driver.find_element_by_xpath("//*[@text='设施更换需求']").click()
# sleep(10)
# driver.find_element_by_xpath("//android.widget.ListView/android.view.View[1]/android.view.View[1]/android.view.View[2]").click()
# sleep(3)
# driver.find_element_by_xpath("//*[@text='内部测试']").click()
# sleep(3)
# driver.find_element_by_xpath("//android.widget.ListView/android.view.View[2]/android.view.View[1]/android.view.View[2]").click()
# sleep(3)
# driver.find_element_by_accessibility_id("阿佩营销中心").click()
# sleep(3)
# driver.tap([(511,860)],100)
# sleep(3)
# driver.tap([(500,612)],100)
# sleep(3)
# driver.tap([(512,918)],100)
# sleep(3)
# driver.find_element_by_xpath("//android.view.View/android.view.View[2]/android.widget.EditText[1]").send_keys(u"通过")
# sleep(3)
# driver.find_element_by_accessibility_id("立即发布").click()
# sleep(8)
# driver.find_element_by_accessibility_id("关闭页面  Link").click()

# # 新增设施需求
# driver.find_element_by_xpath("//*[@text='工作台']").click()
# sleep(3)
# swipeUp(driver,n=2)
# sleep(2)
# driver.find_element_by_xpath("//*[@text='四小建设']").click()
# sleep(3)
# driver.find_element_by_xpath("//*[@text='需求提出']").click()
# sleep(3)
# driver.find_element_by_xpath("//*[@text='新增设施需求']").click()
# sleep(10)
# driver.find_element_by_xpath("//android.widget.ListView/android.view.View[1]/android.view.View[1]/android.view.View[2]").click()
# sleep(3)
# driver.find_element_by_xpath("//*[@text='内部测试']").click()
# sleep(3)
# driver.find_element_by_xpath("//android.widget.ListView/android.view.View[2]/android.view.View[1]/android.view.View[2]").click()
# sleep(3)
# driver.find_element_by_accessibility_id("阿佩营销中心").click()
# driver.tap([(515,855)],100)
# sleep(3)
# driver.find_element_by_xpath("//android.widget.ListView/android.view.View[3]/android.view.View[1]/android.view.View[2]").click()
# sleep(3)
# driver.tap([(574,517)],100)
# sleep(3)
# driver.tap([(515,960)],100)
# sleep(3)
# driver.find_element_by_xpath("//android.widget.ListView/android.view.View[4]/android.view.View[1]/android.view.View[2]").click()
# sleep(3)
# driver.tap([(580,590)],100)
# sleep(3)
# driver.tap([(515,960)],100)
# sleep(3)
# driver.find_element_by_xpath("//android.widget.ListView/android.view.View[5]/android.view.View[1]/android.view.View[2]").click()
# sleep(3)
# driver.tap([(589,762)],100)
# sleep(3)
# driver.tap([(515,860)],100)
# sleep(3)
# driver.find_element_by_xpath("//android.widget.ListView/android.view.View[6]/android.view.View[1]/android.view.View[2]").click()
# sleep(3)
# driver.tap([(590,760)],100)
# sleep(3)
# driver.tap([(515,860)],100)
# sleep(3)
# driver.find_element_by_accessibility_id("请输入").click()
# sleep(3)
# driver.find_element_by_xpath\
#     ("//android.view.View[@content-desc=\"新增需求申请\"]/android.view.View[2]/android.widget.EditText[1]").send_keys("1")
# sleep(3)
# driver.find_element_by_xpath("//android.view.View/android.widget.EditText[2]").send_keys(u"台")
# sleep(3)
# driver.tap([(515,780)],100)
# sleep(3)
# driver.find_element_by_xpath("//android.view.View/android.view.View[1]/android.widget.EditText[1]").send_keys("1000")
# sleep(3)
# driver.find_element_by_xpath("//android.view.View/android.view.View[2]/android.widget.EditText[1]").send_keys(u"无")
# sleep(3)
# driver.find_element_by_accessibility_id("立即发布").click()
# sleep(8)
# driver.find_element_by_accessibility_id("关闭页面  Link").click()

# # 兴趣协会-发布普通协会活动（定期活动类似，尚未写自动化case)
# driver.find_element_by_xpath("//*[@text='工作台']").click()
# sleep(3)
# swipeUp(driver,n=2)
# sleep(2)
# driver.find_element_by_xpath("//*[@text='兴趣协会']").click()
# sleep(3)
# driver.find_element_by_xpath("//*[@text='我的协会']").click()
# sleep(3)
# driver.tap([(308,175)],100)
# sleep(3)
# driver.find_element_by_xpath("//android.view.View[@content-desc=\"\"]").click()
# sleep(3)
# driver.tap([(460,1056)],100)
# sleep(3)
# driver.find_element_by_accessibility_id(" Link").click()
# sleep(3)
# driver.tap([(354,1144)],100)
# sleep(6)
# driver.find_element_by_accessibility_id("Link").click()
# sleep(3)
# driver.find_element_by_id("com.tencent.wework:id/tr").click()
# sleep(2)
# driver.find_element_by_id("com.tencent.wework:id/cb7").click()
# sleep(3)
# driver.find_element_by_xpath("//android.widget.ListView/android.view.View[1]/android.widget.EditText[1]").send_keys(u"剪纸小活动")
# sleep(3)
# driver.find_element_by_xpath("//android.view.View[@content-desc=\"活动发布\"]"
#                              "/android.widget.ListView[2]/android.view.View[2]/android.widget.EditText[1]")\
#     .send_keys("13527188046")
# sleep(3)
# driver.find_element_by_accessibility_id("选择时间").click()
# sleep(3)
# driver.swipe(361,1128,356,1085)
# driver.tap([(676,899)],100)
# sleep(3)
# driver.find_element_by_xpath\
#     ("//android.view.View[@content-desc=\"活动发布\"]/android.widget.ListView[3]/android.view.View[2]/android.view.View[2]").click()
# sleep(3)
# driver.swipe(361,1128,356,1037)
# driver.tap([(676,899)],100)
# sleep(3)
# driver.tap([(624,690)],100)
# sleep(15)
# driver.tap([(350,1240)],100)
# sleep(3)
# driver.find_element_by_xpath\
#     ("//android.widget.ListView/android.view.View[2]/android.view.View[2]/android.widget.EditText[1]").send_keys(u"南方通信大厦")
# sleep(3)
# driver.find_element_by_accessibility_id("无积分").click()
# sleep(3)
# driver.find_element_by_xpath("//*[@text='有积分']").click()
# sleep(1)
# swipeUp(driver,n=2)
# sleep(2)
# driver.tap([(620,815)],100)
# sleep(2)
# driver.tap([(612,452)],100)
# driver.tap([(360,1240)],100)
# sleep(3)
# driver.tap([(644,955)],100)
# sleep(3)
# driver.press_keycode(keycode=15)
# driver.press_keycode(keycode=15)
# driver.press_keycode(keycode=15)
# sleep(3)
# driver.tap([(82,1102)],100)
# sleep(3)
# driver.keyevent(keycode=13)
# driver.press_keycode(keycode=16)
# sleep(3)
# driver.find_element_by_accessibility_id("立即发布").click()


    def test11(self):
        print u"兴趣协会-发布普通协会活动"
        swipeUp(self.driver, n=2)
        sleep(2)
        self.driver.find_element_by_xpath("//*[@text='兴趣协会']").click()
        sleep(3)
        self.driver.find_element_by_xpath("//*[@text='我的协会']").click()
        sleep(5)
        self.driver.find_element_by_accessibility_id("ycxA我来了 Link").click()
        # self.driver.tap([(308, 175)], 100)
        sleep(5)
        self.driver.find_element_by_xpath("//android.view.View[@content-desc=\"\"]").click()
        sleep(5)
        self.driver.tap([(460, 1056)], 100)
        sleep(5)
        self.driver.find_element_by_accessibility_id(" Link").click()
        sleep(3)
        self.driver.tap([(354, 1144)], 100)
        sleep(6)
        self.driver.find_element_by_accessibility_id("Link").click()
        sleep(3)
        self.driver.find_element_by_id("com.tencent.wework:id/tr").click()
        sleep(2)
        self.driver.find_element_by_id("com.tencent.wework:id/cb7").click()
        sleep(3)
        self.driver.find_element_by_xpath(
            "//android.widget.ListView/android.view.View[1]/android.widget.EditText[1]").send_keys(u"剪纸小活动")
        sleep(3)
        self.driver.find_element_by_xpath("//android.view.View[@content-desc=\"活动发布\"]"
                                          "/android.widget.ListView[2]/android.view.View[2]/android.widget.EditText[1]") \
            .send_keys("13527188046")
        sleep(3)
        self.driver.find_element_by_accessibility_id("选择时间").click()
        sleep(3)
        self.driver.swipe(361, 1128, 356, 1085)
        self.driver.tap([(676, 899)], 100)
        sleep(3)
        self.driver.find_element_by_xpath \
            (
                "//android.view.View[@content-desc=\"活动发布\"]/android.widget.ListView[3]/android.view.View[2]/android.view.View[2]").click()
        sleep(3)
        self.driver.swipe(361, 1128, 356, 1037)
        self.driver.tap([(676, 899)], 100)
        sleep(3)
        self.driver.tap([(624, 690)], 100)
        sleep(15)
        self.driver.tap([(350, 1240)], 100)
        sleep(3)
        self.driver.find_element_by_xpath \
            ("//android.widget.ListView/android.view.View[2]/android.view.View[2]/android.widget.EditText[1]").send_keys(
            u"南方通信大厦")
        sleep(3)
        self.driver.find_element_by_accessibility_id("无积分").click()
        sleep(3)
        self.driver.find_element_by_xpath("//*[@text='有积分']").click()
        sleep(1)
        swipeUp(self.driver, n=2)
        sleep(2)
        self.driver.tap([(620, 815)], 100)
        sleep(3)
        self.driver.tap([(612, 452)], 100)
        self.driver.tap([(360, 1240)], 100)
        sleep(3)
        self.driver.tap([(644, 955)], 100)
        sleep(3)
        self.driver.press_keycode(keycode=15)
        self.driver.press_keycode(keycode=15)
        self.driver.press_keycode(keycode=15)
        sleep(3)
        self.driver.tap([(82, 1102)], 100)
        sleep(3)
        self.driver.keyevent(keycode=13)
        self.driver.press_keycode(keycode=16)
        sleep(3)
        self.driver.find_element_by_accessibility_id("立即发布").click()
        sleep(8)
        self.driver.tap([(34, 70)], 100)
        sleep(5)
        print "ok"

if __name__ == "__main__":
    unittest.main()



