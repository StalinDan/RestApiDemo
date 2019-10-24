# -*- coding:utf-8 -*-
import requests
#导入登录接口
from upload import tclogin
#调用登录获取返回值
data = tclogin.testertechnologylogin()
#上传图片的方法
files = {
    'file': ('6.png',open('d:/6.png', "rb"), 'image/jpeg')}
url = "http://www.testertechnology.com:8081/upload/usericon/"+str(data)
#捕获异常
try:
    r = requests.post(url, files=files,timeout=1);
    aa=r.json()
    r.status_code
    #获取节点值
    code=aa['code'];
    print(code)
except TimeoutError:
    print("这个接口超过你设定的接口响应时间了，请排查");



# 打印json格式
