import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QComboBox, QVBoxLayout


class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.button1 = QPushButton('button1', self)
        self.button2 = QPushButton('button2', self)
        self.button2.setProperty('name', 'btn2')

        my_list = ['A', 'B', 'C', 'D']
        self.combo = QComboBox(self)
        self.combo.addItems(my_list)

        self.v_layout = QVBoxLayout()
        self.v_layout.addWidget(self.button1)
        self.v_layout.addWidget(self.button2)
        self.v_layout.addWidget(self.combo)
        self.setLayout(self.v_layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    qss = """
          QPushButton:hover {background-color: red}                     
          QPushButton[name='btn2']:pressed {background-color: blue}
          QComboBox::drop-down:hover {background-color: green}
          """
    # QPushButton:hover {background-color: red}
    # 当鼠标悬停在QPushButton实例或其子类上时，将背景变为红色
    # QPushButton:!hover {background-color: red}
    # 当鼠标不悬停在QPushButton实例或其子类上时，背景颜色才会是红色

    # QPushButton[name='btn2']:pressed {background-color: blue}
    # 当鼠标在QPushButton实例或其子类上按下时，将背景变为蓝色(但只针对name属性为btn2的QPushButton实例及子类)

    # QComboBox::drop-down:hover {background-color: green}
    # 当鼠标在QComboBox实例或其子类的下拉按钮子控件上悬停时，将下拉按钮的背景色改为绿色

    demo.setStyleSheet(qss)
    demo.show()
    sys.exit(app.exec_())