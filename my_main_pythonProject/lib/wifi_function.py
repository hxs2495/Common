import asyncio
import os
import re
import socket
import subprocess
import time

import requests
from loguru import logger


class WifiFunction:
    WIFI_CONNECT_TIMEOUT = 1

    def is_wifi_connected(self):
        """
        检测wifi是否连接
        """
        output = subprocess.check_output(["nmcli"]).decode()
        if '不可用' in output:
            logger.debug('网络不可用')
            return False
        else:
            logger.debug('网络可用')
            return True

    def is_ipv6_or_ipv4(self):
        """
        判断网络类型并获取公网IP地址
        """
        try:
            sock = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)
            sock.connect(("2001:4860:4860::8888", 80))
            ipv6_address = socket.getaddrinfo(socket.gethostname(), None, socket.AF_INET6)[0][4][0]
            logger.debug('获取公网ipv6地址:' + ipv6_address)
            return True, ipv6_address
        except (socket.error, OSError):
            ip_resp = requests.get("http://httpbin.org/ip").json()
            ipv4_address = ip_resp.get('origin', '')
            logger.debug('获取公网ipv4地址:' + ipv4_address)
            return False, ipv4_address
        finally:
            sock.close()

    def select_wifi(self):
        """
        搜索附近的wifi
        """
        os.system('nmcli radio wifi on')
        time.sleep(self.WIFI_CONNECT_TIMEOUT)
        logger.debug('开始搜索附近的wifi')
        wlan_origin = os.popen("nmcli device wifi").readlines()
        wifi_names = re.findall(r'\s+(\S+)\s+Infra', str(wlan_origin))
        wifi_names = [name for name in wifi_names if name != '--']
        return wifi_names

    def connect_wifi(self, wifi_name, wifipassword):
        """
        连接wifi
        """
        os.system('nmcli radio wifi on')
        time.sleep(self.WIFI_CONNECT_TIMEOUT)
        proc = subprocess.Popen(f'nmcli device wifi connect {wifi_name} password {wifipassword}', shell=True,
                                stdout=subprocess.PIPE)
        return proc

    async def check_internet_connection(self, ip=None, hostname=None):
        """
        检查网络连接
        """
        if hostname:
            ip = socket.gethostbyname(hostname)
            logger.debug(f"解析域名{hostname}并获取IP地址{ip}")

        proc = await asyncio.create_subprocess_shell(
            f'ping -c 2 {ip}',
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )
        await proc.communicate()
        if proc.returncode == 0:
            logger.debug(f'{ip} 网络连通')
            return True
        else:
            logger.debug(f'{ip} 网络断开')
            return False

    async def main(self):
        tasks = [
            self.check_internet_connection(ip='192.168.0.10'),
            self.check_internet_connection(ip='192.168.1.136'),
            self.check_internet_connection(hostname="www.baidu.com")
        ]
        await asyncio.gather(*tasks)


# if __name__ == "__main__":
#     wifi = WifiFunction()
#     wifi.is_wifi_connected()
#     wifi.is_ipv6_or_ipv4()
