import sys
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QTextEdit, QPushButton, \
                            QGridLayout
# 输入对话框一共有五种输入方法:
# getItem()                            从下拉框中获取选项输入
# getInt()                               获取整型值输入
# getDouble()                       获取浮点型值输入
# getText()                             获取字符串输入
# getMultiLineText()            获取多行字符串输入

class Demo(QWidget):
    def __init__(self):                                                                                     # 实例化各种按钮、文字输入框，建立连接与布局
        super(Demo, self).__init__()
        self.name_btn = QPushButton('Name', self)
        self.gender_btn = QPushButton('Gender', self)
        self.age_btn = QPushButton('Age', self)
        self.score_btn = QPushButton('Score', self)
        self.info_btn = QPushButton('Info', self)

        self.name_btn.clicked.connect(lambda: self.open_dialog_func(self.name_btn))
        self.gender_btn.clicked.connect(lambda: self.open_dialog_func(self.gender_btn))
        self.age_btn.clicked.connect(lambda: self.open_dialog_func(self.age_btn))
        self.score_btn.clicked.connect(lambda: self.open_dialog_func(self.score_btn))
        self.info_btn.clicked.connect(lambda: self.open_dialog_func(self.info_btn))

        self.name_line = QLineEdit(self)
        self.gender_line = QLineEdit(self)
        self.age_line = QLineEdit(self)
        self.score_line = QLineEdit(self)
        self.info_textedit = QTextEdit(self)

        self.g_layout = QGridLayout()
        self.g_layout.addWidget(self.name_btn, 0, 0, 1, 1)
        self.g_layout.addWidget(self.name_line, 0, 1, 1, 1)
        self.g_layout.addWidget(self.gender_btn, 1, 0, 1, 1)
        self.g_layout.addWidget(self.gender_line,1, 1, 1, 1)
        self.g_layout.addWidget(self.age_btn, 2, 0, 1, 1)
        self.g_layout.addWidget(self.age_line, 2, 1, 1, 1)
        self.g_layout.addWidget(self.score_btn, 3, 0, 1, 1)
        self.g_layout.addWidget(self.score_line, 3, 1, 1, 1)
        self.g_layout.addWidget(self.info_btn, 4, 0, 1, 1)
        self.g_layout.addWidget(self.info_textedit, 4, 1, 1, 1)
        self.setLayout(self.g_layout)

    def open_dialog_func(self, btn):
        if btn == self.name_btn:                                                                    # 如果name_btn被点击
            name, ok = QInputDialog.getText(self, 'Name Input', 'Please enter the name:')
            # 调用QInputDialog的getText(parent, str, str)方法，参数分别为指定的父类、输入框的标题、输入框提示
            # 方法会返回一个字符串和一个布尔值，若点击输入框的ok按钮，则变量ok就为True
            if ok:
                self.name_line.setText(name)                                                  # 调用QLineEdit的setText()方法将其文本设为所输入的内容
        elif btn == self.gender_btn:                                                               # 如果gender_btn被点击
            gender_list = ['Female', 'Male']
            gender, ok = QInputDialog.getItem(self, 'Gender Input', 'Please choose the gender:', gender_list, 0, False)
            # getItem(parent, str, str, iterable, int, bool)方法参数分别为指定的父类、输入框的标题、输入框提示以及:
            # 第四个参数:要加入的选项内容，传入item_list列表，可以让用户选择男性或女性
            # 第五个参数:最初显示的选项，0代表刚开始显示第一个选项，即Female
            # 第六个参数:是否可编辑，这里设为False，不可编辑
            if ok:
                self.gender_line.setText(gender)
        elif btn == self.age_btn:
            age, ok = QInputDialog.getInt(self, 'Age Input', 'Please select the age:')
            if ok:
                self.age_line.setText(str(age))
        elif btn == self.score_btn:
            score, ok = QInputDialog.getDouble(self, 'Score Input', 'Please select the score:')
            if ok:
                self.score_line.setText(str(score))
        else:
            info, ok = QInputDialog.getMultiLineText(self, 'Info Input', 'Please enter the info:')
            if ok:
                self.info_textedit.setText(info)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())