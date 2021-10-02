import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QToolBox, QGroupBox, QToolButton, QVBoxLayout


class Demo(QToolBox):                                                     # 因为要显示的最终控件也就是QToolBox，所以就直接继承QToolBox
    def __init__(self):
        super(Demo, self).__init__()
        self.groupbox_1 = QGroupBox(self)                       # 实例化三个QGroupBox控件，目的是将6个头像分别放入这三个QGroupBox中
        self.groupbox_2 = QGroupBox(self)
        self.groupbox_3 = QGroupBox(self)

        self.toolbtn_f1 = QToolButton(self)                         # QToolButton用于显示头像
        self.toolbtn_f2 = QToolButton(self)
        self.toolbtn_f3 = QToolButton(self)
        self.toolbtn_m1 = QToolButton(self)
        self.toolbtn_m2 = QToolButton(self)
        self.toolbtn_m3 = QToolButton(self)

        self.v1_layout = QVBoxLayout()
        self.v2_layout = QVBoxLayout()
        self.v3_layout = QVBoxLayout()

        # 通过addItem(QWidget, Str)方法将QGroupBox添加到QToolBox中
        # 第一个参数为要添加的控件
        # 第二个参数是给每个QToolBox抽屉设定的名称
        self.addItem(self.groupbox_1, 'Couple One')
        self.addItem(self.groupbox_2, 'Couple Two')
        self.addItem(self.groupbox_3, 'Couple Three')
        self.currentChanged.connect(self.print_index_func)      # 连接currentChanged信号(点击不同抽屉触发)与槽函数print_index_func()

        self.layout_init()
        self.groupbox_init()
        self.toolbtn_init()

    def layout_init(self):
        self.v1_layout.addWidget(self.toolbtn_f1)
        self.v1_layout.addWidget(self.toolbtn_m1)
        self.v2_layout.addWidget(self.toolbtn_f2)
        self.v2_layout.addWidget(self.toolbtn_m2)
        self.v3_layout.addWidget(self.toolbtn_f3)
        self.v3_layout.addWidget(self.toolbtn_m3)

    def groupbox_init(self):                                    # 6
        self.groupbox_1.setFlat(True)
        self.groupbox_2.setFlat(True)
        self.groupbox_3.setFlat(True)
        self.groupbox_1.setLayout(self.v1_layout)
        self.groupbox_2.setLayout(self.v2_layout)
        self.groupbox_3.setLayout(self.v3_layout)

    def toolbtn_init(self):                                     # 通过setIcon(QIcon)方法来设置QToolButton的图标
        self.toolbtn_f1.setIcon(QIcon('images/on.png'))
        self.toolbtn_f2.setIcon(QIcon('images/off.png'))
        self.toolbtn_f3.setIcon(QIcon('images/Red.png'))
        self.toolbtn_m1.setIcon(QIcon('images/Green.png'))
        self.toolbtn_m2.setIcon(QIcon('images/Blue.png'))
        self.toolbtn_m3.setIcon(QIcon('images/Yellow.png'))

    def print_index_func(self):
        couple_dict = {
            0: 'Couple One',
            1: 'Couple Two',
            2: 'Couple Three'
        }
        sentence = 'You are looking at {}.'.format(couple_dict.get(self.currentIndex()))
        print(sentence)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())