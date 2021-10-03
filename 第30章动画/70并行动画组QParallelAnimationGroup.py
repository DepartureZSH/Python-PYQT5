import sys
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QPropertyAnimation, QParallelAnimationGroup, QRect, QEasingCurve
from PyQt5.QtWidgets import QApplication, QWidget, QLabel


class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.resize(600, 600)

        self.plane = QLabel(self)
        self.plane.resize(50, 50)
        self.plane.setPixmap(QPixmap('images\Plane.png').scaled(self.plane.size()))

        self.plane2 = QLabel(self)
        self.plane2.resize(50, 50)
        self.plane2.setPixmap(QPixmap('images\Plane 2.png').scaled(self.plane2.size()))

        self.animation1 = QPropertyAnimation(self.plane, b'geometry')
        self.animation1.setDuration(2000)
        self.animation1.setStartValue(QRect(200, 500, 50, 50))
        self.animation1.setEndValue(QRect(200, 100, 50, 50))
        self.animation1.setEasingCurve(QEasingCurve.OutCirc)
        self.animation1.setLoopCount(1)

        self.animation2 = QPropertyAnimation(self.plane2, b'geometry')
        self.animation2.setDuration(2000)
        self.animation2.setStartValue(QRect(300, 500, 50, 50))
        self.animation2.setEndValue(QRect(300, 100, 50, 50))
        self.animation2.setEasingCurve(QEasingCurve.OutCirc)
        self.animation2.setLoopCount(1)

        self.animation_group = QParallelAnimationGroup(self)      # 实例化一个QParallelAnimationGroup类
        # 调用addAnimation()方法加入动画
        self.animation_group.addAnimation(self.animation1)
        self.animation_group.addAnimation(self.animation2)
        self.animation_group.start()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())