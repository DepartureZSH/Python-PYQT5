import sys
from PyQt5.QtCore import QPropertyAnimation, QPoint
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton


class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.resize(600, 600)

        self.btn = QPushButton('Move', self)
        self.btn.resize(100, 100)

        self.animation = QPropertyAnimation(self.btn, b'pos')   # pos属性可变
        self.animation.setDuration(5000)
        # 使用QPoint让按钮在5秒内从坐标(0, 0)移动到(500, 500)
        self.animation.setStartValue(QPoint(0, 0))
        self.animation.setEndValue(QPoint(500, 500))
        self.animation.start()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
