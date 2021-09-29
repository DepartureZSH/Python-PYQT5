import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QHBoxLayout


class Demo(QWidget):

    def __init__(self):
        super(Demo, self).__init__()
        self.user_label = QLabel('Username:', self)
        self.user_line = QLineEdit(self)                            # QLineEdit控件：单行文本输入框

        self.h_layout = QHBoxLayout()                           # 实例化一个水平布局管理器QHBoxLayout
        self.h_layout.addWidget(self.user_label)
        self.h_layout.addWidget(self.user_line)          # 将QLabel和QLineEdit控件添加到水平布局管理器中，先添加的出现在左边

        self.setLayout(self.h_layout)                               # 将self.h_layout设为整个窗口的最终布局方式

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())