import sys
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QPainter, QPixmap
from PyQt5.QtWidgets import QApplication, QWidget

# 所谓实时绘图也就是说鼠标左键开始被按下那刻，鼠标移动到哪里，画笔就画到哪里，直到左键被释放
class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.resize(600, 600)

        self.begin_point = QPoint()             # 两个QPoint()坐标实例用于记录鼠标位置
        self.end_point = QPoint()

        self.pix = QPixmap(600, 600)            # 实例化一个QPixmap()类作为画布，大小跟窗口一样
        self.pix.fill(Qt.white)                 # 调用fill()放法传入Qt.white让画布变白

        # 窗口(屏幕)<-painter2<-画布pix<-painter
    def paintEvent(self, QPaintEvent):
        painter = QPainter(self.pix)            # 实例化一个以self.pix为绘画设备的QPainter实例
        painter.drawLine(self.begin_point, self.end_point)  # 调用drawLine()方法传入坐标来绘制
        self.begin_point = self.end_point
        painter2 = QPainter(self)               # 实例化一个以窗口为绘画设备的QPainter实例
        painter2.drawPixmap(0, 0, self.pix)     # 调用drawPixmap()方法将self.pix画布一次性画在窗口(屏幕)上

    def mousePressEvent(self, QMouseEvent):
        if QMouseEvent.button() == Qt.LeftButton:
            self.begin_point = QMouseEvent.pos()
            self.end_point = self.begin_point
            self.update()
            # update()让窗口重新调paintEvent()函数
            # 这样鼠标的实时位置坐标才可以被不断传入paintEvent()函数中进行绘制
            # 如果不加的话那paintEvent()只会在程序初始化时被调用一次

    def mouseMoveEvent(self, QMouseEvent):
        if QMouseEvent.buttons() == Qt.LeftButton:
            self.end_point = QMouseEvent.pos()
            self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())