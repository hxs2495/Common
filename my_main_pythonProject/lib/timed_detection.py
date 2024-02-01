#!/usr/bin/python
# -*- coding: UTF-8 -*-
from apscheduler.schedulers.background import BackgroundScheduler


def my_job1():
    print("执行定时任务1")


def my_job2():
    print("执行定时任务2")


if __name__ == '__main__':
    # 创建调度器
    scheduler = BackgroundScheduler()
    # 定义一个要执行的任务
    # 添加任务到调度器，使用IntervalScheduler，每隔5秒执行一次
    scheduler.add_job(my_job1, 'interval', seconds=5)
    scheduler.add_job(my_job2, 'interval', seconds=2)
    # 启动调度器
    scheduler.start()
    try:

        # 这里可以添加一些其他的主线程逻辑，让程序保持运行
        scheduler.print_jobs()
        while True:
            pass
    except (KeyboardInterrupt, SystemExit):
        # 如果接收到终止信号，关闭调度器
        scheduler.shutdown()
