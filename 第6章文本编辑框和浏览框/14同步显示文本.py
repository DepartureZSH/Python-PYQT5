import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QTextEdit, QTextBrowser, QHBoxLayout, QVBoxLayout


class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.edit_label = QLabel('QTextEdit', self)
        self.browser_label = QLabel('QTextBrowser', self)                      #实例化两个QLabel
        self.text_edit = QTextEdit(self)                                                         #实例化一个文本编辑器
        self.text_browser = QTextBrowser(self)                                         #实例化一个文本浏览器

        self.edit_v_layout = QVBoxLayout()
        self.browser_v_layout = QVBoxLayout()
        self.all_h_layout = QHBoxLayout()

        self.layout_init()
        self.text_edit_init()

    def layout_init(self):
        self.edit_v_layout.addWidget(self.edit_label)
        self.edit_v_layout.addWidget(self.text_edit)

        self.browser_v_layout.addWidget(self.browser_label)
        self.browser_v_layout.addWidget(self.text_browser)

        self.all_h_layout.addLayout(self.edit_v_layout)
        self.all_h_layout.addLayout(self.browser_v_layout)

        self.setLayout(self.all_h_layout)

    def text_edit_init(self):
        self.text_edit.textChanged.connect(self.show_text_func)  # 连接信号textChanged与槽函数show_text_func

    def show_text_func(self):
        self.text_browser.setText(self.text_edit.toPlainText())
        # 通过toPlainText()获取self.text_edit的文本
        # 通过setText()将self.text_browser的文本设为self.text_edit的文本

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())

# 浏览框会执行Html代码哦
# 试试输入<font color='red'>Hello World</font>
