# -*- coding: utf-8 -*-
"""
付费通话统计功能接口
"""
# from db.db_handler import get_or_send_mysqldata
#
#
# class CountCallMoney:
#     def get_freeswitch_data(self):
#         caller_id_number = 1003
#         destination_number = 1001
#         data = {'method': 'get_freeswitchdata', 'caller_id_number': caller_id_number,
#                 'destination_number': destination_number}
#         result = get_or_send_mysqldata(data=data)
#         # result = ast.literal_eval(result)
#         print(result)  # [{'caller_id_number': '1003', 'destination_number': '1001', 'start_timestamp': '2021-11-20 17:36:40', 'answer_timestamp': '2021-11-20 17:36:43', 'end_timestamp': '2021-11-20 17:36:48', 'duration': 8, 'billsec': 5}]
#         return result
