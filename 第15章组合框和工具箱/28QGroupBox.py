import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QGroupBox, QRadioButton, QLabel, QHBoxLayout, QVBoxLayout


class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.groupbox_1 = QGroupBox('On and Off', self)                       # 实例化两个QGroupBox组合框，第一个用来放置On和Off单选按钮，
        self.groupbox_2 = QGroupBox('Change Color', self)                   # 第二个用来放置各种颜色按钮

        self.red = QRadioButton('Red', self)                                                # 实例化各个颜色按钮
        self.blue = QRadioButton('Blue', self)
        self.green = QRadioButton('Green', self)
        self.yellow = QRadioButton('Yellow', self)
        self.color_list = [self.red, self.blue, self.green, self.yellow]        # 将各个颜色按钮放在一个列表中，方便使用列表推导式来简化代码

        self.on = QRadioButton('On', self)                                                   # 实例化On和Off单选按钮
        self.off = QRadioButton('Off', self)

        self.pic_label = QLabel(self)                                                               # 实例化一个QLabel控件，用于显示图片

        self.h1_layout = QHBoxLayout()
        self.h2_layout = QHBoxLayout()
        self.h3_layout = QHBoxLayout()
        self.all_v_layout = QVBoxLayout()

        self.layout_init()
        self.radiobutton_init()
        self.label_init()

    def layout_init(self):
        self.h1_layout.addWidget(self.on)
        self.h1_layout.addWidget(self.off)
        self.groupbox_1.setLayout(self.h1_layout)

        self.h2_layout.addWidget(self.red)
        self.h2_layout.addWidget(self.blue)
        self.h2_layout.addWidget(self.green)
        self.h2_layout.addWidget(self.yellow)
        self.groupbox_2.setLayout(self.h2_layout)

        self.h3_layout.addWidget(self.groupbox_1)
        self.h3_layout.addWidget(self.groupbox_2)

        self.all_v_layout.addWidget(self.pic_label)
        self.all_v_layout.addLayout(self.h3_layout)

        self.setLayout(self.all_v_layout)

    def radiobutton_init(self):
        self.yellow.setChecked(True)                                                            # 在radiobutton_init()中，先将yellow单选按钮设为已点击状态，
        for btn in self.color_list:
            btn.clicked.connect(self.change_color_func)                            # 连接各个颜色按钮的clicked信号与槽函数change_color_func()

        self.off.setChecked(True)                                                                  # 将Off按钮设为点击状态
        self.off.toggled.connect(self.on_and_off_func)                           # 将off按钮的 toggled信号与槽函数连接起来

    def label_init(self):                                                                                   # 将刚开始显示的QLabel图片设置为Off.png，然后让其居中显示
        self.pic_label.setPixmap(QPixmap('images/Off.png'))
        self.pic_label.setAlignment(Qt.AlignCenter)

    def change_color_func(self):
        if self.on.isChecked():                                                                         # 判断On单选按钮是否是已点击状态
            # 获取图片路径path
            path = 'images/{}.png'.format([btn.text() for btn in self.color_list if btn.isChecked()][0])
            # 先以 列表推导式 循环判断 是哪一个颜色按钮处于点击状态，然后将该按钮的显示文本获取过来
            self.pic_label.setPixmap(QPixmap(path))                                  # 将QLabel设为相应的图片

    def on_and_off_func(self):
        if self.on.isChecked():
            path = 'images/{}.png'.format([btn.text() for btn in self.color_list if btn.isChecked()][0])
            self.pic_label.setPixmap(QPixmap(path))
        else:
            self.pic_label.setPixmap(QPixmap('images/Off.png'))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())