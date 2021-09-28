import sys
from PyQt5.QtCore import pyqtSignal                             # 导入pyqtSignal
from PyQt5.QtWidgets import QApplication, QWidget, QLabel


class Demo(QWidget):
    my_signal = pyqtSignal()                                    # 实例化一个自定义的信号

    def __init__(self):
        super(Demo, self).__init__()
        self.label = QLabel('Hello World', self)
        self.my_signal.connect(self.change_text)                # 连接connect自定义信号my_signal与槽函数change_text

    def change_text(self):
        if self.label.text() == 'Hello World':
            self.label.setText('Hello PyQt5')
        else:
            self.label.setText('Hello World')

    def mousePressEvent(self, QMouseEvent):                     # 该方法控件自带，用来监测鼠标是否有按下
        self.my_signal.emit()                                                       #现在鼠标若被按下，则会发出自定义的信号

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())