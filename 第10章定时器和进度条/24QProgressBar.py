import sys
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import QApplication, QWidget, QProgressBar, QPushButton, QHBoxLayout, QVBoxLayout


class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.progressbar = QProgressBar(self)                                             # 实例化一个QProgressBar
        # self.progressbar.setOrientation(Qt.Vertical)                              # 设置为垂直进度条，默认水平
        self.progressbar.setMinimum(0)
        self.progressbar.setMaximum(100)
        # self.progressbar.setRange(0, 100)

        self.step = 0                                                                                           # step变量用于计数

        self.timer = QTimer(self)                                                                    # 实例化一个QTimer
        self.timer.timeout.connect(self.update_func)                              # 连接信号timeout与槽函数update_func()

        self.ss_button = QPushButton('Start', self)                                     # 实例化一个QPushButton(Start)
        self.ss_button.clicked.connect(self.start_stop_func)                   # 连接信号clicked与槽函数start_stop_func()
        self.reset_button = QPushButton('Reset', self)                              # 实例化一个QPushButton(Reset)
        self.reset_button.clicked.connect(self.reset_func)                       # 连接信号clicked与槽函数reset_func()

        self.h_layout = QHBoxLayout()
        self.v_layout = QVBoxLayout()

        self.h_layout.addWidget(self.ss_button)
        self.h_layout.addWidget(self.reset_button)
        self.v_layout.addWidget(self.progressbar)
        self.v_layout.addLayout(self.h_layout)

        self.setLayout(self.v_layout)

    def start_stop_func(self):                                                                      # 按钮按下后，判断:
        if self.ss_button.text() == 'Start':                                                      # 按钮为Start
            self.ss_button.setText('Stop')                                                       # 按钮变为Stop
            self.timer.start(100)                                                                        # 激活timer，并且每100毫秒(0.1秒)触发timeout信号
        else:                                                                                                        # 按钮为Stop
            self.ss_button.setText('Start')                                                       # 按钮变为Start
            self.timer.stop()                                                                               # 停止timer

    def update_func(self):                                                                            # 每次调用step+1, 并用progressbar显示当前step
        self.step += 1
        self.progressbar.setValue(self.step)

        if self.step >= 100:                                                                                # 如果step大于100,按钮变为Start,停止timer,清零step
            self.ss_button.setText('Start')
            self.timer.stop()
            self.step = 0

    def reset_func(self):                                                                                # reset:按钮变为Start,停止timer,清零step
        self.progressbar.reset()
        self.ss_button.setText('Start')
        self.timer.stop()
        self.step = 0


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())