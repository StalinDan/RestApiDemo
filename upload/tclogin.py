# -*- coding:utf-8 -*-
import requests

#post接口请求
def testertechnologylogin():
    datanum = {
          "email": "1615266681@qq.com",
          "password": "guangyi77"
          }
    r = requests.post("http://www.testertechnology.com:8081/user/login", data=datanum);
    #得到接口返回值获取data传入到tcupload接口中
    #打印json值
    datajson=r.json();

    #获取节点的值
    data=datajson['data'];
    #返回调用
    return data;


# 打印json格式
#获取response中的cookies

