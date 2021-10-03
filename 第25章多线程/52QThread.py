import sys
from PyQt5.QtCore import Qt, QThread, pyqtSignal
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QHBoxLayout, QVBoxLayout
# 设计思路：
# MyThread类先继承QThread类，把耗时的操作放入run()函数中
# 将该线程在Demo类中实例化并调用start()就可以使用
# 再通过信号连接，让界面上的数字发生变化

class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()

        self.button = QPushButton('Start', self)
        self.button.clicked.connect(self.count_func)
        self.button_2 = QPushButton('Stop', self)                                       # 实例化一个停止按钮
        # 并将信号和槽连接起来，该按钮用于停止my_thread线程
        self.button_2.clicked.connect(self.stop_count_func)

        self.label = QLabel('0', self)
        self.label.setAlignment(Qt.AlignCenter)

        self.my_thread = MyThread()
        self.my_thread.my_signal.connect(self.set_label_func)
        # 连接my_thread线程中的my_signal信号和UI线程中的set_label_func槽函数

        self.h_layout = QHBoxLayout()
        self.v_layout = QVBoxLayout()
        self.h_layout.addWidget(self.button)
        self.h_layout.addWidget(self.button_2)
        self.v_layout.addWidget(self.label)
        self.v_layout.addLayout(self.h_layout)
        self.setLayout(self.v_layout)

    def count_func(self):
        self.my_thread.is_on = True                                                             # 将is_on变量设为True，不然run()函数中循环会直接退出
        self.my_thread.start()                                                                        # 调用start()使用MyThread

    # 在槽函数中我们将label的值设为传递过来的数值
    # 即label.Text<-my_signal<-str(self.count)
    def set_label_func(self, num):
        self.label.setText(num)

    def stop_count_func(self):
        self.my_thread.is_on = False                                                            # 将my_thread中的is_on变量设为False
        self.my_thread.count = 0                                                                   # 将count变量重设为0
        # 此时发现界面上的数字已经不会再改变，my_thread线程运行结束

class MyThread(QThread):
    my_signal = pyqtSignal(str)             # 自定义一个信号my_signal
    # pyqtSignal(str)加上str就代表这个信号可以传一个字符串数值

    def __init__(self):
        super(MyThread, self).__init__()
        self.count = 0
        # is_on变量->通过控制run函数中的while循环->控制my_thread线程的启动和停止
        self.is_on = True

    def run(self):
        while self.is_on:
            print(self.count)
            self.count += 1
            self.my_signal.emit(str(self.count))                                             # 调用信号的emit()函数释放信号
            # 传入str(self.count)字符串值
            # (count变量本身是int类型，而信号要传递的是字符串，所以要调用str()方法将count转为字符串)
            # 所以每次循环都会释放信号，而该信号会同时传递count变量的字符串值
            self.sleep(1)                                                                                       # QThread.sleep()方法可以强制让当前线程睡眠相应的秒数


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
