import sys
from PyQt5.QtCore import Qt, QPoint, QRect
from PyQt5.QtGui import QPainter, QPixmap, QIcon
from PyQt5.QtPrintSupport import QPrintDialog, QPrinter
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout


class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.resize(600, 600)

        self.begin_point = QPoint()
        self.end_point = QPoint()

        self.pix = QPixmap(600, 600)
        self.pix.fill(Qt.white)

        self.printer = QPrinter()                               # 实例化一个用于打印的QPrinter对象

        self.print_btn = QPushButton(self)                      # 实例化一个按钮并设置图标
        self.print_btn.setIcon(QIcon('images\printer.png'))
        self.print_btn.clicked.connect(self.open_printer_func)  # 连接self.printer_btn按钮的信号和槽函数

        self.h_layout = QHBoxLayout()
        self.v_layout = QVBoxLayout()
        self.h_layout.addWidget(self.print_btn)
        self.h_layout.addStretch(1)
        self.v_layout.addLayout(self.h_layout)
        self.v_layout.addStretch(1)

        self.setLayout(self.v_layout)

    # self.pix->(QPainter)painter->self.printer
    def open_printer_func(self):
        printer_dialog = QPrintDialog(self.printer)     # 传入self.printer实例化一个QPrintDialog打印设置对话框
        if printer_dialog.exec_():                      # 调用exec_()使之成为模态对话框,并判断是否成功打开
            painter = QPainter(self.printer)            # 传入self.printer作为绘制设备用于实例化一个QPainter对象
            painter.drawPixmap(0, 0, self.pix)          # 将要打印的内容绘制到self.printer上

    def paintEvent(self, QPaintEvent):
        painter = QPainter(self)
        painter.drawPixmap(0, 0, self.pix)

        if self.begin_point and self.end_point:
            rect = QRect(self.begin_point, self.end_point)
            painter.drawRect(rect)

    def mousePressEvent(self, QMouseEvent):
        if QMouseEvent.button() == Qt.LeftButton:
            self.begin_point = QMouseEvent.pos()
            self.end_point = self.begin_point
            self.update()

    def mouseMoveEvent(self, QMouseEvent):
        if QMouseEvent.buttons() == Qt.LeftButton:
            self.end_point = QMouseEvent.pos()
            self.update()

    def mouseReleaseEvent(self, QMouseEvent):
        if QMouseEvent.button() == Qt.LeftButton:
            painter = QPainter(self.pix)
            rect = QRect(self.begin_point, self.end_point)
            painter.drawRect(rect)
            self.begin_point = self.end_point = QPoint()
            self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())