# coding:utf-8
import unittest
from selenium.webdriver.support import expected_conditions as EC
import os
import HTMLTestRunner

# 用例路径
case_path = os.path.join(os.getcwd(), "gonghui")
# 报告存放路径
report_path = os.path.join(os.getcwd(), "report")


def all_case():
    discover = unittest.defaultTestLoader.discover(case_path,pattern="test_app.py",top_level_dir=None)
    print(discover)
    return discover


if __name__ == "__main__":
    report_abspath = os.path.join(report_path, "result.html")
fp = open(report_abspath, "wb")
runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title=u'自动化测试报告,测试结果如下：', description=u'用例执行情况：')
runner.run(all_case())
fp.close()
