import unittest
import requests
import logging,logging.config
from log import TestLog

hostUrl = "http://192.168.1.3"

#日志配置
'''
CON_LOG = "../log/log.conf"
logging.config.fileConfig(CON_LOG)
logger = logging.getLogger()
'''


logger = TestLog.TestLog().getlog()

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
        self.assertEqual(response["type"],1)
        logger.handlers.pop()


if __name__ == '__main__':
    unittest.main()
