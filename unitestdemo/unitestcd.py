import unittest
from unitestdemo import demo

if __name__ == '__main__':
    # unittest.main() #使用main()直接运行时，将按case的名称顺序执行
    suite = unittest.TestSuite()
    suite.addTest(demo.MyTestCase('test_01'))  # 将需要执行的case添加到Test Suite中，没有添加的不会被执行
    suite.addTest(demo.MyTestCase('test_02'))
    suite.addTest(demo.MyTestCase('test_03'))
    suite.addTest(demo.MyTestCase('test_04'))
    suite.addTest(demo.MyTestCase('test_05'))
    suite.addTest(demo.MyTestCase('test_06'))
    unittest.TextTestRunner().run(suite)  # 将根据case添加的先后顺序执行
