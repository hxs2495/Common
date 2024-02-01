#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""自然语言词法分析功能接口"""
import base64
import hashlib
import json
import time
import urllib.parse
import urllib.request

# 接口地址
url = "http://ltpapi.xfyun.cn/v1/cws"
# 开放平台应用ID
x_appid = "7765c87b"
# 开放平台应用接口秘钥
api_key = "1341c4c185feda5c383176492781ced2"


def receive_messages(text):
    body = urllib.parse.urlencode({'text': text}).encode('utf-8')
    param = {"type": "dependent"}
    x_param = base64.b64encode(json.dumps(param).replace(' ', '').encode('utf-8'))
    x_time = str(int(time.time()))
    x_checksum = hashlib.md5(api_key.encode('utf-8') + str(x_time).encode('utf-8') + x_param).hexdigest()
    x_header = {'X-Appid': x_appid,
                'X-CurTime': x_time,
                'X-Param': x_param,
                'X-CheckSum': x_checksum}
    req = urllib.request.Request(url, body, x_header)
    result = urllib.request.urlopen(req)
    result = result.read()
    print(result.decode('utf-8'))
    return


if __name__ == '__main__':
    # 语言文本
    TEXT = "汉皇重色思倾国，御宇多年求不得。杨家有女初长成，养在深闺人未识。天生丽质难自弃，一朝选在君王侧。"
    receive_messages(TEXT)
