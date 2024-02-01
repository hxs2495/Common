#!/usr/bin/python
# -*- coding: UTF-8 -*-
def get_cpuid():
    """获取机器人cpuid"""
    cpuid = '111114'
    # result = subprocess.run("cat_serial.sh", stdout=subprocess.PIPE, text=True)
    # key, cpuid = result.stdout.split(":", 1)
    # cpuid = cpuid.strip()
    # print(cpuid)
    return cpuid


def get_sip():
    """获取机器人用户固定sip号码"""
    sip = '111114'
    return sip
