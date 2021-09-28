import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton


class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.resize(300, 300)                                   # 窗口初始化为宽300，长300
        self.setWindowTitle('demo')                             # 窗口名称：“demo”
        self.button = QPushButton('Start', self)
        self.button.clicked.connect(self.change_text)                     # 连接connect信号clicked(按钮被点击)与槽函数change_text
        self.button.clicked.connect(self.change_window_size)    # 连接connect信号clicked(按钮被点击)与槽函数change_window_size
        self.button.clicked.connect(self.change_window_title)   # 连接connect信号clicked(按钮被点击)与槽函数change_window_title

    def change_text(self):                                              # start转换为stop
        print('change text')
        self.button.setText('Stop')
        self.button.clicked.disconnect(self.change_text)

    def change_window_size(self):                               # 改变窗口大小
        print('change window size')
        self.resize(500, 500)
        self.button.clicked.disconnect(self.change_window_size)

    def change_window_title(self):                              # 改变窗口名称
        print('change window title')
        self.setWindowTitle('window title changed')
        self.button.clicked.disconnect(self.change_window_title)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())