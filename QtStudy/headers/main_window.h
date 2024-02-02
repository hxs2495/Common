//
// Created by hxs on 2023/8/29.
//

#ifndef QTPROJECT_WINDOWTEST_H
#define QTPROJECT_WINDOWTEST_H

#include <QWidget>
#include "QMessageBox"
#include <QPixmap>
#include "QDebug"


QT_BEGIN_NAMESPACE
namespace Ui { class windowTest; }
QT_END_NAMESPACE

class windowTest : public QWidget {
Q_OBJECT

public:
    explicit windowTest(QWidget *parent = nullptr);

    ~windowTest() override;

private:
    Ui::windowTest *ui;

    void resizeEvent(QResizeEvent *event);

    void test_print();

    void test_db();

    void test_request();

    void test_request_get();

    void test_request_post();

    void test_open_video();

    void test_open_file();

    void test_write_file();
};


#endif //QTPROJECT_WINDOWTEST_H
