import sys
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout

# QTimer定时器会根据设定的时间不断发出timeout信号并调用连接的槽函数
class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.label = QLabel('0', self)
        self.label.setAlignment(Qt.AlignCenter)                                         # setAlignment(Qt.AlignCenter)让控件居中显示

        self.step = 0                                                                                           # step变量用于计数，通过QTimer来不断增加

        self.timer = QTimer(self)                                                                    # 实例化一个QTimer
        self.timer.timeout.connect(self.update_func)                              # 连接信号timeout与槽函数update_func()

        self.ss_button = QPushButton('Start', self)                                    # 实例化一个QPushButton
        self.ss_button.clicked.connect(self.start_stop_func)                  # 连接信号clicked与槽函数start_stop_func()

        self.v_layout = QVBoxLayout()
        self.v_layout.addWidget(self.label)
        self.v_layout.addWidget(self.ss_button)

        self.setLayout(self.v_layout)

    def start_stop_func(self):                                                                      # 按钮按下后，判断:
        if not self.timer.isActive():                                                                 # isActive()方法来判断定时器是否处于激活状态
            self.ss_button.setText('Stop')                                                       # 没有激活，则将按钮文字变成Stop
            self.timer.start(100)                                                                        # 激活timer，并且每100毫秒(0.1秒)触发timeout信号
        else:
            self.ss_button.setText('Start')                                                       # 激活了，则将按钮文字变成Start
            self.timer.stop()                                                                               # 停止timer

    def update_func(self):                                                                            # 每次调用step+1, 并用QLabel显示当前step
        self.step += 1
        self.label.setText(str(self.step))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())