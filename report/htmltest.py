# coding:utf-8
from report import HTMLTestRunner
import unittest
from report import testDemo
#系统方法
import os
#获取路径
ABSPATH = os.path.abspath(os.path.realpath(os.path.dirname(__file__)))
#C:\Users\Administrator\PycharmProjects\DemoApi\report
print(ABSPATH)
#执行case生成报告
if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(testDemo.MyTestCase("test_one1"))
    suite.addTest(testDemo.MyTestCase("test_one2"))
    suite.addTest(testDemo.MyTestCase("test_one3"))
    suite.addTest(testDemo.MyTestCase("test_one4"))
    suite.addTest(testDemo.MyTestCase("test_one5"))

    #如果没指定路径需要创建路径（获取报告的路径）
    path=ABSPATH
    #IF没有这个路径C:\Users\Administrator\Desktop\interfaceapi\report通过它（makedirs）创建一个路径
    if not os.path.exists(path):
        #创建路径方法
        os.makedirs(path)
    else:
        pass
    report_path = "index.html"
    report_title = u"测试报告"
    desc = u"接口自动化测试报告详情"
    fp = open(report_path, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(fp, title=report_title, description=desc)
    runner.run(suite)
