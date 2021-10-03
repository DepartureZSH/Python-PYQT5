import sys
from PyQt5.QtCore import QPropertyAnimation, QSize
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton


class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.resize(600, 600)

        self.btn = QPushButton('Bigger', self)
        self.btn.resize(100, 100)

        self.animation = QPropertyAnimation(self.btn, b'size')
        # 将动画持续时间设为10秒，
        # 然后调用setKeyValueAt()方法在指定的时刻设置指定的大小(传入的第一个参数的值范围为0-1)
        # 下面代码的意思就是说：
        # 在0-3秒中将按钮大小从(100, 100)变为(200, 200)
        # 在3-8秒中将大小从(200, 200)变为(300, 300)
        # 在8-10秒中将大小从(300, 300)变为(600, 600)
        self.animation.setDuration(10000)
        self.animation.setKeyValueAt(0.3, QSize(200, 200))
        self.animation.setKeyValueAt(0.8, QSize(300, 300))
        self.animation.setKeyValueAt(1, QSize(600, 600))
        self.animation.start()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
