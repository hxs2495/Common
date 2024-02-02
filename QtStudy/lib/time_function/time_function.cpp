//
// Created by hxs on 2023/12/29.
//
#include <iostream>
#include <ctime>

using namespace std;

void get_time() {
    // 基于当前系统的当前日期/时间
    time_t now = time(0);

    // 把 now 转换为字符串形式
    char *dt = ctime(&now);

    cout << "本地日期和时间：" << dt << endl;

    // 把 now 转换为 tm 结构
    tm *gmtm = gmtime(&now);
    dt = asctime(gmtm);
    cout << "UTC 日期和时间：" << dt << endl;
}

//输出结果：
//本地日期和时间：Fri Sep 15 06:44:51 2023
//UTC 日期和时间：Fri Sep 15 06:44:51 2023
