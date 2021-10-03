import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtWidgets import QApplication, QWidget


class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.resize(600, 600)

        self.pen1 = QPen()                      # 实例化QPen对象
        self.pen1.setColor(Qt.green)            # 调用setColor()方法可设置画笔颜色
        self.pen2 = QPen(Qt.SolidLine)          # 传入画笔样式(默认为Qt.SolidLine)
        self.pen2.setWidth(6)                   # 调用setWidth()设置画笔粗细(默认为1)
        # self.pen2.setWidthF(3.3)              # 如果要传入浮点型的话可使用setWidthF()
        self.pen3 = QPen(Qt.DashLine)
        self.pen4 = QPen(Qt.DotLine)
        self.pen5 = QPen(Qt.DashDotLine)
        self.pen6 = QPen(Qt.DashDotDotLine)
        self.pen7 = QPen(Qt.CustomDashLine)     # 使用Qt.CustomDashLine自定义样式的话
        # 之后还需要调用setDashPattern()方法来设置虚线模式
        # 传入迭代器参数的含义是：像素长度，空白间隔长度，像素长度，空白间隔长度......
        self.pen7.setDashPattern([6, 2, 18, 2])

        self.pen8 = QPen(Qt.SolidLine)
        self.pen8.setWidth(6)
        self.pen8.setCapStyle(Qt.RoundCap)      # 调用setCapStyle()设置笔端样式为Qt.RoundCap
        # 三种笔端样式详见Qt.RoundCap.jpg

        self.pen9 = QPen(Qt.SolidLine)
        self.pen9.setWidthF(6)
        self.pen9.setJoinStyle(Qt.MiterJoin)    # 调用setJoinStyle()设置线条连接方式为Qt.MiterJoin
        # 三种线条连接形式详见Qt.MiterJoin.jpg

    def paintEvent(self, QPaintEvent):
        painter = QPainter(self)                # 在paintEvent()事件函数中实例化一个QPainter对象
        painter.setPen(self.pen1)               # 调用setPen()方法设置画笔
        painter.drawLine(100, 10, 500, 10)      # 调用drawLine()方法传入坐标就可以画出一条直线

        painter.setPen(self.pen2)
        painter.drawLine(100, 30, 500, 30)

        painter.setPen(self.pen3)
        painter.drawLine(100, 50, 500, 50)

        painter.setPen(self.pen4)
        painter.drawLine(100, 70, 500, 70)

        painter.setPen(self.pen5)
        painter.drawLine(100, 90, 500, 90)

        painter.setPen(self.pen6)
        painter.drawLine(100, 110, 500, 110)

        painter.setPen(self.pen7)
        painter.drawLine(100, 130, 500, 130)

        painter.setPen(self.pen8)
        painter.drawLine(100, 150, 500, 150)

        painter.setPen(self.pen2)
        painter.drawRect(100, 170, 400, 200)    # 用Pen2和Pen9分别画了个矩形
        # 设矩形左上角坐标（x,y），长为L，宽为D
        # 传入参数为(x,y,x+L,y+D)

        painter.setPen(self.pen9)
        painter.drawRect(100, 390, 400, 200)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())