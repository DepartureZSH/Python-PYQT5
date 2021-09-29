import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout


class Demo(QWidget):

    def __init__(self):
        super(Demo, self).__init__()
        self.user_label = QLabel('Username:', self)
        self.pwd_label = QLabel('Password:', self)

        self.v_layout = QVBoxLayout()                     # 实例化一个垂直布局管理器QVBoxLayout
        self.v_layout.addWidget(self.user_label)
        self.v_layout.addWidget(self.pwd_label)  # 通过调用addWidget()方法来将控件一个个添加到垂直布局中，最先添加的出现在最上方
        self.setLayout(self.v_layout)                         # 将self.v_layout设为整个窗口的最终布局方式

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())