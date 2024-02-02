#include <QCoreApplication>
#include <QDebug>
#include <QApplication>
#include <QFile>
#include <iostream>
#include "headers/main_window.h"

using namespace std;

void applyStylesheet(QApplication &app, const QString &qss_file) {
    QFile file(qss_file);
    if (file.open(QIODevice::ReadOnly | QIODevice::Text)) {
        QByteArray style_data = file.readAll();
        file.close();
        app.setStyleSheet(QString::fromUtf8(style_data));
    } else {
        qDebug() << "无法打开QSS文件:" << qss_file;
    }
}


int main(int argc, char *argv[]) {

    QApplication app(argc, argv);
    applyStylesheet(app, "../static/qss/balck_qss.qss");
    windowTest w;
    w.show();
    return QCoreApplication::exec();
//    int var = 20;   // 实际变量的声明
//    int *ip;        // 指针变量的声明
//
//    ip = &var;       // 在指针变量中存储 var 的地址
//
//    cout << "变量 var 的值是：";
//    cout << var << &var << endl;
//    cout << "变量 var 的地址是：";
//    cout << &var << endl;
//
//    // 输出在指针变量中存储的地址
//    cout << "指针 ip 指向的地址是：";
//    cout << ip << endl;
//
//    // 访问指针中地址的值
//    cout << "指针 ip 指向的地址存的变量的值是：";
//    cout << *ip << endl;
//
//
//    return 0;
}

