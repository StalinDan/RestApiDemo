import unittest
import requests

class MyTestCase(unittest.TestCase):
    def test_something(self):
       datacon={'email':'1615266681@qq.com','password':'guangyi77'}
       r=requests.post("http://www.testertechnology.com:8081/user/login",data=datacon);
       print(r.text)
       print(r.status_code)
       print(r.headers)
       print(r.headers['Content-Type'])


if __name__ == '__main__':
    unittest.main()
