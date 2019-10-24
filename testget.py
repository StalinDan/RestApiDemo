import unittest
import requests

class MyTestCase(unittest.TestCase):
    def test_something(self):
     #第一种方式
     #r=requests.get("https://selectcar.yiche.com/selectcarforapp?mid=7&s=4&page=1&pagesize=20&cityId=201");
     #print(r.text)
     #第二种方法：
     payload={'mid': 7, 's': 4,'page':1,'pagesize':10,'cityId': 201};
     re=requests.get("https://selectcar.yiche.com/selectcarforapp",params=payload)
     #打印接口url
     print(re.url)
     #打印响应内容
     print(re.text)
     #打印json格式
     print(re.json())
     #文本形式
     print(re.content)
     #输出编码格式
     print(re.encoding)


if __name__ == '__main__':
    unittest.main()
