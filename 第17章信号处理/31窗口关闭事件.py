import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTextEdit, QPushButton, QMessageBox, QVBoxLayout


class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()

        self.is_saved = True                                                                             # is_saved变量用于记录用户是否已经进行保存

        self.textedit = QTextEdit(self)                                                            # 实例化一个QTextEdit控件用于文本编辑
        self.textedit.textChanged.connect(self.on_textchanged_func) # 连接控件textChanged信号与槽函数on_textchanged_func()

        self.button = QPushButton('Save', self)                                           # 实例化一个按钮用于保存操作
        self.button.clicked.connect(self.on_clicked_func)                        # 连接clicked信号与槽函数on_clicked_func()

        self.v_layout = QVBoxLayout()
        self.v_layout.addWidget(self.textedit)
        self.v_layout.addWidget(self.button)
        self.setLayout(self.v_layout)

    def on_textchanged_func(self):                                                           # 判断在每次文本内容发生变化时
        if self.textedit.toPlainText():                                                             # textedit中是否还有文本
            self.is_saved = False                                                                       #若有的话则将is_saved变量设为False，即未保存
        else:
            self.is_saved = True                                                                        # 若无文本，则将其设为True

    def on_clicked_func(self):                                                                      #每次点击该按钮就进行保存，
        self.save_func(self.textedit.toPlainText())                                     # 不管文本编辑框中是否有文本，文本保存通过save_fcun()函数完成
        self.is_saved = True

    def save_func(self, text):
        with open('saved.txt', 'w') as f:                                                         # 将内容保存在当前目录下的saved.txt函数中
            f.write(text)

    def closeEvent(self, QCloseEvent):                                                       # 重新定义QWidget库的窗口关闭函数closeEvent()
        if not self.is_saved:                                                                              # 如果还没有保存就关闭窗口，则弹出QMessageBox窗口询问是否保存
            choice = QMessageBox.question(self, '', 'Do you want to save the text?',
                                          QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel)
            if choice == QMessageBox.Yes:                                                     # 若用户点击Yes
                self.save_func(self.textedit.toPlainText())                              # 则调用save_func()函数进行保存
                QCloseEvent.accept()                                                                  # 然后通过accept()方法来接收关闭窗口操作，窗口随之关闭
            elif choice == QMessageBox.No:                                                   # 若点击No
                QCloseEvent.accept()                                                                  # 则不进行保存，但同样得关闭窗口
            else:                                                                                                    # 若点击cancel，也不进行保存
                QCloseEvent.ignore()                                                                  # 并通过ignore()方法来忽略这次关闭窗口的操作


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())