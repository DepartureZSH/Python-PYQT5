import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QToolButton


class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.test_button = QToolButton(self)                        # 不能在QToolButton实例化的时候直接传入文本字符串
        self.test_button.setCheckable(True)
        self.test_button.setIcon(QIcon('button.png'))
        self.test_button.toggled.connect(self.button_state_func)
        self.test_button.isCheckable()

    def button_state_func(self):
        print(self.test_button.isChecked())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())