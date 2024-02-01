# -*- coding: utf-8 -*-
"""sip通信功能接口"""
import re
import subprocess
import threading
import time

import psutil as psutil
from PyQt5.QtCore import QThread, pyqtSignal
from loguru import logger

from lib.requests_function.requests_server import get_user_isbusy


class LinphonecThread(QThread):
    """Linphone中文命令：
        - help：打印命令帮助。
        - answer：接听电话。
        - autoanswer：显示/设置自动接听模式。
        - call：拨打SIP URI或号码。
        - calls：显示当前所有通话及其ID和状态。
        - call-logs：通话记录。
        - camera：发送当前通话的摄像头输出。
        - chat：与SIP URI进行聊天。
        - conference：创建和管理音频会议。
        - duration：打印上一个通话的持续时间（以秒为单位）。
        - firewall：设置防火墙策略。
        - friend：管理好友。
        - ipv6：使用IPV6。
        - mute：静音麦克风并暂停语音传输。
        - nat：设置NAT地址。
        - pause：暂停通话。
        - play：播放WAV文件。
        - playbackgain：调整播放增益。
        - proxy：管理代理服务器。
        - record：录制到WAV文件。
        - resume：恢复通话。
        - soundcard：管理声卡。
        - stun：设置STUN服务器地址。
        - terminate：终止通话。
        - transfer：将通话转移到指定目的地。
        - unmute：取消静音麦克风并恢复语音传输。
        - webcam：管理网络摄像头。
        - quit：退出linphonec
    """
    send_recording_result = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.config_file = 'conf/linphone/ipv4linphonerc.ini'
        self.address = "fs4.icare.link"
        # 创建一个锁对象来确保线程安全
        self.lock = threading.Lock()
        self.id = 1

    def _read_process_output(self, stream):
        """线程函数，循环读取并打印流"""
        while True:
            line = stream.readline()
            if not line:
                # 如果流已经关闭，则退出循环
                break
            # 使用锁来确保线程安全地打印输出
            with self.lock:

                linphonec_message = line.decode().strip()
                logger.debug(linphonec_message)
                if "Media streams established with" in linphonec_message:
                    self.send_recording_result.emit(f"正在通话中")
                elif "User is busy" in linphonec_message:
                    self.send_recording_result.emit(f"对方正在忙碌中，请稍候再拨")
                elif "Call terminated" in linphonec_message:
                    self.send_recording_result.emit(f"对方已挂断")
                elif "Receiving new incoming" in linphonec_message:
                    pattern = r'from\s+"(\w+)"\s+<(\S+)>,\s+assigned\s+id\s+(\d+)'
                    match = re.search(pattern, linphonec_message)
                    name, address_sip, self.id = match.groups()
                    # sip:111112@192.168.1.178
                    self.send_recording_result.emit(f"用户{name},号码{address_sip}来电,id{self.id}")
                    # 调用自动接听应答功能
                    self.auto_answer_function(address_sip=address_sip)
                elif "Terminating" in linphonec_message:
                    self.send_recording_result.emit("挂断成功")
                elif "successful" in linphonec_message:
                    self.send_recording_result.emit("注册成功，在线中")
                elif "Connected" in linphonec_message:
                    self.send_recording_result.emit("接听成功，正在通话中...")

    def find_process_by_port(self, port):
        for process in psutil.process_iter():
            try:
                connections = process.connections()
                if any(conn.laddr.port == port for conn in connections):
                    return process
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass
        return None

    def run(self):
        port = 5060
        process = self.find_process_by_port(port)
        if process:
            logger.debug(f"找到进程 {process.pid}，正在杀死...")
            process.kill()
        else:
            logger.debug(f"未找到使用端口 {port} 的进程")

        time.sleep(1)
        logger.debug('启动 linphonec 服务')
        command = ['linphonec', '-c', self.config_file]
        self.process = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        # 创建并启动一个线程来监测并打印标准输出信息
        output_thread = threading.Thread(target=self._read_process_output, args=(self.process.stdout,))
        output_thread.daemon = True
        output_thread.start()
        # 创建并启动一个线程来监测并打印标准错误信息
        error_thread = threading.Thread(target=self._read_process_output, args=(self.process.stderr,))
        error_thread.daemon = True
        error_thread.start()
        # 等待线程结束
        # error_thread.join()

    def audio_call(self, sipnum):
        state = get_user_isbusy(target_sip=sipnum).get("state")
        if not state:
            self.send_recording_result.emit(f"目标用户{sipnum}正在忙线通话中，请稍后再拨...")
            return

        try:
            command = f"call sip:{sipnum}@{self.address}\n"
            self.process.stdin.write(command.encode())
            self.process.stdin.flush()
            self.send_recording_result.emit(f"正在音频呼叫{sipnum}...")
        except:
            self.send_recording_result.emit(f"音频呼叫失败")

    def video_call(self, sipnum):
        state = get_user_isbusy(target_sip=sipnum).get("state")
        if not state:
            self.send_recording_result.emit(f"目标用户{sipnum}正在忙线通话中，请稍后再拨...")
            return
        # 重启linphonec,以视频方式拨打
        command = ['linphonec', '-V', '-c', self.config_file]
        self.videoprocess = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                             stderr=subprocess.PIPE)
        try:
            callcommand = f"call {sipnum}@{self.address}\n"
            self.process.stdin.write(callcommand.encode())
            self.process.stdin.flush()
            self.send_recording_result.emit(f"正在视频呼叫{sipnum}...")
        except:
            self.send_recording_result.emit(f"视频呼叫失败")

    def call_terminate(self):
        try:
            command = f"terminate\n"
            self.process.stdin.write(command.encode())
            self.process.stdin.flush()
            self.process.terminate()
        except:
            pass
        finally:
            logger.debug('执行terminate命令，退出linphonec进程')
            time.sleep(1)
            self.run()

    def answer_incoming_call(self):
        try:
            callcommand = f"answer {self.id}\n"
            # callcommand = f"accept\n"
            self.process.stdin.write(callcommand.encode())
            self.process.stdin.flush()
            # 等待一段时间以确保接听操作完成
            time.sleep(1)
        except:
            logger.debug('接听失败')

    def auto_answer_function(self, address_sip):
        sip = ''
        result = re.search(r'sip:(\d+)@', address_sip)
        if result:
            sip = result.group(1)
        else:
            logger.debug("未找到匹配的字符串")

        # 允许自动应答列表
        sip_auto_answer_list = ["111112", "111113", "1005", "1007", "1008"]

        if sip in sip_auto_answer_list:
            self.answer_incoming_call()
            logger.debug("来电用户在自动应答列表中，启动自动应答模式")
