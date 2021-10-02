import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout


class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.pic_label = QLabel(self)                                                               # pic_label用于设置图片，
        self.pic_label.setPixmap(QPixmap('images/keyboard.png'))     # 先将初始化的图片设为keyboard.png
        self.pic_label.setAlignment(Qt.AlignCenter)

        self.key_label = QLabel('No Key Pressed', self)                              # key_label用于记录按键状态
        self.key_label.setAlignment(Qt.AlignCenter)

        self.v_layout = QVBoxLayout()
        self.v_layout.addWidget(self.pic_label)
        self.v_layout.addWidget(self.key_label)
        self.setLayout(self.v_layout)

    def keyPressEvent(self, QKeyEvent):                                                   # keyPressEvent()为键盘某个键被按下时所触发的响应函数
        if QKeyEvent.key() == Qt.Key_Up:                                                    # 在这个函数中我们判断被按下的键种类
            self.pic_label.setPixmap(QPixmap('images/up.png'))             # 并将pic_label设为相应的箭头图片
            self.key_label.setText('Key Up Pressed')                                    # 将key_label设为相应的文本
        elif QKeyEvent.key() == Qt.Key_Down:
            self.pic_label.setPixmap(QPixmap('images/down.png'))
            self.key_label.setText('Key Down Pressed')
        elif QKeyEvent.key() == Qt.Key_Left:
            self.pic_label.setPixmap(QPixmap('images/left.png'))
            self.key_label.setText('Key Left Pressed')
        elif QKeyEvent.key() == Qt.Key_Right:
            self.pic_label.setPixmap(QPixmap('images/right.png'))
            self.key_label.setText('Key Right Pressed')

    def keyReleaseEvent(self, QKeyEvent):  # 4
        self.pic_label.setPixmap(QPixmap('images/keyboard.png'))
        self.key_label.setText('Key Released')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())