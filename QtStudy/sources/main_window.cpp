//
// Created by hxs on 2023/12/26.
//

#include "../headers/main_window.h"
#include "../ui/ui_windowtest.h"
#include "../lib/db_hander/db_hander.cpp"
#include "../lib/request_function/request.cpp"
#include "../lib/request_function/get_post_request.cpp"
#include "../lib/opencv_video/opencv_function.cpp"
#include "../lib/file_hander/file_hander.cpp"
#include <iostream>
#include <jsoncpp/json/json.h>
#include <QMovie>
#include <QLabel>

windowTest::windowTest(QWidget *parent) :
        QWidget(parent), ui(new Ui::windowTest) {
    ui->setupUi(this);
//    // 加载背景图片
//    QPixmap pixmap("../static/img/keji.png");
//
//    // 设置背景图片
//    QPalette palette;
//    palette.setBrush(QPalette::Background, pixmap);
//    this->setPalette(palette);

    // 为按钮绑定事件 connect(信号的发送者,发送的信号,信号的接受者,处理的函数(槽函数))
    connect(ui->pushButton_exit, &QPushButton::clicked, this, &QWidget::close);

    connect(ui->pushButton, &QPushButton::clicked, this, &windowTest::test_print);
    connect(ui->pushButton_3, &QPushButton::clicked, this, &windowTest::test_db);
    connect(ui->pushButton_request, &QPushButton::clicked, this, &windowTest::test_request);
    connect(ui->pushButton_request_get, &QPushButton::clicked, this, &windowTest::test_request_get);
    connect(ui->pushButton_request_post, &QPushButton::clicked, this, &windowTest::test_request_post);
    connect(ui->pushButton_open_cv, &QPushButton::clicked, this, &windowTest::test_open_video);
    connect(ui->pushButton_open_file, &QPushButton::clicked, this, &windowTest::test_open_file);
    connect(ui->pushButton_file_write, &QPushButton::clicked, this, &windowTest::test_write_file);

}

windowTest::~windowTest() {
    delete ui;
}

void windowTest::resizeEvent(QResizeEvent *event) {
    QWidget::resizeEvent(event);
    // 加载背景图片
    QPixmap pixmap("../static/img/keji.png");
    // 将图片缩放到和窗口一样的大小
    pixmap = pixmap.scaled(size(), Qt::IgnoreAspectRatio);
    // 设置背景图片
    QPalette palette;
    palette.setBrush(QPalette::Background, pixmap);
    this->setPalette(palette);
}

//void windowTest::resizeEvent(QResizeEvent *event) {
//    QWidget::resizeEvent(event);
//
//    // 创建QMovie对象并加载动态图片
//    QMovie *movie = new QMovie("../static/img/11.gif");
//
//    // 将QMovie对象关联到标签上
//    QLabel *label = new QLabel(this);
//    label->setMovie(movie);
//
//    // 设置标签大小和窗口一样大
//    label->setGeometry(0, 0, width(), height());
//
//    // 播放动态图片
//    movie->start();
//}


void windowTest::test_print() {
    qDebug() << "测试输出";
    QMessageBox::information(this, "提示", "测试输出...");
}

void windowTest::test_db() {
    db_hander_function();
}

void windowTest::test_request() {

    http_request("www.baidu.com", [](std::string const &response) {
        std::cout << "收到的回复: " << response << "\n";
    });
}

void windowTest::test_request_get() {

    // 发送 GET 请求并解析 JSON 数据
    std::string get_url = "http://192.168.1.27:5004/data/";
    Json::Value get_data = send_get_request(get_url);
}

void windowTest::test_request_post() {

    // 发送 POST 请求并解析 JSON 数据
    std::string post_url = "http://192.168.1.27:5004/data/";
    std::string post_data = "key1=value1&key2=value2";
    Json::Value post_result = send_post_request(post_url, post_data);
}

void windowTest::test_open_video() {

    open_video();
}

void windowTest::test_open_file() {
    // 测试读取文件
    std::string filename = "../static/file/test_file.txt";
    std::string content = readFile(filename);
    std::cout << "文件内容：" << std::endl;
    std::cout << content << std::endl;
    // 将文件内容写入 plainTextEdit
    QString plainText = QString::fromStdString(content);
    ui->plainTextEdit->setPlainText(plainText);
}

void windowTest::test_write_file() {
    // 获取 plainTextEdit 中的文本内容
    QString plainText = ui->plainTextEdit->toPlainText();
    // 将文本内容写入指定文件
    std::string newContent = plainText.toStdString();
    writeFile("../static/file/test_file.txt", newContent);
}
