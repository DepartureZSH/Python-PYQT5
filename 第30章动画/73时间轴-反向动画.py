import sys
from PyQt5.QtCore import QTimeLine
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QHBoxLayout, QVBoxLayout


class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.resize(600, 600)

        self.label = QLabel('Hello PyQt5', self)
        self.label.move(-100, 100)

        self.timeline = QTimeLine(5000, self)
        self.timeline.setFrameRange(0, 700)
        self.timeline.frameChanged.connect(self.set_frame_func)
        self.timeline.setLoopCount(0)
        self.timeline.start()

        self.forward_btn = QPushButton('Forward', self)
        self.backward_btn = QPushButton('Backward', self)
        self.forward_btn.move(150, 0)
        self.backward_btn.move(350, 0)
        self.forward_btn.clicked.connect(lambda: self.change_direction_func(self.forward_btn))
        self.backward_btn.clicked.connect(lambda: self.change_direction_func(self.backward_btn))

    def set_frame_func(self, frame):
        self.label.move(-100+frame, 100)

    def change_direction_func(self, btn):                       # 调用setDirection()方法传入方向值
        if btn == self.forward_btn:
            self.timeline.setDirection(QTimeLine.Forward)
        else:
            self.timeline.setDirection(QTimeLine.Backward)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())