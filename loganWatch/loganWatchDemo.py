import unittest
from loganWatch import loganWatchTestCase
from report import HTMLTestRunner

import os

ABSPATH = os.path.abspath(os.path.realpath(os.path.dirname(__file__)))
print(ABSPATH)

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(loganWatchTestCase.MyTestCase("test_bindBed"))

    # 如果没指定路径需要创建路径（获取报告的路径）
    path = ABSPATH
    # IF没有这个路径C:\Users\Administrator\Desktop\interfaceapi\report通过它（makedirs）创建一个路径

    if not os.path.exists(path):
        # 创建路径方法
        os.makedirs(path)
    else:
        pass

    report_path = "loganWatch.html"
    report_title = "间休手表测试报告"
    desc = u"间休手表测试详情"
    fp = open(report_path,'wb')
    runner = HTMLTestRunner.HTMLTestRunner(fp,title=report_title,description=desc)
    runner.run(suite)
