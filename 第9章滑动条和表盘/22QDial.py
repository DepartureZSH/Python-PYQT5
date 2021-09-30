import sys
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QWidget, QDial, QLabel, QHBoxLayout


class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.setWindowTitle('QDial')                                                             # setWindowTitle()设置窗口标题

        self.dial = QDial(self)                                                                           # 实例化一个QDial
        self.dial.setFixedSize(100, 100)                                                         # setFixedSize()来固定QDial的大小
        self.dial.setRange(0, 100)                                                                   # setRange()来设置表盘数值范围
        self.dial.setNotchesVisible(True)                                                      # True:显示刻度，刻度根据设置的数值自动调整
        self.dial.valueChanged.connect(self.on_change_func)               # 连接信号valueChanged与槽函数on_change_func

        self.label = QLabel('0', self)
        self.label.setFont(QFont('Arial Black', 20))

        self.h_layout = QHBoxLayout()
        self.h_layout.addWidget(self.dial)
        self.h_layout.addWidget(self.label)

        self.setLayout(self.h_layout)

    def on_change_func(self):
        self.label.setText(str(self.dial.value()))                                           # 当dial数值变化，同时改变label的值


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())