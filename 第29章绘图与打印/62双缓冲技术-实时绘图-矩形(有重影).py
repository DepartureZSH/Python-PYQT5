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

    def paintEvent(self, QPaintEvent):
        painter = QPainter(self.pix)
        rect = QRect(self.begin_point, self.end_point)  # 1
        painter.drawRect(rect)
        painter2 = QPainter(self)
        painter2.drawPixmap(0, 0, self.pix)

    def mousePressEvent(self, QMouseEvent):
        if QMouseEvent.button() == Qt.LeftButton:
            self.begin_point = QMouseEvent.pos()
            self.end_point = self.begin_point
            self.update()

    def mouseMoveEvent(self, QMouseEvent):
        if QMouseEvent.buttons() == Qt.LeftButton:
            self.end_point = QMouseEvent.pos()
            self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())