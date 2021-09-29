import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, \
    QHBoxLayout, QVBoxLayout

class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.user_label = QLabel('Username:', self)
        self.pwd_label = QLabel('Password:', self)
        self.user_line = QLineEdit(self)
        self.pwd_line = QLineEdit(self)
        self.login_button = QPushButton('Log in', self)
        self.signin_button = QPushButton('Sign in', self)

        self.label_v_layout = QVBoxLayout()                     # 实例化一个垂直布局管理器1号(管理QLabel)
        self.line_v_layout = QVBoxLayout()                       # 实例化一个垂直布局管理器2号(管理QLineEdit)
        self.label_line_h_layout = QHBoxLayout()           # 实例化一个水平布局管理器3号(管理1、2号管理器)
        self.button_h_layout = QHBoxLayout()                # 实例化一个水平布局管理器4号(管理QPushButton)
        self.all_v_layout = QVBoxLayout()                         # 实例化一个垂直布局管理器5号(管理3、4号管理器)

        self.label_v_layout.addWidget(self.user_label)
        self.label_v_layout.addWidget(self.pwd_label)

        self.line_v_layout.addWidget(self.user_line)
        self.line_v_layout.addWidget(self.pwd_line)

        self.button_h_layout.addWidget(self.login_button)
        self.button_h_layout.addWidget(self.signin_button)

        self.label_line_h_layout.addLayout(self.label_v_layout)
        self.label_line_h_layout.addLayout(self.line_v_layout)

        self.all_v_layout.addLayout(self.label_line_h_layout)
        self.all_v_layout.addLayout(self.button_h_layout)

        self.setLayout(self.all_v_layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())