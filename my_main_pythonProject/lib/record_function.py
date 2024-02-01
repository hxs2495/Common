#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""语音识别监听功能接口"""
import _thread as thread
import base64
import hashlib
import hmac
import json
import ssl
import time
from datetime import datetime
from time import mktime
from urllib.parse import urlencode
from wsgiref.handlers import format_date_time

import pyaudio
import websocket
from PyQt5.QtCore import pyqtSignal, QThread
from loguru import logger

# from lib.voiceprint_recognition.mvector.predict import MVectorPredictor
# from lib.voiceprint_recognition.mvector.utils.record import RecordAudio

STATUS_FIRST_FRAME = 0  # 第一帧的标识
STATUS_CONTINUE_FRAME = 1  # 中间帧标识
STATUS_LAST_FRAME = 2  # 最后一帧的标识

# 定义一个列表
list_hq = ["小智", "小志", "小镇", "小制", "小吃", "小至", "小车", "想知", "想这", "小知", "小只", "人民", "小之",
           "小这", "小芝", "小枝"]


class RecordThread(QThread):
    """语音转文本功能"""
    send_recording_result = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.APPID = '458071bf'
        self.APIKey = '51933b655acb55dae65c18daec0ebbbe'
        self.APISecret = 'ODI1MDY5MWUzYzQyZWNmNmMwNWEzZDRl'
        # 公共参数(common)
        self.CommonArgs = {"app_id": self.APPID}
        # 业务参数(business)，更多个性化参数可在官网查看
        self.BusinessArgs = {"domain": "iat", "language": "zh_cn", "accent": "mandarin", "vinfo": 1, "vad_eos": 10000}
        self.create_url()
        self.is_running = False  # 线程运行状态的开关

    # 生成url
    def create_url(self):
        url = 'wss://ws-api.xfyun.cn/v2/iat'
        # 生成RFC1123格式的时间戳
        now = datetime.now()
        date = format_date_time(mktime(now.timetuple()))
        # 拼接字符串
        signature_origin = "host: " + "ws-api.xfyun.cn" + "\n"
        signature_origin += "date: " + date + "\n"
        signature_origin += "GET " + "/v2/iat " + "HTTP/1.1"
        # 进行hmac-sha256进行加密
        signature_sha = hmac.new(self.APISecret.encode('utf-8'), signature_origin.encode('utf-8'),
                                 digestmod=hashlib.sha256).digest()
        signature_sha = base64.b64encode(signature_sha).decode(encoding='utf-8')
        authorization_origin = "api_key=\"%s\", algorithm=\"%s\", headers=\"%s\", signature=\"%s\"" % (
            self.APIKey, "hmac-sha256", "host date request-line", signature_sha)
        authorization = base64.b64encode(authorization_origin.encode('utf-8')).decode(encoding='utf-8')
        # 将请求的鉴权参数组合为字典
        v = {
            "authorization": authorization,
            "date": date,
            "host": "ws-api.xfyun.cn"
        }
        # 拼接鉴权参数，生成url
        url = url + '?' + urlencode(v)
        # print("date: ",date)
        # print("v: ",v)
        # 此处打印出建立连接时候的url,参考本demo的时候可取消上方打印的注释，比对相同参数时生成的url与自己代码生成的url是否一致
        # print('websocket url :', url)
        return url

    # 收到websocket错误的处理
    def on_error(self, ws, error):
        # print("错误:", error)
        return

    # 收到websocket关闭的处理
    def on_close(self, ws):
        return

    # 收到websocket连接建立的处理
    def on_open(self, ws):
        def run(*args):
            status = STATUS_FIRST_FRAME  # 音频的状态信息，标识音频是第一帧，还是中间帧、最后一帧
            CHUNK = 520  # 定义数据流块
            FORMAT = pyaudio.paInt16  # 16bit编码格式
            CHANNELS = 1  # 单声道
            RATE = 16000  # 16000采样频率
            p = pyaudio.PyAudio()
            # 创建音频流
            stream = p.open(format=FORMAT,  # 音频流wav格式
                            channels=CHANNELS,  # 单声道
                            rate=RATE,  # 采样率16000
                            input=True,
                            frames_per_buffer=CHUNK)

            logger.debug("-----开始录制-----")
            for i in range(0, int(RATE / CHUNK * 60)):
                buf = stream.read(CHUNK)
                if not buf:
                    status = STATUS_LAST_FRAME
                if status == STATUS_FIRST_FRAME:

                    d = {"common": self.CommonArgs,
                         "business": self.BusinessArgs,
                         "data": {"status": 0, "format": "audio/L16;rate=16000",
                                  "audio": str(base64.b64encode(buf), 'utf-8'),
                                  "encoding": "raw"}}
                    d = json.dumps(d)

                    ws.send(d)
                    status = STATUS_CONTINUE_FRAME
                    # 中间帧处理
                elif status == STATUS_CONTINUE_FRAME:
                    d = {"data": {"status": 1, "format": "audio/L16;rate=16000",
                                  "audio": str(base64.b64encode(buf), 'utf-8'),
                                  "encoding": "raw"}}
                    ws.send(json.dumps(d))

                # 最后一帧处理
                elif status == STATUS_LAST_FRAME:
                    d = {"data": {"status": 2, "format": "audio/L16;rate=16000",
                                  "audio": str(base64.b64encode(buf), 'utf-8'),
                                  "encoding": "raw"}}
                    ws.send(json.dumps(d))
                    time.sleep(1)
                    break

            stream.stop_stream()
            stream.close()
            p.terminate()
            ws.close()

        thread.start_new_thread(run, ())

    # 收到websocket消息的处理
    def on_message(self, ws, message):
        try:
            code = json.loads(message)["code"]
            # sid = json.loads(message)["sid"]
            if code == 0:
                data = json.loads(message)["data"]["result"]["ws"]
                result = ""
                for i in data:
                    for w in i["cw"]:
                        result += w["w"]
                self.send_recording_result.emit(result)

        except Exception as e:
            logger.debug("接收消息解析异常:", e)

    # @staticmethod
    # def voiceprint_recognition():
    #     """声纹识别功能接口"""
    #     logger.debug('进行声纹验证')
    #     time.sleep(1)
    #     pass

    def run(self):
        # 在这里编写多线程执行的代码
        # self = Ws_Param()
        websocket.enableTrace(False)
        wsUrl = self.create_url()

        ws = websocket.WebSocketApp(wsUrl, on_message=self.on_message, on_error=self.on_error,
                                    on_close=self.on_close)
        ws.on_open = self.on_open
        ws.run_forever(sslopt={"cert_reqs": ssl.CERT_NONE}, ping_timeout=2)

# class VoicePrintRecognition:
#     """声纹识别功能"""
#     # send_voiceprintrecognition_result = pyqtSignal(str)
#
#     def __init__(self):
#         # 获取识别器
#         # super().__init__()
#         self.predictor = MVectorPredictor(configs='lib/voiceprint_recognition/configs/ecapa_tdnn.yml',
#                                           threshold=0.45,
#                                           audio_db_path='lib/voiceprint_recognition/audio_db/',
#                                           model_path='lib/voiceprint_recognition/EcapaTdnn_Fbank/best_model/',
#                                           use_gpu=False)
#         self.record_audio = RecordAudio()
#         self.record_seconds = 3
#         self.register_seconds = 5
#
#         self.stop_event = threading.Event()
#
#         self.max_len = 3
#         self.q = queue.Queue(maxsize=2)
#         self.data_deque = deque(maxlen=self.max_len)
#         self.recognizing = True
#
#     @staticmethod
#     def get_register_user():
#         folders = []
#         path = "lib/voiceprint_recognition/audio_db"
#         for item in os.listdir(path):
#             if os.path.isdir(os.path.join(path, item)):
#                 folders.append(item)
#         return folders
#
#     def voice_register(self, name):
#         # input(f"按下回车键开机录音，录音{self.register_seconds}秒中：")
#         audio_data = self.record_audio.record(record_seconds=self.register_seconds)
#         # name = input("请输入该音频用户的名称：")
#         if name != '':
#             self.predictor.register(user_name=name, audio_data=audio_data, sample_rate=self.record_audio.sample_rate)
#
#     def voice_recognition(self):
#         # input(f"按下回车键开机录音，录音{self.record_seconds}秒中：")
#         audio_data = self.record_audio.record(record_seconds=self.record_seconds)
#         name = self.predictor.recognition(audio_data, sample_rate=self.record_audio.sample_rate)
#         if name:
#             print(f"识别说话的为：{name}")
#             return True
#         else:
#             print(f"没有识别到说话人，可能是没注册。")
#             return False
#
#     def voice_delete(self):
#         name = input("请输入该音频用户的名称：")
#         if name != '':
#             self.predictor.remove_user(user_name=name)
#
#     def recognize_real(self):
#         threshold = 0.6
#
#         while self.recognizing:
#             self.data_deque.append(self.q.get())
#             if len(self.data_deque) != self.max_len: continue
#             audio_data = None
#             for data in self.data_deque:
#                 if audio_data is None:
#                     audio_data = data
#                 else:
#                     audio_data = np.concatenate((audio_data, data))
#             name = self.predictor.recognition(audio_data, threshold, sample_rate=self.record_audio.sample_rate)
#             print(name)
#             if name != None:
#                 self.stop_event.set()
#                 return
#
#     def record_real(self):
#         while self.recognizing:
#             audio_data = self.record_audio.record(record_seconds=3)
#             self.q.put(audio_data)
#             while self.stop_event.is_set():
#                 return
#
#     def recognize_thread(self):
#         max_len = int(self.record_seconds)
#         q = queue.Queue(maxsize=2)
#         data_deque = deque(maxlen=max_len)
#         threading.Thread(target=self.recognize_real).start()
#         threading.Thread(target=self.record_real).start()
#         while not self.stop_event.is_set():
#             pass
#         return 1
