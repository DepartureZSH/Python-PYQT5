import sys
from PyQt5.QtWidgets import QApplication, QWidget
from designer import Ui_Form


class Demo(QWidget, Ui_Form):
    def __init__(self):
        super(Demo, self).__init__()
        self.setupUi(self)                                                                                  # 将UI界面布局到Demo上
        self.text_edit.textChanged.connect(self.show_text_func)          # 连接.text_edit的信号textChanged(text变化)与槽函数show_text_func()

    def show_text_func(self):                                                                       # 将self.text_browser的文本设为self.text_edit的文本
        self.text_browser.setText(self.text_edit.toPlainText())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())