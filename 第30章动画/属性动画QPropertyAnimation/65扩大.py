import sys
from PyQt5.QtCore import QPropertyAnimation, QSize
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton


class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.resize(600, 600)

        self.btn = QPushButton('Bigger', self)
        self.btn.resize(100, 100)

        self.animation = QPropertyAnimation(self.btn, b'size')  # 实例化一个QPropertyAnimation对象
        # 传入该动画要作用的对象self.btn以及要改变的属性size
        # 第二个参数为字节数组类型QByteArray，不是简单的字符串类型str，所以必须要加上个b
        self.animation.setDuration(6000)                        # 调用setDuration()方法设置动画持续时间
        # 这里的6000代表持续6秒

        # 设置动画开始和结束时候按钮的属性值(专业点叫做“线性插值”)
        self.animation.setStartValue(QSize(100, 100))           # 设置动画开始时按钮的大小为(100, 100)
        self.animation.setEndValue(QSize(600, 600))             # 设置动画结束时按钮的大小为(600, 600)
        # 这里传入的参数必须为QVariant类型(可以把QVariant理解为Qt中常见的数据类型)
        # 该类型包括int，float，double，QColor，QLine，QLineF，
        # QPoint，QPointF，QRect，QRectF，QSize和QSizeF等。

        self.animation.start()                                  # 调用start()方法开始动画


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())