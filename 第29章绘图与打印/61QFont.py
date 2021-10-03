import sys
from PyQt5.QtGui import QPainter, QFont
from PyQt5.QtWidgets import QApplication, QWidget


class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.resize(600, 600)

    def paintEvent(self, QPaintEvent):
        painter = QPainter(self)
        painter.setFont(QFont('Times New Roman', 30))
        painter.drawText(100, 100, 'Hello PyQt5!')
        # drawText方法详见drawText方法.jpg

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())