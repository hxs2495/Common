#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""自然灾害预警相关功能接口"""
import requests
from PyQt5.QtCore import QThread, pyqtSignal
from loguru import logger

from lib.common_function import config

province = config.get('address', 'province')
city = config.get('address', 'city')
district = config.get('address', 'district')


class WeatherThread(QThread):
    send_early_warning_list = pyqtSignal(list)
    send_early_warning_str = pyqtSignal(str)

    def check_warning(self):
        url = "http://www.12379.cn/data/alarm_list_all.html"
        data_list = []
        try:
            res = requests.post(url, timeout=None)
            res.encoding = 'utf-8'
            json_dict = res.json()
            # 判断是否有对应城市预警信息及类型
            for data_dict in json_dict['alertData']:
                if province in data_dict['headline'] or city in data_dict['headline'] or district in data_dict[
                    'headline'] \
                        or city in data_dict['description'] or district in data_dict['description']:
                    self.trigger_alarm(data_dict)
                    data_list.append(data_dict)
            self.send_early_warning_list.emit(data_list)
        except requests.exceptions.RequestException as e:
            logger.debug(f"网络请求异常:{e}")

    def trigger_alarm(self, data_dict):
        # 在这里触发警报的代码逻辑
        # 从headline字段中提取等级描述
        start_index = data_dict['headline'].find('[') + 1
        end_index = data_dict['headline'].find(']')
        level_description = data_dict['headline'][start_index:end_index]
        # 根据不同预警等级进行不同处理
        if 'IV级' in level_description:
            logger.debug('IV级/一般，蓝色预警信息')
        elif 'III级' in level_description:
            logger.debug('III级/较重，黄色预警信息')
            self.send_early_warning_str.emit(data_dict['headline'])
        elif 'Ⅱ级' in level_description:
            logger.debug('Ⅱ级/严重，橙色预警信息')
        elif 'Ⅰ级' in level_description:
            logger.debug('Ⅰ级/特别严重，红色预警信息')

    def get_weather_data(self, formatted_date):
        url = f"https://devapi.qweather.com/v7/weather/7d?location=101220101&key=f7306a94be7c49d8a05c7d6e00cf02a6"
        response = requests.get(url)
        data_list = response.json().get('daily', '')
        # print(data_list)
        for data_dict in data_list:
            if data_dict['fxDate'] == formatted_date:
                text_data = self.translate_weather_data(data_dict)
                return text_data

    def translate_weather_data(self, weather_dict):
        """组织生成天气预报文本"""
        output = []
        output.append(f"天气预报日期：{weather_dict.get('fxDate', '')}")
        output.append(f"白天天气状况：{weather_dict.get('textDay', '')}")
        output.append(f"夜间天气状况：{weather_dict.get('textNight', '')}")
        output.append(f"最高温度：{weather_dict.get('tempMax', '')}°C")
        output.append(f"最低温度：{weather_dict.get('tempMin', '')}°C")
        output.append(f"湿度：{weather_dict.get('humidity', '')}%")
        output.append(f"降水量：{weather_dict.get('precip', '')}mm")
        output.append(f"紫外线指数：{weather_dict.get('uvIndex', '')}")
        output.append(f"气压：{weather_dict.get('pressure', '')}hPa")
        output.append(f"能见度：{weather_dict.get('vis', '')}km")
        output.append(f"白天风向角度：{weather_dict.get('wind360Day', '')}°")
        output.append(f"白天风向：{weather_dict.get('windDirDay', '')}")
        output.append(f"白天风速：{weather_dict.get('windSpeedDay', '')}m/s")
        output.append(f"夜间风向角度：{weather_dict.get('wind360Night', '')}°")
        output.append(f"夜间风向：{weather_dict.get('windDirNight', '')}")
        output.append(f"夜间风速：{weather_dict.get('windSpeedNight', '')}m/s")
        output.append(f"日出时间：{weather_dict.get('sunrise', '')}")
        output.append(f"日落时间：{weather_dict.get('sunset', '')}")
        output.append(f"月升时间：{weather_dict.get('moonrise', '')}")
        output.append(f"月落时间：{weather_dict.get('moonset', '')}")
        # output += f"夜间风力等级：{weather_dict['windScaleNight']},"
        # output += f"白天风力等级：{weather_dict['windScaleDay']},"
        # output += f"月相：{weather_dict['moonPhase']},"
        # output += f"月相图标：{weather_dict['moonPhaseIcon']},"
        # output += f"白天天气图标：{weather_dict['iconDay']},"
        # output += f"夜间天气图标：{weather_dict['iconNight']},"
        # output += f"云量：{weather_dict['cloud']}%"
        return ", ".join(output)

    def run(self):
        self.check_warning()

        # while True:
        #     self.check_warning()
        #     time.sleep(600)  # 每隔600秒检查一次预警信息
