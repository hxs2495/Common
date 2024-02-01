
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QVBoxLayout, QWidget, QScrollArea, QPushButton
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        scroll_area = QScrollArea()
        scroll_widget = QWidget()
        scroll_layout = QVBoxLayout()
        scroll_widget.setLayout(scroll_layout)

        # 添加一些文本内容到滚动区域
        for i in range(100):
            label = QTextEdit(f'Text {i}')
            label.setReadOnly(True)
            scroll_layout.addWidget(label)

        scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        scroll_area.setWidgetResizable(True)
        scroll_area.setWidget(scroll_widget)

        button = QPushButton('滑动到底部')
        button.clicked.connect(self.scroll_to_bottom)

        main_layout = QVBoxLayout()
        main_layout.addWidget(scroll_area)
        main_layout.addWidget(button)

        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

    def scroll_to_bottom(self):
        # 获取垂直滚动条
        scrollbar = self.centralWidget().layout().itemAt(0).widget().verticalScrollBar()
        # 将滚动条的值设置为最大值
        scrollbar.setValue(scrollbar.maximum())

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
