# # -*- coding: utf-8 -*-
# """蓝牙功能接口"""
# from PyQt5 import QtCore
# from PyQt5 import QtBluetooth as QtBt
# from loguru import logger
#
#
# class BlueTooth:
#     def __init__(self, select_pushbutton, connect_pushbutton, bluetooth_listwidget):
#         super().__init__()
#         self.ble = None
#         self.timer = None
#         self.ble_connect_controller = None
#         self.ble_service_controller = None
#         self.ble_characteristic_write_controller = None
#         self.bel_characteristic_read_controller = None
#         self.ble_characteristic_notification_controller = None
#         self.device_name = ''
#         self.ble_device_arr = []
#         self.ble_select_device = []
#         self.ble_select_device_id = ''
#         self.search_service_arr = []
#         self.ble_service_arr = []
#         self.ble_select_service_id = ''
#         self.select_pushButton = select_pushbutton
#         self.connect_pushButton = connect_pushbutton
#         self.select_pushButton.clicked.connect(self.ble_scan_devices)
#         self.connect_pushButton.clicked.connect(self.ble_connect_devices)
#         self.bluetooth_listWidget = bluetooth_listwidget
#         self.bluetooth_listWidget.currentItemChanged.connect(self.item_clicked)
#         # self.ble_scan_devices()
#
#     def item_clicked(self, current_item):
#         print("当前文本:", current_item.text())
#         current_index = self.bluetooth_listWidget.row(current_item)  # 获取当前单元格的索引位置
#         print("当前单元格索引：", current_index)
#         if len(self.ble_select_device):
#             self.ble_select_device = []
#             self.ble.ble_select_device_id = ''
#
#         self.ble_select_device = self.ble_device_arr[current_index]
#         self.ble.ble_select_device_id = self.ble_select_device['address']
#         print("ble_select_device", self.ble_select_device, "ble_select_device_id", self.ble.ble_select_device_id)
#
#     def ble_finished(self):
#         logger.info("....蓝牙搜索回调....")
#         for dev in self.ble.discoveredDevices():
#             info = {
#                 "name": dev.name(),
#                 "address": dev.address().toString(),
#                 "rssi": dev.rssi(),
#                 "dev": dev
#             }
#             if self.device_name:
#                 if info['name'].find(self.device_name) != -1:
#                     self.ble_device_arr.append(info)
#             else:
#                 self.ble_device_arr.append(info)
#
#     def ble_display_status(self):
#         logger.info("....定时器判断搜索状态....")
#         self.timer.stop()
#         if len(self.ble_device_arr):
#             self.ble_device_arr = self.device_rssi_sort(self.ble_device_arr)
#         self.get_table_data()
#
#         # 根据信号值排序函数
#
#     def device_rssi_sort(self, arr):
#         logger.info("....根据信号值排序函数....")
#         self.min = {}
#         if len(arr):
#             for i in range(len(arr)):
#                 for j in range(i, len(arr)):
#                     if arr[i]['rssi'] < arr[j]['rssi']:
#                         self.min = arr[j]
#                         arr[j] = arr[i]
#                         arr[i] = self.min
#         return arr
#
#     # 获取列表数据函数
#     def get_table_data(self):
#         logger.info("....获取列表数据函数....")
#         # print("获取列表数据函数",self.ble_device_arr)
#
#         for (key, value) in enumerate(self.ble_device_arr):
#             print(key, value)
#             self.bluetooth_listWidget.addItem(value["name"])
#
#     # 扫描周边蓝牙设备函数
#     def ble_scan_devices(self):
#         logger.info("....扫描周边蓝牙设备....")
#         self.bluetooth_listWidget.clear()
#         self.ble_device_arr = []
#         self.ble = QtBt.QBluetoothDeviceDiscoveryAgent()
#         self.ble.setLowEnergyDiscoveryTimeout(3000)
#         # 过滤低功率蓝牙
#         self.ble.finished.connect(self.ble_finished)
#         self.ble.start()
#         self.timer = QtCore.QTimer(self.ble)
#         self.timer.start(8000)  # 5秒搜索结束
#         self.timer.timeout.connect(self.ble_display_status)
#
#     # 连接设备函数
#     def ble_connect_devices(self):
#         logger.info("....连接蓝牙设备....")
#         try:
#             self.ble_connect_controller = QtBt.QLowEnergyController.createCentral(self.ble_select_device['dev'])
#         except:
#             pass
#         else:
#             self.ble_connect_controller.connected.connect(self.ble_connect_notify)
#             self.ble_connect_controller.disconnected.connect(self.ble_disconnect_notify)
#             self.ble_connect_controller.serviceDiscovered.connect(self.ble_service_discovered)
#             self.ble_connect_controller.discoveryFinished.connect(self.ble_service_finished)
#             self.ble_connect_controller.connectToDevice()
#
#     def ble_connect_notify(self, *args, **kwargs):
#         self.ble_service_arr = list()
#         self.ble_connect_controller.discoverServices()
#         logger.info("....连接通知....")
#
#         # 连接断开函数
#
#     @staticmethod
#     def ble_disconnect_notify(*args, **kwargs):
#         logger.info("....断开设备连接....")
#
#     def ble_service_discovered(self, uuid: QtBt.QBluetoothUuid):
#         logger.info("....正在获取设备的服务ID....")
#         bluetooth_item = {
#             "name": uuid.toString(),
#             "value": uuid
#         }
#         print(bluetooth_item)
#         self.ble_service_arr.append(bluetooth_item)
#
#     def ble_service_finished(self):
#         logger.info("....获取设备的服务ID完成....")
#         logger.info("....蓝牙设备连接成功....")
