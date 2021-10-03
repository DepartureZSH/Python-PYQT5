import sys
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QPropertyAnimation, QSequentialAnimationGroup, QRect
from PyQt5.QtWidgets import QApplication, QWidget, QLabel

# 串行动画：按照调用addAnimation()或者insertAnimation()方法把各个动画添加进去的顺序来执行动画
class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.resize(600, 600)

        self.plane = QLabel(self)
        self.plane.resize(50, 50)
        self.plane.setPixmap(QPixmap('images\Plane.png').scaled(self.plane.size()))
        # 调用scaled()可以将图片设置为我们想要的大小，这里我们设置成QLabel控件一样的大小，否则图像会显示不全

        self.animation1 = QPropertyAnimation(self.plane, b'geometry')
        self.animation1.setDuration(2000)
        self.animation1.setStartValue(QRect(300, 500, 50, 50))
        self.animation1.setEndValue(QRect(200, 400, 50, 50))
        self.animation1.setLoopCount(1)

        self.animation2 = QPropertyAnimation(self.plane, b'geometry')
        self.animation2.setDuration(2000)
        self.animation2.setStartValue(QRect(200, 400, 50, 50))
        self.animation2.setEndValue(QRect(400, 300, 50, 50))
        self.animation2.setLoopCount(1)

        self.animation3 = QPropertyAnimation(self.plane, b'geometry')
        self.animation3.setDuration(2000)
        self.animation3.setStartValue(QRect(400, 300, 50, 50))
        self.animation3.setEndValue(QRect(200, 200, 50, 50))
        self.animation3.setLoopCount(1)

        self.animation_group = QSequentialAnimationGroup(self)    # 实例化一个QSequentialAnimationGroup类

        # 调用addAnimation()方法将之前设置好的3个QPropertyAnimation属性动画实例添加进去
        self.animation_group.addAnimation(self.animation1)
        # addPause()方法用来在动画执行过程中添加暂停时间
        self.animation_group.addPause(1000)
        self.animation_group.addAnimation(self.animation2)
        self.animation_group.addAnimation(self.animation3)
        self.animation_group.start()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
