import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox,QHBoxLayout


class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.button_ok = QPushButton('ok', self)
        self.button_YNC = QPushButton('yes_no_cancel', self)
        self.button_Question = QPushButton('question', self)

        self.button_ok.clicked.connect(self.show_messagebox_ok)       # 连接connect信号clicked(按钮被点击)与槽函数show_messagebox_ok
        self.button_YNC.clicked.connect(self.show_messagebox_YNC)
        self.button_Question.clicked.connect(self.show_messagebox_Q)

        self.button_h_layout = QHBoxLayout()                                            # 实例化一个水平布局管理器(管理QPushButton)
        self.button_h_layout.addWidget(self.button_ok)
        self.button_h_layout.addWidget(self.button_YNC)
        self.button_h_layout.addWidget(self.button_Question)
        self.setLayout(self.button_h_layout)

    def show_messagebox_ok(self):
        QMessageBox.information(self, 'Title', 'Content')

    def show_messagebox_Q(self):
        QMessageBox.question(self, 'Title', 'Content')                              # 另外还有QMessageBox.warning警告框
                                                                                                                        # QMessageBox.critical错误框，QMessageBox.about 关于框
    def show_messagebox_YNC(self):
        QMessageBox.information(self, 'Title', 'Content',
                                QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel)

# 常用按钮
# QMessageBox.Ok
# QMessageBox.Yes
# QMessageBox.No
# QMessageBox.Close
# QMessageBox.Cancel
# QMessage.Open
# QMessage.Save

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())