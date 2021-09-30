import sys
from PyQt5.QtWidgets import QApplication, QWidget, QComboBox, QFontComboBox, QLineEdit, QMessageBox, QVBoxLayout


class Demo(QWidget):
    choice = 'a'
    choice_list = ['b', 'c', 'd', 'e']

    def __init__(self):
        super(Demo, self).__init__()

        self.combobox_1 = QComboBox(self)               # 实例化一个QComboBox，普通的下拉框，框里没有内容的，需要添加
        self.combobox_2 = QFontComboBox(self)       # 实例化一个QFontComboBox，字体下拉框，继承于QComboBox，该字体下拉框里会默认有许多字体供选择

        self.lineedit = QLineEdit(self)                               # 实例化一个单行文本输入框，输入框中字体会根据以上选择发生变化

        self.v_layout = QVBoxLayout()

        self.layout_init()
        self.combobox_init()

    def layout_init(self):
        self.v_layout.addWidget(self.combobox_1)
        self.v_layout.addWidget(self.combobox_2)
        self.v_layout.addWidget(self.lineedit)

        self.setLayout(self.v_layout)

    def combobox_init(self):
        self.combobox_1.addItem(self.choice)                 # addItem()方法是添加一个选项
        self.combobox_1.addItems(self.choice_list)        # addItems()接收一个可循环参数，这里传入了列表self.choice_list

        # 当下拉框当前选项发生变化变化的话，则会触发序号变化currentIndexChanged信号和文本变化currentTextChanged信号
        self.combobox_1.currentIndexChanged.connect(lambda: self.on_combobox_func(self.combobox_1))   # 连接信号currentIndexChanged(序号变化)与槽函数(带参数要用lambda)
        # self.combobox_1.currentTextChanged.connect(lambda: self.on_combobox_func(self.combobox_1))  # 连接信号currentTextChanged(文本变化)与槽函数(带参数要用lambda)

        self.combobox_2.currentFontChanged.connect(lambda: self.on_combobox_func(self.combobox_2))
        # self.combobox_2.currentFontChanged.connect(lambda: self.on_combobox_func(self.combobox_2))

    def on_combobox_func(self, combobox):                                         # 通过传入的combobox判断combobox种类
        if combobox == self.combobox_1:                 # 当combobox_1时，出现信息框，并且显示当前文本和及文本序号
            QMessageBox.information(self, 'ComboBox 1', '{}: {}'.format(combobox.currentIndex(), combobox.currentText()))      # currentIndex()方法获取当前文本序号，currentText()方法获取当前文本
        else:                                                                       # 当combobox_2时，通过setFont()设置字体，currentFont()获取字体下拉框的当前字体
            self.lineedit.setFont(combobox.currentFont())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())