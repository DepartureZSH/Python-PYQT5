import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QBrush, QPixmap, QLinearGradient, QRadialGradient, QConicalGradient
from PyQt5.QtWidgets import QApplication, QWidget


class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.resize(600, 600)

        self.brush1 = QBrush(Qt.SolidPattern)                   # 传入画刷样式进行实例化
        # 默认的样式为Qt.NoBrush而不是Qt.SolidPattern

        self.brush2 = QBrush(Qt.Dense6Pattern)
        self.brush2.setColor(Qt.red)                            # 调用setColor()方法设置画刷颜色

        # Qt一共提供三种渐变色样式，分别是:
        # 线性渐变QLinearGradientPattern
        # 径向渐变QRadialGradientPattern
        # 锥形渐变QConicalGradientPattern
        gradient1 = QLinearGradient(200, 200, 300, 300)         # 实例化线性渐变QLinearGradient对象
        # QLinearGradient参数须输入两点坐标，若输入对角坐标，则在对角方向上渐变
        gradient1.setColorAt(0.2, Qt.red)
        # setColorAt()方法传入需两个参数
        # 第一个参数代表颜色开始渐变的位置(大小范围为0-1)，第二个参数为颜色值
        # setColorAt(0.2, Qt.red)表示红色在渐变区域0.2(即20%)处的位置开始渐变到下一种颜色
        gradient1.setColorAt(0.8, Qt.green)
        gradient1.setColorAt(1, Qt.blue)
        self.brush3 = QBrush(gradient1)                         # 实例化QBrush对象并传入相应的渐变类型

        gradient2 = QRadialGradient(350, 350, 50, 350, 350)     # 实例化径向渐变QRadialGradient对象
        # QRadialGradient前两个参数为中心点坐标，50为半径(渐变范围)，后两个为焦点坐标
        gradient2.setColorAt(0, Qt.red)
        gradient2.setColorAt(1, Qt.blue)
        self.brush4 = QBrush(gradient2)

        gradient3 = QConicalGradient(450, 450, 90)              # 实例化锥形渐变QConicalGradient对象
        # QConicalGradient前两个值为中心点坐标，最后个为首个颜色开始处的角度值(范围为0-360)
        gradient3.setColorAt(0, Qt.red)
        gradient3.setColorAt(1, Qt.blue)
        self.brush5 = QBrush(gradient3)

        self.brush6 = QBrush(Qt.TexturePattern)
        # Qt.TexturePattern为纹理样式
        # 调用该方法会自动把样式设置为Qt.TexturePattern，所以在实例化的时候可以不需要传入该样式值
        self.brush6.setTexture(QPixmap('images/smile32x32.png'))
        # 调用setTexture()方法传入QPixmap值可以设置好纹理图案

    def paintEvent(self, QPaintEvent):
        painter = QPainter(self)
        painter.setBrush(self.brush1)                           # 调用setBrush()方法就可以设置画刷
        painter.drawRect(0, 0, 100, 100)

        painter.setBrush(self.brush2)
        painter.drawRect(100, 100, 100, 100)

        painter.setBrush(self.brush3)
        painter.drawRect(200, 200, 100, 100)

        painter.setBrush(self.brush4)
        painter.drawRect(300, 300, 100, 100)

        painter.setBrush(self.brush5)
        painter.drawRect(400, 400, 100, 100)

        painter.setBrush(self.brush6)
        painter.drawRect(500, 500, 100, 100)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
