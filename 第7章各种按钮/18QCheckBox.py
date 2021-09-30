import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QCheckBox, QVBoxLayout


class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.checkbox1 = QCheckBox('Checkbox 1', self)
        self.checkbox2 = QCheckBox('Checkbox 2', self)
        self.checkbox3 = QCheckBox('Checkbox 3', self)

        self.v_layout = QVBoxLayout()

        self.checkbox_init()
        self.layout_init()

    def layout_init(self):
        self.v_layout.addWidget(self.checkbox1)
        self.v_layout.addWidget(self.checkbox2)
        self.v_layout.addWidget(self.checkbox3)

        self.setLayout(self.v_layout)

    def checkbox_init(self):
        self.checkbox1.setChecked(True)                                                                          # 勾选checkbox1
        # self.checkbox1.setCheckState(Qt.Checked)                                                      # 勾选的第二种方式
        self.checkbox1.stateChanged.connect(lambda: self.on_state_change_func(self.checkbox1))      # 连接信号stateChanged和槽函数(槽函数是带参数，通过lambda表达式传入)

        self.checkbox2.setChecked(False)
        # self.checkbox2.setCheckState(Qt.Unchecked)
        self.checkbox2.stateChanged.connect(lambda: self.on_state_change_func(self.checkbox2))

        self.checkbox3.setTristate(True)                                                                            # 通过setTristate(True)方法，让一个复选框拥有三种状态
        self.checkbox3.setCheckState(Qt.PartiallyChecked)                                           # 让第三个复选框拥有三种状态
        self.checkbox3.stateChanged.connect(lambda: self.on_state_change_func(self.checkbox3))

    def on_state_change_func(self, checkbox):                                      # checkState()方法可以获取当前复选框的状态，返回值为int类型
        print('{} was clicked, and its current state is {}'.format(checkbox.text(), checkbox.checkState()))     # 0为无选中状态，1为半选中状态，2位选中状态

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())