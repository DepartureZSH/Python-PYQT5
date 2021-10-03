import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QScrollArea, QScrollBar, \
                            QHBoxLayout, QVBoxLayout


class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.label = QLabel(self)                                                                      # 实例化一个QLabel控件用于显示大图
        self.label.setPixmap(QPixmap('image.jpg'))
        self.label.setScaledContents(True)                                                  # setScaledContents(True)让图片随QLabel大小变化而变化，即自适应

        self.scroll_area = QScrollArea(self)                                                  # 实例化一个QScrollArea控件
        self.scroll_area.setWidget(self.label)                                              # setWidget()方法:将QLabel设为滚动区域中的控件
        self.scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)    # 将滚动区域自带的横向滚动条给隐藏掉

        self.scrollbar = QScrollBar(Qt.Horizontal, self)                              # 实例化一个横向滚动条
        self.scrollbar.setMaximum(self.scroll_area.horizontalScrollBar().maximum())
        # setMaximum()方法设置最大值,即跟QScrollArea被隐藏掉的横向滚动条的最大值一样

        # 实例化两个按钮用于放大缩小QLabel控件(图片也会相应的放大缩小)
        self.bigger_btn = QPushButton('Zoom in', self)
        self.smaller_btn = QPushButton('Zoom out', self)

        self.bigger_btn.clicked.connect(self.bigger_func)                        # 连接点击Zoom in按钮的信号与槽函数bigger_func()
        self.smaller_btn.clicked.connect(self.smaller_func)                   # 连接点击Zoom out按钮的信号与槽函数smaller_func
        self.scrollbar.valueChanged.connect(self.sync_func)                 # 连接信号valueChanged(自定义的滚动条值改变)与槽函数sync_func()

        self.h_layout = QHBoxLayout()
        self.h_layout.addWidget(self.bigger_btn)
        self.h_layout.addWidget(self.smaller_btn)

        self.v_layout = QVBoxLayout()
        self.v_layout.addWidget(self.scroll_area)
        self.v_layout.addWidget(self.scrollbar)
        self.v_layout.addLayout(self.h_layout)
        self.setLayout(self.v_layout)

    def bigger_func(self):
        self.label.resize(self.label.width()*1.2, self.label.height()*1.2)   # 将QLabel控件放大20%
        self.scrollbar.setMaximum(self.scroll_area.horizontalScrollBar().maximum())
        # 设置QScrollBar的最大值为QScrollArea横向滚动条的最大值

    def smaller_func(self):
        self.label.resize(self.label.width() * 0.8, self.label.height() * 0.8)  # 将QLabel控件缩小20%
        self.scrollbar.setMaximum(self.scroll_area.horizontalScrollBar().maximum())
        # 设置QScrollBar的最大值为QScrollArea横向滚动条的最大值

    def sync_func(self):
        self.scroll_area.horizontalScrollBar().setValue(self.scrollbar.value())
        # 让QScrollArea横向滚动条的当前值和QScrollBar的值同步


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())