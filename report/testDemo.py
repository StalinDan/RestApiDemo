import unittest
import requests
#导入登录接口
from upload import tclogin
#调用登录获取返回值
data = tclogin.testertechnologylogin()
class MyTestCase(unittest.TestCase):
    '''汽车列表'''
    def test_one1(self):
        r=requests.get("https://selectcar.yiche.com/selectcarforapp?mid=7&s=4&page=1&pagesize=20&cityId=201")
        car=r.json();
        print(car)
        carname=car['data']['resList'][0]['name']
        self.assertEqual(carname,"卡罗")

    # '''登录后图片上传'''
    def test_one2(self):
        # 上传图片的方法
        files = {
            'file': ('6.JPG', open('/Users/danish/Downloads/DemoApi-1/image/6.JPG', "rb"), 'image/jpeg')}
        url = "http://www.testertechnology.com:8081/upload/usericon/" + str(data)
        # 捕获异常
        try:
            r = requests.post(url, files=files, timeout=1);
            aa = r.json()
            r.status_code
            # 获取节点值
            code = aa['code'];
            print(r.json())
            print(code)
        except TimeoutError:
            print("这个接口超过你设定的接口响应时间了，请排查");
    # '''登录'''
    def test_one3(self):
        datacon = {'email': '1615266681@qq.com', 'password': 'guangyi77'}
        r = requests.post("http://www.testertechnology.com:8081/user/login", data=datacon);
        print(r.text)
        print(r.status_code)
        print(r.headers)
        print(r.headers['Content-Type'])
        print(r.json())
    def test_one4(self):
        print("1223333");
    def test_one5(self):
        print("可能吧");

if __name__ == '__main__':
    unittest.main()
