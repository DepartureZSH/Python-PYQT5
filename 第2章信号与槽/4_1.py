import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import *

class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.resize(300, 300)                                   # 窗口初始化为宽300，长300
        self.setWindowTitle('demo')                             # 窗口名称：“demo”
        self.button = QPushButton('Start', self)
        #self.button.setIcon(QIcon('u.jpg'))
        self.button.clicked.connect(self.change_window_size)    # 连接connect信号clicked(按钮被点击)与槽函数change_window_size
        self.button.clicked.connect(self.change_window_title)   # 连接connect信号clicked(按钮被点击)与槽函数change_window_title
        self.button.clicked.connect(self.change_text)                   # 连接connect信号clicked(按钮被点击)与槽函数change_text

    def change_text(self):                                              # start转换为stop
        print('change text')
        if self.button.text() == 'Start':
            self.button.setText('Stop')
        else:
            self.button.setText('Start')

    def change_window_size(self):                               # 改变窗口大小
        print('change window size')
        if self.button.text() == 'Start':
            self.resize(500, 500)
        else:
            self.resize(300, 300)

    def change_window_title(self):                              # 改变窗口名称
        print('change window title')
        if self.button.text() == 'Start':
            self.setWindowTitle('window title changed')
        else:
            self.setWindowTitle('demo')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())