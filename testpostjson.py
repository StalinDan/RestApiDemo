import unittest
import requests
class MyTestCase(unittest.TestCase):
    def test_something(self):
       head={"Content-Type":"application/json"}
       data={
          "phone": "14050000000",
          "password": "e10adc3949ba59abbe56e057f20f883e",
          "messageCode": "",
          "loginType": "1",
          "timestamp": ""
         }
       r=requests.post("http://api-shuangshi.tengyue360.com/backend/student/unauth/login",json=data,headers=head);
       print(r.json())



if __name__ == '__main__':
    unittest.main()
