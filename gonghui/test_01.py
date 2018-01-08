# coding:utf-8
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
import unittest
import time


class Union(unittest.TestCase):
    import SendKeys
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
    def test01(self):
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
        self.driver.find_element_by_css_selector(".btn.btn-green").click()
        time.sleep(3)
        print "OK"
    def test02(self):
        print u"添加工会宣传"
        # 点击微信公会
        # self.driver.find_element_by_xpath(".//*[@id='navbarList']/li[1]/a").click()
        # time.sleep(2)
        # 点击工会家园
        # self.driver.find_element_by_xpath(".//*[@id='mainPanel']/div[1]/div[1]/h4/a/span[2]").click()
        # time.sleep(3)
        # 点击工会宣传
        self.driver.find_element_by_xpath(".//*[@id='collapse_0']/ul/li[4]/a").click()
        time.sleep(3)
        js2 = 'document.getElementsByClassName("btn-empty-theme")[1].click();'
        self.driver.execute_script(js2)
        time.sleep(2)
        s1 = self.driver.find_element_by_xpath(".//*[@id='addForm']/div[1]/select")
        Select(s1).select_by_value("url")
        self.driver.implicitly_wait(20)
        Select(s1).select_by_value("txtimg")
        self.driver.implicitly_wait(20)
        Select(s1).select_by_value("url")
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_class_name("form-control").click()
        self.driver.find_element_by_xpath(".//*[@id='addForm']/div[2]/input").send_keys("123")
        time.sleep(2)
        self.driver.find_element_by_xpath(".//*[@id='contentUrl']/input").send_keys("https://www.baidu.com")
        time.sleep(2)
        s2 = self.driver.find_element_by_xpath(".//*[@id='addForm']/div[5]/select")
        Select(s2).select_by_visible_text(u"不置顶")
        time.sleep(2)
        self.driver.find_element_by_name('_img').send_keys(r"D:\tupian\1.jpg")
        time.sleep(3)
        self.driver.find_element_by_xpath(".//*[@id='addLawBtn']").click()
        time.sleep(3)
        self.driver.find_element_by_xpath("html/body/div[4]/div/div/div[3]/button[1]").click()
        time.sleep(3)
        print "ok"
    def test03(self):
        print u"添加女子课堂"
        # 点击微信工会
        # self.driver.find_element_by_xpath(".//*[@id='navbarList']/li[1]/a").click()
        # time.sleep(2)
        # 点击女工园地
        self.driver.find_element_by_xpath(".//*[@id='mainPanel']/div[2]/div[1]/h4/a/span[2]").click()
        time.sleep(2)
        # 点击女子课堂
        self.driver.find_element_by_xpath(".//*[@id='collapse_1']/ul/li[1]/a").click()
        time.sleep(2)
        # 新增课堂
        js3 = 'document.getElementsByClassName("btn-empty-theme")[0].click();'
        self.driver.execute_script(js3)
        time.sleep(2)
        self.driver.find_element_by_xpath(".//*[@id='addPane']/form/div[1]/div[1]/input").send_keys(u"女子瑜伽")
        time.sleep(2)
        self.driver.find_element_by_xpath(".//*[@id='addPane']/form/div[1]/div[2]/input").send_keys("12")
        time.sleep(2)
        self.driver.find_element_by_xpath(".//*[@id='addPane']/form/div[1]/div[3]/div/input[1]").send_keys("2017-12-12 9:00")
        self.driver.find_element_by_xpath(".//*[@id='addPane']/form/div[1]/div[3]/label").click()
        time.sleep(2)
        self.driver.find_element_by_xpath(".//*[@id='addPane']/form/div[1]/div[3]/div/input[2]").send_keys("2017-12-20 17:00")
        self.driver.find_element_by_xpath(".//*[@id='addPane']/form/div[1]/div[3]/label").click()
        time.sleep(2)
        self.driver.find_element_by_xpath(".//*[@id='addPane']/form/div[1]/div[4]/textarea").send_keys(u"瑜伽，带给您自然而然的感觉。")
        time.sleep(2)
        self.driver.find_element_by_xpath(".//*[@id='addPane']/form/div[1]/div[5]/textarea").send_keys(u"无")
        time.sleep(2)
        js5="var q=document.documentElement.scrollTop=10000"
        self.driver.execute_script(js5)
        time.sleep(2)
        self.driver.find_element_by_xpath(".//*[@id='addPane']/form/div[1]/div[6]/label[3]/input").click()
        time.sleep(5)
        self.driver.find_element_by_name('_img').send_keys(r"D:\tupian\1.jpg")
        time.sleep(2)
        self.driver.find_element_by_id("fujianFile").send_keys(r"D:\tupian\17.jpg")
        time.sleep(2)
        self.driver.find_element_by_id("addBtn").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("html/body/div[7]/div/div/div[3]/button[1]").click()
        time.sleep(3)
        print "ok"
    def test04(self):
        print u"新增妈妈小屋"
        # 点击微信工会
        # self.driver.find_element_by_xpath(".//*[@id='navbarList']/li[1]/a").click()
        # time.sleep(2)
        # 点击女工园地
        # self.driver.find_element_by_xpath(".//*[@id='mainPanel']/div[2]/div[1]/h4/a/span[2]").click()
        # time.sleep(2)
        # 点击妈妈小屋
        self.driver.find_element_by_xpath(".//*[@id='collapse_1']/ul/li[2]/a").click()
        time.sleep(5)
        # 新增小屋
        self.driver.find_element_by_xpath(".//*[@id='mainPane']/div/a").click()
        time.sleep(2)
        self.driver.find_element_by_xpath(".//*[@id='addPane']/div[3]/from/div[1]/div/input").send_keys(u"育儿经验分享")
        time.sleep(2)
        self.driver.find_element_by_name("_img").send_keys(r"D:\tupian\1.jpg")
        time.sleep(2)
        self.driver.find_element_by_xpath(".//*[@id='addPane']/div[3]/from/div[3]/div/textarea").send_keys(u"我们讲述了很多关于优生、新生儿护理、婴幼儿生理卫生和心理卫生知识等内容，它会帮助您了解更多的0-6岁的育儿保健知识，更好教育幼儿，促进其健康成长。")
        time.sleep(2)
        self.driver.find_element_by_xpath(".//*[@id='start_1']").send_keys("9:00")
        self.driver.find_element_by_xpath(".//*[@id='addPane']/div[4]/div/div[1]/label[2]").click()
        time.sleep(2)
        self.driver.find_element_by_xpath(".//*[@id='end_1']").send_keys("17:00")
        self.driver.find_element_by_xpath(".//*[@id='addPane']/div[4]/div/div[1]/label[2]").click()
        time.sleep(2)
        self.driver.find_element_by_id("mon").click()
        time.sleep(2)
        self.driver.find_element_by_id("submit").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("html/body/div[19]/div/div/div[3]/button[1]").click()
        time.sleep(3)
        print "ok"
    def test05(self):
        print u"党建在线添加文章"
        # 点击党建在线
        self.driver.find_element_by_xpath(".//*[@id='navbarList']/li[2]/a").click()
        time.sleep(2)
        # 点击文章管理
        self.driver.find_element_by_xpath(".//*[@id='mainPanel']/div[2]/div[1]/h4/a/span[2]").click()
        time.sleep(2)
        # 点击添加文章
        self.driver.find_element_by_xpath(".//*[@id='collapse_1']/ul/li[1]/a").click()
        time.sleep(2)
        # 点击链接
        self.driver.find_element_by_xpath(".//*[@id='cateNav']/li[2]/a").click()
        time.sleep(3)
        self.driver.find_element_by_xpath(".//*[@id='form']").click()
        self.driver.find_element_by_xpath(".//*[@id='add-title']").send_keys(u"父亲")
        time.sleep(2)
        self.driver.find_element_by_id("addMyimg").send_keys(r"D:\tupian\1.jpg")
        time.sleep(2)
        self.driver.find_element_by_xpath(".//*[@id='form']/div[2]/label[3]/input").click()
        time.sleep(2)
        self.driver.find_element_by_id("add-brief-info").send_keys(u"父亲老了，看着父亲的背影，我思绪万千......")
        time.sleep(2)
        self.driver.find_element_by_id("link").send_keys("https://news.baidu.com")
        time.sleep(2)
        self.driver.find_element_by_id("attachments").send_keys(r"D:\tupian\2.jpg")
        time.sleep(2)
        self.driver.find_element_by_xpath(".//*[@id='addProductConfirm']").click()
        time.sleep(2)
        self.driver.find_element_by_class_name("btn-green").click()
        time.sleep(3)
        print "ok"
    def test06(self):
        print u"党建在线发布摄影比赛"
        # 点击党建在线
        self.driver.find_element_by_xpath(".//*[@id='navbarList']/li[2]/a").click()
        time.sleep(2)
        # 点击摄影比赛
        self.driver.find_element_by_xpath(".//*[@id='mainPanel']/div[3]/div[1]/h4/a/span[2]").click()
        time.sleep(2)
        # 点击发布比赛
        self.driver.find_element_by_xpath(".//*[@id='collapse_2']/ul/li[1]/a").click()
        time.sleep(2)
        self.driver.find_element_by_xpath(".//*[@id='uiMain']/div/div/from/div[1]/div/input").send_keys(u"选美比赛")
        time.sleep(2)
        self.driver.find_element_by_name("_img").send_keys(r"D:\tupian\16.jpg")
        time.sleep(2)
        self.driver.find_element_by_xpath(".//*[@id='uiMain']/div/div/from/div[3]/div/input").send_keys("13527188046")
        time.sleep(2)
        js_4= 'document.getElementById("start_datetimepicker").removeAttribute("readonly");'
        self.driver.execute_script(js_4)
        js_5= 'document.getElementById("end_datetimepicker").removeAttribute("readonly");'
        self.driver.execute_script(js_5)
        self.driver.find_element_by_id("start_datetimepicker").send_keys("2017-12-15 9:00")
        self.driver.find_element_by_xpath(".//*[@id='uiMain']/div/div/from/div[4]/label[1]").click()
        time.sleep(2)
        self.driver.find_element_by_id("end_datetimepicker").send_keys("2017-12-25 17:00")
        self.driver.find_element_by_xpath(".//*[@id='uiMain']/div/div/from/div[4]/label[2]").click()
        time.sleep(2)
        self.driver.find_element_by_xpath(".//*[@id='uiMain']/div/div/from/div[5]/div/textarea").send_keys(u"无整容，无ps,纯天然")
        time.sleep(2)
        self.driver.find_element_by_xpath(".//*[@id='uiMain']/div/div/from/div[6]/div/textarea").send_keys(u"不限地区，冠军可获得10万美元")
        time.sleep(2)
        s9 = self.driver.find_element_by_xpath(".//*[@id='select']")
        Select(s9).select_by_index(1)
        time.sleep(2)
        self.driver.find_element_by_xpath(".//*[@id='submit']").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("html/body/div[21]/div/div/div[3]/button[1]").click()
        # self.driver.find_element_by_class_name("btn-green").click()
        time.sleep(3)
        print "ok"
    def test07(self):
        print u"党建在线，面向支部添加学习计划"
        # 点击党建在线
        # self.driver.find_element_by_xpath(".//*[@id='navbarList']/li[2]/a").click()
        # time.sleep(2)
        # 点击学习考试
        self.driver.find_element_by_xpath(".//*[@id='mainPanel']/div[5]/div[1]/h4/a/span[2]").click()
        time.sleep(2)
        # 点击学习计划
        self.driver.find_element_by_xpath(".//*[@id='collapse_4']/ul/li[2]/a").click()
        time.sleep(2)
        # 点击添加计划
        self.driver.find_element_by_xpath(".//*[@id='mainPane']/div[1]/a[1]").click()
        time.sleep(2)
        self.driver.find_element_by_xpath(".//*[@id='addPane']/form/div[1]/input").send_keys("2017-12-25 9:00")
        self.driver.find_element_by_xpath(".//*[@id='addPane']/form/div[1]/label").click()
        time.sleep(2)
        self.driver.find_element_by_xpath(".//*[@id='addPane']/form/div[2]/input").send_keys("2017-12-29 17:30")
        self.driver.find_element_by_xpath(".//*[@id='addPane']/form/div[2]/label").click()
        time.sleep(2)
        s10 =self.driver.find_element_by_xpath(".//*[@id='branch']/select")
        Select(s10).select_by_index(1)
        time.sleep(2)
        s11 =self.driver.find_element_by_xpath(".//*[@id='branch']/select[2]")
        Select(s11).select_by_index(1)
        time.sleep(2)
        self.driver.find_element_by_xpath(".//*[@id='addPane']/form/div[5]/textarea").send_keys(u"年底之前进行测试")
        time.sleep(2)
        self.driver.find_element_by_xpath(".//*[@id='addBtn']").click()
        time.sleep(2)
        self.driver.find_element_by_class_name("btn-green").click()
        time.sleep(3)
        print "ok"
    def test08(self):
        print u"党建在线，面向支部发布考试"
        # 点击党建在线
        # self.driver.find_element_by_xpath(".//*[@id='navbarList']/li[2]/a").click()
        # time.sleep(2)
        # 点击学习考试
        # self.driver.find_element_by_xpath(".//*[@id='mainPanel']/div[5]/div[1]/h4/a/span[2]").click()
        # time.sleep(2)
        # 点击发布考试
        self.driver.find_element_by_xpath(".//*[@id='collapse_4']/ul/li[3]/a").click()
        time.sleep(2)
        self.driver.find_element_by_xpath(".//*[@id='pNav']/li[1]/a").click()
        time.sleep(2)
        s12 = self.driver.find_element_by_xpath(".//*[@id='groupId']")
        Select(s12).select_by_index(1)
        time.sleep(5)
        s13 = self.driver.find_element_by_xpath(".//*[@id='branch']/select[2]")
        Select(s13).select_by_index(1)
        time.sleep(2)
        s14 = self.driver.find_element_by_xpath(".//*[@id='plan']")
        Select(s14).select_by_index(0)
        time.sleep(2)
        self.driver.find_element_by_xpath(".//*[@id='exameName']").send_keys(u"英语测试")
        time.sleep(2)
        self.driver.find_element_by_xpath(".//*[@id='exameInfo']").send_keys(u"无")
        time.sleep(2)
        self.driver.find_element_by_xpath(".//*[@id='uiMain']/div/form/div[6]/div/label[2]/input").click()
        time.sleep(2)
        js_6= 'document.getElementById("endTime").removeAttribute("readonly");'
        self.driver.execute_script(js_6)
        self.driver.find_element_by_id("endTime").send_keys("2017-12-25 23:59")
        self.driver.find_element_by_xpath(".//*[@id='uiMain']/div/form/div[7]/label").click()
        time.sleep(2)
        self.driver.find_element_by_xpath(".//*[@id='myEditor']").send_keys(u"自主复习")
        time.sleep(2)
        js_7="var q=document.documentElement.scrollTop=10000"
        self.driver.execute_script(js_7)
        time.sleep(2)
        self.driver.find_element_by_xpath(".//*[@id='uiMain']/div/form/div[9]").click()
        self.driver.find_element_by_id("uimage").click()
        time.sleep(3)
        self.SendKeys.SendKeys(r"D:\tupian\3.jpg")
        time.sleep(1)
        self.SendKeys.SendKeys("{ENTER}")
        time.sleep(2)
        self.driver.find_element_by_xpath(".//*[@id='uiMain']/div/form/div[10]").click()
        self.driver.find_element_by_id("ufile").click()
        time.sleep(3)
        self.SendKeys.SendKeys(r"D:\tupian\4.jpg")
        time.sleep(1)
        self.SendKeys.SendKeys("{ENTER}")
        time.sleep(2)
        s15 =self.driver.find_element_by_xpath(".//*[@id='exameType']")
        Select(s15).select_by_index(0)
        time.sleep(2)
        self.driver.find_element_by_xpath(".//*[@id='addExamBtn']").click()
        time.sleep(2)
        self.driver.find_element_by_xpath(".//*[@id='uiMain']/div/form/div[12]/div/div[2]/div[1]/input").clear()
        self.driver.find_element_by_xpath(".//*[@id='uiMain']/div/form/div[12]/div/div[2]/div[1]/input").send_keys(u"one or two")
        time.sleep(2)
        self.driver.find_element_by_xpath(".//*[@id='exame1']/label[1]/input[2]").clear()
        self.driver.find_element_by_xpath(".//*[@id='exame1']/label[1]/input[2]").send_keys(u"one")
        time.sleep(2)
        self.driver.find_element_by_xpath(".//*[@id='exame1']/label[2]/input[2]").clear()
        self.driver.find_element_by_xpath(".//*[@id='exame1']/label[2]/input[2]").send_keys(u"two")
        time.sleep(2)
        self.driver.find_element_by_xpath(".//*[@id='exame1']/label[1]/input[1]").click()
        time.sleep(2)
        self.driver.find_element_by_xpath(".//*[@id='subBtn']").click()
        time.sleep(3)
        self.driver.find_element_by_class_name("btn-green").click()
        time.sleep(5)
        print "ok"
    def test09(self):
        print u"清风纪语公告推送"
        # 点击清风纪语
        self.driver.find_element_by_xpath(".//*[@id='navbarList']/li[3]/a").click()
        time.sleep(2)
        # 点击公告管理
        self.driver.find_element_by_xpath(".//*[@id='mainPanel']/div[1]/div[1]/h4/a/span[2]").click()
        time.sleep(2)
        # 点击公告推送
        self.driver.find_element_by_xpath(".//*[@id='collapse_0']/ul/li[1]/a").click()
        time.sleep(5)
        # 输入内容
        self.driver.find_element_by_xpath(".//*[@id='mpnewsForm']/div[1]/input").click()
        self.driver.find_element_by_xpath(".//*[@id='mpnewsForm']/div[1]/input").send_keys(u"蚊虫大扫除")
        time.sleep(2)
        self.driver.find_element_by_xpath(".//*[@id='uploadNewsImg']").send_keys(r"D:\tupian\1.jpg")
        time.sleep(2)
        s4 =self.driver.find_element_by_xpath(".//*[@id='mpnewsForm']/div[3]/select")
        Select(s4).select_by_index(1)
        time.sleep(2)
        s5 =self.driver.find_element_by_xpath(".//*[@id='mpnewsForm']/div[4]/select")
        Select(s5).select_by_visible_text(u"通知通报")
        time.sleep(5)
        self.driver.find_element_by_xpath(".//*[@id='noticeCnt']").send_keys(u"最近蚊虫猖狂，请各家各户做好防虫除虫措施")
        time.sleep(3)
        self.driver.find_element_by_xpath(".//*[@id='mpnewsForm']/div[6]/textarea").clear()
        self.driver.find_element_by_xpath(".//*[@id='mpnewsForm']/div[6]/textarea").send_keys("123")
        time.sleep(2)
        self.driver.find_element_by_xpath(".//*[@id='mpnewsForm']/div[7]/input").send_keys(u"yy")
        time.sleep(2)
        self.driver.find_element_by_xpath(".//*[@id='mpnewsForm']/div[8]/input").send_keys("https://news.baidu.com")
        time.sleep(2)
        self.driver.find_element_by_xpath(".//*[@id='safeMsgBtn']").click()
        time.sleep(2)
        self.driver.find_element_by_xpath(".//*[@id='sendBtn']").click()
        time.sleep(3)
        print "ok"
    def test10(self):
        print u"清风纪语添加学习计划"
        self.driver.find_element_by_xpath(".//*[@id='navbarList']/li[3]/a").click()
        time.sleep(2)
        # 点击学习考试
        self.driver.find_element_by_xpath(".//*[@id='mainPanel']/div[2]/div[1]/h4/a/span[2]").click()
        time.sleep(2)
        # 点击学习计划
        self.driver.find_element_by_xpath(".//*[@id='collapse_1']/ul/li[2]/a").click()
        time.sleep(2)
        # 添加计划
        self.driver.find_element_by_xpath(".//*[@id='cateNav']/li[2]/a").click()
        time.sleep(2)
        self.driver.find_element_by_xpath(".//*[@id='mainPane']/div[1]/a[1]").click()
        time.sleep(2)
        self.driver.find_element_by_xpath(".//*[@id='addPane']/form/div[1]/input").send_keys("2017-12-12 9:00")
        time.sleep(2)
        self.driver.find_element_by_xpath(".//*[@id='addPane']/form/div[1]/label").click()
        time.sleep(2)
        self.driver.find_element_by_xpath(".//*[@id='addPane']/form/div[2]/input").send_keys("2017-12-20 17:00")
        time.sleep(2)
        self.driver.find_element_by_xpath(".//*[@id='addPane']/form/div[2]/label").click()
        time.sleep(2)
        self.driver.find_element_by_xpath(".//*[@id='addPane']/form/div[3]/textarea").send_keys(u"下周一进行党纪考试")
        time.sleep(2)
        self.driver.find_element_by_xpath(".//*[@id='addBtn']").click()
        time.sleep(2)
        # self.driver.find_element_by_xpath("html/body/div[5]/div/div/div[3]/button[1]").click()
        self.driver.find_element_by_class_name("btn-green").click()
        time.sleep(3)
        print "ok"
    def test11(self):
        print u"清风纪语发布考试"
        # self.driver.find_element_by_xpath(".//*[@id='navbarList']/li[3]/a").click()
        # time.sleep(2)
        # # 点击学习考试
        # self.driver.find_element_by_xpath(".//*[@id='mainPanel']/div[2]/div[1]/h4/a/span[2]").click()
        # time.sleep(2)
        # 点击发布考试
        self.driver.find_element_by_xpath(".//*[@id='collapse_1']/ul/li[3]/a").click()
        time.sleep(2)
        s6 = self.driver.find_element_by_xpath(".//*[@id='groupId']")
        Select(s6).select_by_index(2)
        Select(s6).select_by_index(1)
        Select(s6).select_by_index(2)
        time.sleep(2)
        s7 = self.driver.find_element_by_id("plan")
        Select(s7).select_by_index(1)
        time.sleep(2)
        self.driver.find_element_by_xpath(".//*[@id='exameName']").send_keys(u"党纪考试")
        time.sleep(2)
        self.driver.find_element_by_xpath(".//*[@id='exameInfo']").send_keys(u"各位党员务必参与")
        time.sleep(2)
        self.driver.find_element_by_xpath(".//*[@id='uiMain']/div/form/div[4]/div/label[2]/input").click()
        time.sleep(2)
        js_2= 'document.getElementById("endTime").removeAttribute("readonly");'
        self.driver.execute_script(js_2)
        time.sleep(2)
        self.driver.find_element_by_id("endTime").send_keys("2017-12-20 17:00")
        time.sleep(2)
        self.driver.find_element_by_xpath(".//*[@id='uiMain']/div/form/div[6]/label").click()
        time.sleep(2)
        self.driver.find_element_by_id("myEditor").send_keys(u"无")
        time.sleep(2)
        js_3="var q=document.documentElement.scrollTop=10000"
        self.driver.execute_script(js_3)
        time.sleep(2)
        self.driver.find_element_by_xpath(".//*[@id='uiMain']/div/form/div[8]").click()
        self.driver.find_element_by_id("uimage").click()
        time.sleep(3)
        self.SendKeys.SendKeys(r"D:\tupian\1.jpg")
        time.sleep(1)
        self.SendKeys.SendKeys("{ENTER}")
        time.sleep(2)
        self.driver.find_element_by_xpath(".//*[@id='uiMain']/div/form/div[9]").click()
        self.driver.find_element_by_id("ufile").click()
        time.sleep(3)
        self.SendKeys.SendKeys(r"D:\tupian\2.jpg")
        time.sleep(1)
        self.SendKeys.SendKeys("{ENTER}")
        time.sleep(2)
        s8 =self.driver.find_element_by_xpath(".//*[@id='exameType']")
        Select(s8).select_by_index(0)
        time.sleep(2)
        self.driver.find_element_by_xpath(".//*[@id='addExamBtn']").click()
        time.sleep(2)
        self.driver.find_element_by_xpath(".//*[@id='uiMain']/div/form/div[11]/div/div[2]/div[1]/input").clear()
        self.driver.find_element_by_xpath(".//*[@id='uiMain']/div/form/div[11]/div/div[2]/div[1]/input").send_keys(u"你喜欢谁")
        time.sleep(2)
        self.driver.find_element_by_xpath(".//*[@id='exame1']/label[1]/input[2]").clear()
        self.driver.find_element_by_xpath(".//*[@id='exame1']/label[1]/input[2]").send_keys(u"范冰冰")
        time.sleep(2)
        self.driver.find_element_by_xpath(".//*[@id='exame1']/label[2]/input[2]").clear()
        self.driver.find_element_by_xpath(".//*[@id='exame1']/label[2]/input[2]").send_keys(u"李冰冰")
        time.sleep(2)
        self.driver.find_element_by_xpath(".//*[@id='exame1']/label[1]/input[1]").click()
        time.sleep(2)
        self.driver.find_element_by_xpath(".//*[@id='subBtn']").click()
        time.sleep(3)
        self.driver.find_element_by_class_name("btn-green").click()
        time.sleep(3)
        print "ok"
    def test12(self):
        print u"青年部落添加推送成果"
        # 点击青年部落
        self.driver.find_element_by_xpath(".//*[@id='navbarList']/li[4]/a").click()
        time.sleep(2)
        # 点击往期回顾
        self.driver.find_element_by_xpath(".//*[@id='mainPanel']/div[1]/div[1]/h4/a/span[2]").click()
        time.sleep(2)
        # 点击推送成果
        self.driver.find_element_by_xpath(".//*[@id='collapse_0']/ul/li/a").click()
        time.sleep(2)
        self.driver.find_element_by_xpath(".//*[@id='mpnewsForm']/div[1]/input").click()
        self.driver.find_element_by_xpath(".//*[@id='mpnewsForm']/div[1]/input").send_keys(u"比赛结束")
        time.sleep(2)
        self.driver.find_element_by_xpath(".//*[@id='uploadNewsImg']").send_keys(r"D:\tupian\1.jpg")
        time.sleep(2)
        self.driver.find_element_by_id("noticeCnt").send_keys(u"一年一度的划船比赛正式结束")
        time.sleep(2)
        self.driver.find_element_by_xpath(".//*[@id='mpnewsForm']/div[4]/textarea").clear()
        self.driver.find_element_by_xpath(".//*[@id='mpnewsForm']/div[4]/textarea").send_keys(u"123")
        time.sleep(2)
        self.driver.find_element_by_xpath(".//*[@id='mpnewsForm']/div[5]/input").send_keys(u"yy")
        time.sleep(2)
        self.driver.find_element_by_xpath(".//*[@id='mpnewsForm']/div[6]/input").send_keys("https://news.baidu.com")
        time.sleep(2)
        self.driver.find_element_by_xpath(".//*[@id='safeMsgBtn']").click()
        time.sleep(2)
        self.driver.find_element_by_xpath(".//*[@id='sendBtn']").click()
        time.sleep(2)
        self.driver.find_element_by_class_name("btn-green").click()
        time.sleep(3)
        print "ok"
    def test13(self):
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
        self.driver.find_element_by_xpath(".//*[@id='uiMain']/div/form/div[4]/div[2]/div/input").send_keys(
            "13527188046")
        time.sleep(2)
        self.driver.find_element_by_xpath(".//*[@id='suggestId']").send_keys(u"南方通信大厦")
        time.sleep(2)
        self.driver.find_element_by_xpath(".//*[@id='uiMain']/div/form/div[5]/div/label").click()
        time.sleep(2)
        self.driver.find_element_by_xpath(".//*[@id='uiMain']/div/form/div[7]/div[1]/div/textarea").send_keys(
            u"欢迎参与")
        time.sleep(2)
        self.driver.find_element_by_xpath(".//*[@id='uploadNewsImg']").send_keys(r"D:\tupian\1.jpg")
        time.sleep(2)
        self.driver.find_element_by_xpath(".//*[@id='uiMain']/div/form/div[8]/div/div/textarea").send_keys(u"无")
        time.sleep(2)
        self.driver.find_element_by_id("btn-add").click()
        time.sleep(4)
        self.driver.find_element_by_class_name("btn-green").click()
        time.sleep(4)
        print "ok"
    def test14(self):
        print u"青年部落添加新闻推送"
        # 点击青年部落
        self.driver.find_element_by_xpath(".//*[@id='navbarList']/li[4]/a").click()
        time.sleep(2)
        # 点击新闻管理
        self.driver.find_element_by_xpath(".//*[@id='mainPanel']/div[4]/div[1]/h4/a/span[2]").click()
        time.sleep(2)
        # 点击新闻推送
        self.driver.find_element_by_xpath(".//*[@id='collapse_3']/ul/li[1]/a").click()
        time.sleep(2)
        self.driver.find_element_by_xpath(".//*[@id='cateNav']/li[2]/a").click()
        self.driver.find_element_by_xpath(".//*[@id='cateNav']/li[1]/a").click()
        self.driver.find_element_by_xpath(".//*[@id='cateNav']/li[2]/a").click()
        time.sleep(2)
        self.driver.find_element_by_xpath(".//*[@id='mpnewsForm']/div[1]/input").click()
        self.driver.find_element_by_xpath(".//*[@id='mpnewsForm']/div[1]/input").send_keys(u"天气骤冷")
        time.sleep(2)
        s3 = self.driver.find_element_by_xpath(".//*[@id='select-type']")
        Select(s3).select_by_visible_text(u"先进典型")
        time.sleep(2)
        self.driver.find_element_by_xpath(".//*[@id='uploadNewsImg']").send_keys(r"D:\tupian\1.jpg")
        time.sleep(2)
        self.driver.find_element_by_xpath(".//*[@id='mpnewsForm']/div[5]/textarea").send_keys("123")
        time.sleep(2)
        self.driver.find_element_by_xpath(".//*[@id='mpnewsForm']/div[7]/input").send_keys("https://news.baidu.com")
        time.sleep(2)
        self.driver.find_element_by_xpath(".//*[@id='safeMsgBtn']").click()
        time.sleep(2)
        self.driver.find_element_by_xpath(".//*[@id='sendBtn']").click()
        time.sleep(2)
        self.driver.find_element_by_class_name("btn-green").click()
        time.sleep(3)
        print "ok"


