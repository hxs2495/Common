# -*- coding: utf-8 -*-
"""
语音播报相关功能接口
"""


# 语音播报功能函数
def text_to_speech(text, filename):
    from aip import AipSpeech

    # 百度开放平台调用参数，后续需要申请企业版，存入配置文件中
    app_id = '45226577'
    api_key = 'm1kWMSCxgNy20LyqbuAgz93d'
    secret_key = 'eStb6oyKHZukp6mAzfpLn7BktQRQWMEQ'
    client = AipSpeech(app_id, api_key, secret_key)

    result = client.synthesis(text, 'zh', 1, {
        'vol': 4,  # vol	String	音量，取值0-15，默认为5中音量	否
        'per': 0,  # per	String	发音人选择, 0为女声，1为男声，3为情感合成-度逍遥，4为情感合成-度丫丫，默认为普通女	否
        'spd': 5,  # spd	String	语速，取值0-9，默认为5中语速	否
        'pit': 4,  # pit	String	音调，取值0-9，默认为5中语调	否
    })

    if isinstance(result, dict):
        print(result)
        print('语音合成失败')
        return

    path = f"conf/static/voice/{filename}.mp3"
    with open(path, 'wb') as f:
        f.write(result)

    start_broadcast(path)
    print(path)
    return path


def start_broadcast(path):
    import pygame
    # 初始化pygame
    pygame.init()
    # 创建音频对象
    pygame.mixer.music.load(path)
    # 播放音频文件
    pygame.mixer.music.play()
    # 等待音频播放完毕
    while pygame.mixer.music.get_busy():
        pass


def stop_broadcast():
    import pygame

    pygame.mixer.init()  # 初始化mixer模块
    if pygame.mixer.music.get_busy():
        pygame.mixer.music.stop()
    pygame.quit()
