import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QWidget, QSlider, QLabel, QVBoxLayout, QHBoxLayout


class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.slider_1 = QSlider(Qt.Horizontal, self)                                     # 实例化一个水平(Qt.Horizontal)的滑动条
        self.slider_1.setRange(0, 100)                                                           # setRange()方法设置滑动条的范围
        self.slider_1.valueChanged.connect(lambda: self.on_change_func(self.slider_1))  # 连接信号valueChanged(滑动使数值改变触发)和槽函数

        self.slider_2 = QSlider(Qt.Vertical, self)                                          # 实例化一个垂直(Qt.Vertical)的滑动条
        self.slider_2.setMinimum(0)                                                            # 使用setMinimum()和setMaximum()方法来设置最小值和最大值
        self.slider_2.setMaximum(100)                                                       # 替代了setRange()
        self.slider_2.valueChanged.connect(lambda: self.on_change_func(self.slider_2))

        self.label = QLabel('0', self)                                                                # 实例化QLabel，显示QSlider当前的数值
        self.label.setFont(QFont('Arial Black', 20))                                     # 设置label中字体与大小

        self.h_layout = QHBoxLayout()
        self.v_layout = QVBoxLayout()

        self.h_layout.addWidget(self.slider_2)
        self.h_layout.addStretch(1)
        self.h_layout.addWidget(self.label)
        self.h_layout.addStretch(1)

        self.v_layout.addWidget(self.slider_1)
        self.v_layout.addLayout(self.h_layout)

        self.setLayout(self.v_layout)

    def on_change_func(self, slider):                                                         # 将两个滑动条的数值同步,然后改变label数值
        if slider == self.slider_1:
            self.slider_2.setValue(self.slider_1.value())
            self.label.setText(str(self.slider_1.value()))
        else:
            self.slider_1.setValue(self.slider_2.value())
            self.label.setText(str(self.slider_2.value()))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())