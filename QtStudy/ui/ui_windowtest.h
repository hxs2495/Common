/********************************************************************************
** Form generated from reading UI file 'windowtest.ui'
**
** Created by: Qt User Interface Compiler version 5.12.8
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_WINDOWTEST_H
#define UI_WINDOWTEST_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QGridLayout>
#include <QtWidgets/QHBoxLayout>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QPlainTextEdit>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QSpacerItem>
#include <QtWidgets/QTabWidget>
#include <QtWidgets/QVBoxLayout>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_windowTest
{
public:
    QGridLayout *gridLayout;
    QTabWidget *tabWidget;
    QWidget *tab;
    QVBoxLayout *verticalLayout_4;
    QSpacerItem *verticalSpacer;
    QHBoxLayout *horizontalLayout_2;
    QSpacerItem *horizontalSpacer;
    QVBoxLayout *verticalLayout_2;
    QVBoxLayout *verticalLayout_3;
    QLineEdit *lineEdit;
    QLineEdit *lineEdit_2;
    QHBoxLayout *horizontalLayout;
    QPushButton *pushButton;
    QPushButton *pushButton_exit;
    QSpacerItem *horizontalSpacer_2;
    QSpacerItem *verticalSpacer_2;
    QWidget *tab_2;
    QGridLayout *gridLayout_2;
    QPushButton *pushButton_request;
    QPushButton *pushButton_request_get;
    QPushButton *pushButton_request_post;
    QPushButton *pushButton_open_cv;
    QPushButton *pushButton_3;
    QWidget *tab_3;
    QVBoxLayout *verticalLayout_6;
    QPushButton *pushButton_open_file;
    QPlainTextEdit *plainTextEdit;
    QPushButton *pushButton_file_write;

    void setupUi(QWidget *windowTest)
    {
        if (windowTest->objectName().isEmpty())
            windowTest->setObjectName(QString::fromUtf8("windowTest"));
        windowTest->resize(768, 544);
        gridLayout = new QGridLayout(windowTest);
        gridLayout->setObjectName(QString::fromUtf8("gridLayout"));
        tabWidget = new QTabWidget(windowTest);
        tabWidget->setObjectName(QString::fromUtf8("tabWidget"));
        tabWidget->setDocumentMode(true);
        tab = new QWidget();
        tab->setObjectName(QString::fromUtf8("tab"));
        verticalLayout_4 = new QVBoxLayout(tab);
        verticalLayout_4->setObjectName(QString::fromUtf8("verticalLayout_4"));
        verticalSpacer = new QSpacerItem(20, 40, QSizePolicy::Minimum, QSizePolicy::Expanding);

        verticalLayout_4->addItem(verticalSpacer);

        horizontalLayout_2 = new QHBoxLayout();
        horizontalLayout_2->setObjectName(QString::fromUtf8("horizontalLayout_2"));
        horizontalSpacer = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        horizontalLayout_2->addItem(horizontalSpacer);

        verticalLayout_2 = new QVBoxLayout();
        verticalLayout_2->setSpacing(50);
        verticalLayout_2->setObjectName(QString::fromUtf8("verticalLayout_2"));
        verticalLayout_2->setContentsMargins(-1, -1, -1, 0);
        verticalLayout_3 = new QVBoxLayout();
        verticalLayout_3->setObjectName(QString::fromUtf8("verticalLayout_3"));
        lineEdit = new QLineEdit(tab);
        lineEdit->setObjectName(QString::fromUtf8("lineEdit"));
        QFont font;
        font.setPointSize(15);
        lineEdit->setFont(font);

        verticalLayout_3->addWidget(lineEdit);

        lineEdit_2 = new QLineEdit(tab);
        lineEdit_2->setObjectName(QString::fromUtf8("lineEdit_2"));
        lineEdit_2->setFont(font);
        lineEdit_2->setEchoMode(QLineEdit::Password);

        verticalLayout_3->addWidget(lineEdit_2);


        verticalLayout_2->addLayout(verticalLayout_3);

        horizontalLayout = new QHBoxLayout();
        horizontalLayout->setObjectName(QString::fromUtf8("horizontalLayout"));
        pushButton = new QPushButton(tab);
        pushButton->setObjectName(QString::fromUtf8("pushButton"));

        horizontalLayout->addWidget(pushButton);

        pushButton_exit = new QPushButton(tab);
        pushButton_exit->setObjectName(QString::fromUtf8("pushButton_exit"));

        horizontalLayout->addWidget(pushButton_exit);


        verticalLayout_2->addLayout(horizontalLayout);


        horizontalLayout_2->addLayout(verticalLayout_2);

        horizontalSpacer_2 = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        horizontalLayout_2->addItem(horizontalSpacer_2);


        verticalLayout_4->addLayout(horizontalLayout_2);

        verticalSpacer_2 = new QSpacerItem(20, 40, QSizePolicy::Minimum, QSizePolicy::Expanding);

        verticalLayout_4->addItem(verticalSpacer_2);

        tabWidget->addTab(tab, QString());
        tab_2 = new QWidget();
        tab_2->setObjectName(QString::fromUtf8("tab_2"));
        gridLayout_2 = new QGridLayout(tab_2);
        gridLayout_2->setObjectName(QString::fromUtf8("gridLayout_2"));
        pushButton_request = new QPushButton(tab_2);
        pushButton_request->setObjectName(QString::fromUtf8("pushButton_request"));

        gridLayout_2->addWidget(pushButton_request, 0, 0, 1, 1);

        pushButton_request_get = new QPushButton(tab_2);
        pushButton_request_get->setObjectName(QString::fromUtf8("pushButton_request_get"));

        gridLayout_2->addWidget(pushButton_request_get, 1, 0, 1, 1);

        pushButton_request_post = new QPushButton(tab_2);
        pushButton_request_post->setObjectName(QString::fromUtf8("pushButton_request_post"));

        gridLayout_2->addWidget(pushButton_request_post, 2, 0, 1, 1);

        pushButton_open_cv = new QPushButton(tab_2);
        pushButton_open_cv->setObjectName(QString::fromUtf8("pushButton_open_cv"));

        gridLayout_2->addWidget(pushButton_open_cv, 3, 0, 1, 1);

        pushButton_3 = new QPushButton(tab_2);
        pushButton_3->setObjectName(QString::fromUtf8("pushButton_3"));

        gridLayout_2->addWidget(pushButton_3, 4, 0, 1, 1);

        tabWidget->addTab(tab_2, QString());
        tab_3 = new QWidget();
        tab_3->setObjectName(QString::fromUtf8("tab_3"));
        verticalLayout_6 = new QVBoxLayout(tab_3);
        verticalLayout_6->setObjectName(QString::fromUtf8("verticalLayout_6"));
        pushButton_open_file = new QPushButton(tab_3);
        pushButton_open_file->setObjectName(QString::fromUtf8("pushButton_open_file"));

        verticalLayout_6->addWidget(pushButton_open_file);

        plainTextEdit = new QPlainTextEdit(tab_3);
        plainTextEdit->setObjectName(QString::fromUtf8("plainTextEdit"));

        verticalLayout_6->addWidget(plainTextEdit);

        pushButton_file_write = new QPushButton(tab_3);
        pushButton_file_write->setObjectName(QString::fromUtf8("pushButton_file_write"));

        verticalLayout_6->addWidget(pushButton_file_write);

        tabWidget->addTab(tab_3, QString());

        gridLayout->addWidget(tabWidget, 0, 0, 1, 1);


        retranslateUi(windowTest);

        tabWidget->setCurrentIndex(0);


        QMetaObject::connectSlotsByName(windowTest);
    } // setupUi

    void retranslateUi(QWidget *windowTest)
    {
        windowTest->setWindowTitle(QApplication::translate("windowTest", "QT&C++\345\255\246\344\271\240", nullptr));
        lineEdit->setPlaceholderText(QApplication::translate("windowTest", "\350\264\246\345\217\267", nullptr));
        lineEdit_2->setPlaceholderText(QApplication::translate("windowTest", "\345\257\206\347\240\201", nullptr));
        pushButton->setText(QApplication::translate("windowTest", "\347\231\273\351\231\206", nullptr));
        pushButton_exit->setText(QApplication::translate("windowTest", "\351\200\200\345\207\272", nullptr));
        tabWidget->setTabText(tabWidget->indexOf(tab), QApplication::translate("windowTest", "\344\270\273\347\225\214\351\235\242", nullptr));
        pushButton_request->setText(QApplication::translate("windowTest", "\350\257\267\346\261\202\346\265\213\350\257\225", nullptr));
        pushButton_request_get->setText(QApplication::translate("windowTest", "get\350\257\267\346\261\202\346\265\213\350\257\225", nullptr));
        pushButton_request_post->setText(QApplication::translate("windowTest", "post\350\257\267\346\261\202\346\265\213\350\257\225", nullptr));
        pushButton_open_cv->setText(QApplication::translate("windowTest", "\346\211\223\345\274\200\346\221\204\345\203\217\345\244\264", nullptr));
        pushButton_3->setText(QApplication::translate("windowTest", "\346\265\213\350\257\225\346\225\270\346\223\232\345\272\253", nullptr));
        tabWidget->setTabText(tabWidget->indexOf(tab_2), QApplication::translate("windowTest", "\346\265\213\350\257\225\347\225\214\351\235\242", nullptr));
        pushButton_open_file->setText(QApplication::translate("windowTest", "\350\257\273\345\217\226\346\226\207\344\273\266", nullptr));
        pushButton_file_write->setText(QApplication::translate("windowTest", "\345\206\231\345\205\245\346\226\207\344\273\266", nullptr));
        tabWidget->setTabText(tabWidget->indexOf(tab_3), QApplication::translate("windowTest", "\346\226\207\344\273\266\346\223\215\344\275\234", nullptr));
    } // retranslateUi

};

namespace Ui {
    class windowTest: public Ui_windowTest {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_WINDOWTEST_H
