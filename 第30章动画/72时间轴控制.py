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
        self.timeline.stateChanged.connect(lambda: print(self.timeline.state()))
        # 将stateChanged信号和打印函数连接起来
        # 每当状态发生改变，我们就打印出当前进入的状态：
        # 0代表NotRunning，1代表Paused，2代表Running
        self.timeline.setLoopCount(0)

        self.start_btn = QPushButton('Start', self)
        self.stop_btn = QPushButton('Stop', self)
        self.pause_btn = QPushButton('Pause', self)
        self.resume_btn = QPushButton('Resume', self)

        # 将各个按钮的clicked信号和对应得方法进行连接，运行程序后我们就可以通过这四个按钮来控制动画
        self.start_btn.clicked.connect(self.timeline.start)
        self.stop_btn.clicked.connect(self.timeline.stop)
        self.pause_btn.clicked.connect(lambda: self.timeline.setPaused(True))
        self.resume_btn.clicked.connect(self.timeline.resume)

        self.h_layout = QHBoxLayout()
        self.v_layout = QVBoxLayout()
        self.h_layout.addWidget(self.start_btn)
        self.h_layout.addWidget(self.stop_btn)
        self.h_layout.addWidget(self.pause_btn)
        self.h_layout.addWidget(self.resume_btn)
        self.v_layout.addStretch(1)
        self.v_layout.addLayout(self.h_layout)
        self.setLayout(self.v_layout)

    def set_frame_func(self, frame):
        self.label.move(-100+frame, 100)
        self.update()
        # self.update()避免点了Stop或者Pause按钮后，再点击Start按钮重新开始
        # 窗口中出现了两个QLabel控件，之前停住的QLabel遗留在了窗口上

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())