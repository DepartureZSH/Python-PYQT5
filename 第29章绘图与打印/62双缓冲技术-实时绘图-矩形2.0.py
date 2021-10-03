import sys
from PyQt5.QtCore import Qt, QPoint, QRect
from PyQt5.QtGui import QPainter, QPixmap
from PyQt5.QtWidgets import QApplication, QWidget


class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.resize(600, 600)

        self.begin_point = QPoint()
        self.end_point = QPoint()

        self.pix = QPixmap(600, 600)
        self.pix.fill(Qt.white)

    # 第一步：画布self.pix->painter->窗口
    # 第二步（鼠标按下开启第二步）：
    #   判断坐标不是(0, 0),直接在窗口绘制矩形
    #   注：这是预览矩形，因为鼠标释放，此矩形将绘制于画布self.pix，并重复第一步
    def paintEvent(self, QPaintEvent):
        painter = QPainter(self)                                # 实例化以窗口为绘图设备的QPainter对象
        painter.drawPixmap(0, 0, self.pix)                      # 调用drawPixmap()方法将画布呈现在窗口上

        if self.begin_point and self.end_point:                 # 判断坐标是否不是(0, 0)
            rect = QRect(self.begin_point, self.end_point)
            painter.drawRect(rect)                              # 调用drawRect()方法绘制矩形

    def mousePressEvent(self, QMouseEvent):
        if QMouseEvent.button() == Qt.LeftButton:
            self.begin_point = QMouseEvent.pos()
            self.end_point = self.begin_point
            self.update()


    def mouseMoveEvent(self, QMouseEvent):
        if QMouseEvent.buttons() == Qt.LeftButton:
            self.end_point = QMouseEvent.pos()
            self.update()

    #   鼠标释放->painter->画布self.pix
    def mouseReleaseEvent(self, QMouseEvent):              # 鼠标释放事件函数中
        if QMouseEvent.button() == Qt.LeftButton:
            painter = QPainter(self.pix)                    # 实例化以画布self.pix为绘图设备的QPainter对象
            rect = QRect(self.begin_point, self.end_point)  # 此时鼠标已经释放，坐标都已经确定
            painter.drawRect(rect)                          # 将矩形绘制出来（只可能有一个）
            self.begin_point = self.end_point = QPoint()    # 设置begin_point和end_point为原点坐标(即为空)
            self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())