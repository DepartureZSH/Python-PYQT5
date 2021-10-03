import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTextEdit, QColorDialog, QFontDialog, QPushButton, \
                            QHBoxLayout, QVBoxLayout


class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.text_edit = QTextEdit(self)                                                         # QTextEdit控件用于显示文本颜色和字体变化

        self.color_btn = QPushButton('Color', self)                                    # 实例化一个按钮用于打开颜色对话框
        self.font_btn = QPushButton('Font', self)                                       # 实例化一个按钮用于打开字体对话框
        self.color_btn.clicked.connect(lambda: self.open_dialog_func(self.color_btn))   # 连接点击Color按钮信号与槽函数
        self.font_btn.clicked.connect(lambda: self.open_dialog_func(self.font_btn))   # 连接点击Font按钮信号与槽函数

        self.h_layout = QHBoxLayout()
        self.h_layout.addWidget(self.color_btn)
        self.h_layout.addWidget(self.font_btn)
        self.v_layout = QVBoxLayout()
        self.v_layout.addWidget(self.text_edit)
        self.v_layout.addLayout(self.h_layout)
        self.setLayout(self.v_layout)

    def open_dialog_func(self, btn):
        if btn == self.color_btn:                                                                      # 如果color_btn被按下
            color = QColorDialog.getColor()                                                   # 调用QColorDialog的getColor()方法显示颜色对话框
            # 返回的十六进制的值保存在color变量
            if color.isValid():                                                                              # 当选择一种颜色后(如果点击取消(Cancel)按钮，则color为无效值)
                self.text_edit.setTextColor(color)                                            # setTextColor()方法设置QTextEdit的文本颜色
        else:                                                                                                        # 如果font_btn被按下
            font, ok = QFontDialog.getFont()                                                 # 调用QFontDialog的getFont()方法显示字体对话框
            # 该方法返回两个值，分别为QFont和bool值
            # 如果用户选择了一种字体并按下确定(Ok)，则font保存所选择的QFont值，并且ok为True。
            # 若按下取消(Cancel)的话，则bool为False。
            if ok:                                                                                                   # 如果用户按下确认
                self.text_edit.setFont(font)                                                       # 调用setFont()方法设置QTextEdit的文本字体

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())