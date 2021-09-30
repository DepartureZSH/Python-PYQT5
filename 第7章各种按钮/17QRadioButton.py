import sys
import time

from PyQt5.QtGui import QPixmap,QMovie
from PyQt5.QtWidgets import QApplication, QWidget, QRadioButton, QLabel, QHBoxLayout, QVBoxLayout,QPushButton

class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.off_button = QRadioButton('off', self)                  # 实例化三个单选按钮，一个off，另一个为on
        self.on_button = QRadioButton('on', self)

        self.pic_label = QLabel(self)                                            # 用QLabel控件来显示图片

        self.button_h_layout = QHBoxLayout()
        self.pic_h_layout = QHBoxLayout()
        self.all_v_layout = QVBoxLayout()

        self.layout_init()
        self.radiobutton_init()
        self.label_init()

    def layout_init(self):
        self.pic_h_layout.addStretch(1)                             # 添加一个占位符
        self.pic_h_layout.addWidget(self.pic_label)       # 因为左右都有一个占位符，该图像居中
        self.pic_h_layout.addStretch(1)                             # 添加一个占位符
        self.button_h_layout.addWidget(self.off_button)
        self.button_h_layout.addWidget(self.on_button)
        self.all_v_layout.addLayout(self.pic_h_layout)
        self.all_v_layout.addLayout(self.button_h_layout)

        self.setLayout(self.all_v_layout)

    def radiobutton_init(self):
        self.off_button.setChecked(True)                                                    # 将off单选按钮设为选中状态
        self.off_button.toggled.connect(self.on_off_bulb_func)            # 连接toggled信号与槽函数on_off_bulb_func
        # self.on_button.toggled.connect(self.on_off_bulb_func)

    def label_init(self):
        self.pic_label.setPixmap(QPixmap('wuwuwu.png'))                    # 初始化空调图片

    def on_off_bulb_func(self):                                                                  # 空调控制函数
        if self.off_button.isChecked():
            self.pic_label.setPixmap(QPixmap('wuwuwu.png'))
        else:
            self.gif = QMovie('wuwuwu.gif')
            self.pic_label.setMovie(self.gif)
            self.gif.start()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())