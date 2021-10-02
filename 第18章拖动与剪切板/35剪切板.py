import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTextEdit, QTextBrowser, QPushButton, QGridLayout


class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.text_edit = QTextEdit(self)
        self.text_browser = QTextBrowser(self)

        self.clipboard = QApplication.clipboard()                                                       # 实例化一个剪贴板
        self.clipboard.dataChanged.connect(lambda: print('Data Changed'))     # 连接信号dataChanged(剪贴板内容变化时触发)与打印函数

        self.copy_btn = QPushButton('Copy', self)                                     # 实例化一个push按钮
        self.copy_btn.clicked.connect(self.copy_func)                             # 连接信号clicked与槽函数copy_func

        self.paste_btn = QPushButton('Paste', self)                                   # 实例化一个push按钮
        self.paste_btn.clicked.connect(self.paste_func)                           # 连接信号clicked与槽函数paste_func

        self.g_layout = QGridLayout()
        self.g_layout.addWidget(self.text_edit, 0, 0, 1, 1)                         # 从(0,0)格开始，占用1行1列(默认)
        self.g_layout.addWidget(self.text_browser, 0, 1, 1, 1)                 # 从(0,1)格开始，占用1行1列(默认)
        self.g_layout.addWidget(self.copy_btn, 1, 0, 1, 1)                        # 从(1,0)格开始，占用1行1列(默认)
        self.g_layout.addWidget(self.paste_btn, 1, 1, 1, 1)                      # 从(1,1)格开始，占用1行1列(默认)
        self.setLayout(self.g_layout)

    def copy_func(self):
        self.clipboard.setText(self.text_edit.toPlainText())
        # 将text_edit中的文本获取过来
        # 然后通过setText()方法将其设置为剪贴板self.clipboard的文本

    def paste_func(self):
        self.text_browser.setText(self.clipboard.text())                           # 将text_browser的文本设为剪贴板self.clipboard的文本

    # def paste_func(self):
    #     mime = self.clipboard.mimeData()
    #     if mime.hasText():
    #         self.text_browser.setText(mime.text())
    # 用mimeData()获取剪贴板内容的MIME类型，再判断mime类型是否为text / plain，
    # 是的话则通过text()方法获取，并设为text_browser文本

    # clear()                   清空剪切板内容
    # mimeDate()        获取剪切板上的MIME类型数据
    # setMimeDate()   将MIME类型数据放到剪切板中
    # pixmap()              获取剪切板上的QPixmap类型数据
    # setPixmap()         将QPixmap类型数据放到剪切板中
    # image()                 获取剪切板上的QImage类型数据
    # setImage()            将QImage类型数据放到剪贴板中
    # text()                     获取剪贴板上的文本
    # setText()               将文本放到剪贴板中

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())