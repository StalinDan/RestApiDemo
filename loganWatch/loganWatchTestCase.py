import unittest
import requests
import logging,logging.config
from log import TestLog

hostUrl = "http://192.168.1.3"

#日志配置
#第一种： 打印日志 只打印 logger.info("12345")  logger.error("error")
'''
CON_LOG = "../log/log.conf"
logging.config.fileConfig(CON_LOG)
logger = logging.getLogger()
'''

#第二种：不打印日志
# logger = TestLog.TestLog().getlog()

#第三种：可以打印

logging.basicConfig(format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='../log/test.log',
                    filemode='w')
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


class MyTestCase(unittest.TestCase):

    def test_something(self):
        self.assertEqual(True, False)

    def test_bindBed(self):
        logger.info("12345")
        logger.debug("debug")
        logger.error("error")
        r = requests.get("http://192.168.1.3:80/api2/bed/bind")
        response = r.json()
        # print(response)
        logger.info(response)
        logger.info("kkkkk")
        self.assertEqual(response["type"],1)
        # logger.handlers.pop()


if __name__ == '__main__':
    unittest.main()
