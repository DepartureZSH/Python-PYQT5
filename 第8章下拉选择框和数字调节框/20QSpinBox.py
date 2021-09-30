import sys
from PyQt5.QtWidgets import QApplication, QWidget, QSpinBox, QDoubleSpinBox, QHBoxLayout

class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.spinbox = QSpinBox(self)                                                           # 实例化QSpinBox(整型数字调节框)
        self.spinbox.setRange(-99, 99)                                                         # setRange()设置范围，默认范围为0-99
        self.spinbox.setSingleStep(1)                                                            # 设置步长，即每次点击递增或递减多少值
        self.spinbox.setValue(66)                                                                  # 设置QSpinBox初始显示值
        self.spinbox.valueChanged.connect(self.value_change_func)  # 连接信号valueChanged(每次数字发生变化都会触发)与槽函数value_change_func

        self.double_spinbox = QDoubleSpinBox(self)                               # 实例化QDoubleSpinBox(浮点型数字调节框)
        self.double_spinbox.setRange(-99.99, 99.99)                               # setRange()设置范围，默认范围为0.00-99.99
        self.double_spinbox.setSingleStep(0.01)                                       # setSingleStep()设置步长，QDoubleSpinBox小数位数默认是两位
        self.double_spinbox.setValue(66.66)                                             # 设置QDoubleSpinBox初始显示值

        self.h_layout = QHBoxLayout()
        self.h_layout.addWidget(self.spinbox)
        self.h_layout.addWidget(self.double_spinbox)
        self.setLayout(self.h_layout)

    def value_change_func(self):
        decimal_part = self.double_spinbox.value() - int(self.double_spinbox.value())       # 获得浮点框中小数部分decimal_part
        self.double_spinbox.setValue(self.spinbox.value() + decimal_part)                           # 当整数框发生变化，浮点框=整数框+原小数部分
        # 通过setValue()方法可以设置调节框的值，而value()方法是获取值

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())