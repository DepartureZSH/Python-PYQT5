import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton


class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.test_button = QPushButton('Test', self)
        self.test_button.setCheckable(True)                         # True: 按钮有两种状态，即0和1;False:按钮按下会弹起
        self.test_button.setIcon(QIcon('button.png'))               # 通过setIcon()方法给按钮设置一个图标，传入的参数为QIcon()
        self.test_button.toggled.connect(self.button_state_func)    # 连接信号toggled和槽函数button_state_func
        # 按钮标记状态发生变化就会发出toggled信号

    def button_state_func(self):
        print(self.test_button.isChecked())                         # 通过isChecked()方法来判断按钮是否为标记状态，若是则返回True，不是则返回False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())