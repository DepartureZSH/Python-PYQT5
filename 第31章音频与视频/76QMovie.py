import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QMovie, QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QHBoxLayout, QVBoxLayout


class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.movie = QMovie(self)                       # 实例化一个QMovie对象
        self.movie.setFileName('images/zootopia.gif')   # setFileName()设置要播放的gif文件
        self.movie.jumpToFrame(0)                       # jumpToFrame()可以选择让gif跳转到某一帧
        # 如果要使用jumpToFrame()跳转到某一帧的话该帧必须先播放过
        # 在初始化的时候只能jumpToFrame(0)跳转到第一帧

        self.label = QLabel(self)                               # QLabel控件用于显示QMovie
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setMovie(self.movie)

        self.speed = 100
        # self.speed变量用于控制播放速度，在之后快进和快退功能中用到

        # 实例化几个按钮，分别是：开始、暂停、停止、快进、快退和截图。
        # 接着设置按钮的图标，并进行信号和槽的连接
        self.start_btn = QPushButton(self)
        self.pause_btn = QPushButton(self)
        self.stop_btn = QPushButton(self)
        self.fast_btn = QPushButton(self)
        self.back_btn = QPushButton(self)
        self.screenshot_btn = QPushButton(self)

        self.start_btn.setIcon(QIcon('images/start.png'))
        self.pause_btn.setIcon(QIcon('images/pause.png'))
        self.stop_btn.setIcon(QIcon('images/stop.png'))
        self.fast_btn.setIcon(QIcon('images/fast_forward.png'))
        self.back_btn.setIcon(QIcon('images/back_forward.png'))
        self.screenshot_btn.setIcon(QIcon('images/screenshot.png'))

        self.start_btn.clicked.connect(lambda: self.btn_func(self.start_btn))
        self.pause_btn.clicked.connect(lambda: self.btn_func(self.pause_btn))
        self.stop_btn.clicked.connect(lambda: self.btn_func(self.stop_btn))
        self.fast_btn.clicked.connect(lambda: self.btn_func(self.fast_btn))
        self.back_btn.clicked.connect(lambda: self.btn_func(self.back_btn))
        self.screenshot_btn.clicked.connect(lambda: self.btn_func(self.screenshot_btn))

        self.h_layout = QHBoxLayout()
        self.v_layout = QVBoxLayout()

        self.h_layout.addWidget(self.back_btn)
        self.h_layout.addWidget(self.start_btn)
        self.h_layout.addWidget(self.pause_btn)
        self.h_layout.addWidget(self.stop_btn)
        self.h_layout.addWidget(self.fast_btn)
        self.h_layout.addWidget(self.screenshot_btn)
        self.v_layout.addWidget(self.label)
        self.v_layout.addLayout(self.h_layout)
        self.setLayout(self.v_layout)

    def btn_func(self, btn):
        if btn == self.start_btn:           # start_btn: 调用start()方法来开始播放gif文件
            self.movie.start()
        elif btn == self.pause_btn:         # pause_btn: 调用setPaused(True)来暂停播放，传入False则继续播放
            self.movie.setPaused(True)
        elif btn == self.stop_btn:          # stop_btn: 调用stop()方法停止播放
            self.movie.stop()
            self.movie.jumpToFrame(0)       # jumpToFrame(0)目的是为了在停止播放后，画面直接跳转到第一帧
        elif btn == self.fast_btn:          # fast_btn和back_btn:
            self.speed *= 2                 # 先调整self.speed变量大小
            self.movie.setSpeed(self.speed) # 在传入setSpeed()方法中来控制播放速度
        elif btn == self.back_btn:
            self.speed /= 2
            self.movie.setSpeed(self.speed)
        elif btn == self.screenshot_btn:
            self.movie.currentPixmap().save('zootopia.png')
        # screenshot_btn: 使用currentPixmap()方法获取当前帧(此时还是QPixmap类型)，
        # 接着再调用save()方法将该帧保存到本地


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
