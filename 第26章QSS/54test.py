import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout


class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.button1 = QPushButton('super class', self)
        self.button2 = SubButton()

        self.h_layout = QHBoxLayout()
        self.h_layout.addWidget(self.button1)
        self.h_layout.addWidget(self.button2)
        self.setLayout(self.h_layout)


class SubButton(QPushButton):
    def __init__(self):
        super(SubButton, self).__init__()
        self.setText('subclass')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    qss = 'QPushButton {color: red}'
    # qss = 'QPushButton, QLabel, QLineEdit {color: red}'
    # qss = 'QPushButton {color: red; background-color: blue}'
    demo.setStyleSheet(qss)
    demo.show()
    sys.exit(app.exec_())