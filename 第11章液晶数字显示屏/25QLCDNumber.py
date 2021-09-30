import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLCDNumber, QVBoxLayout


class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.resize(600, 600)

        self.lcd_1 = QLCDNumber(self)                                   # 实例化一个QLCDNumber
        self.lcd_1.setDigitCount(10)                                        # setDiditCount()设置一共可以显示多少为数字
        self.lcd_1.display(1234567890)                                  # display()用于显示

        self.lcd_2 = QLCDNumber(self)                                   # 实例化一个QLCDNumber
        # setSegmentStyle()设置显示屏数字样式
        self.lcd_2.setSegmentStyle(QLCDNumber.Flat)             # 值2，内容扁平化显示，颜色同窗口标题相同
        # self.lcd_2.setSegmentStyle(QLCDNumber.Filled)       # 值1，让内容浮现，颜色同窗口标题相同
        # self.lcd_2.setSegmentStyle(QLCDNumber.Outline)   # 值0，让内容浮现，颜色同显示屏背景相同

        self.lcd_2.setSmallDecimalPoint(True)                         #setSmallDecimalPoint(bool)可以设置小数点的显示方式
        # True:小数点不单独占位，False:小数点单独占位(默认)

        self.lcd_2.setDigitCount(10)
        self.lcd_2.display(0.123456789)

        self.lcd_3 = QLCDNumber(self)                                           # lcd_3显示的为字符串，
        # 可以显示的字母种类有限：A, B, C, D, E, F, h, H, L, o, P, r, u, U, Y, O/0, S/5, g/9
        self.lcd_3.setSegmentStyle(QLCDNumber.Filled)
        self.lcd_3.display('HELLO')

        self.lcd_4 = QLCDNumber(self)
        self.lcd_4.setSegmentStyle(QLCDNumber.Outline)
        self.lcd_4.setMode(QLCDNumber.Hex)                    # setMode()方法来更改数字显示方式(进制)
        # Hex：值0，16进制
        # Dec：值1，10进制
        # Oct：值2，8进制
        # Bin：值3，2进制
        self.lcd_4.setDigitCount(6)
        self.lcd_4.display(666)

        self.v_layout = QVBoxLayout()
        self.v_layout.addWidget(self.lcd_1)
        self.v_layout.addWidget(self.lcd_2)
        self.v_layout.addWidget(self.lcd_3)
        self.v_layout.addWidget(self.lcd_4)

        self.setLayout(self.v_layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())