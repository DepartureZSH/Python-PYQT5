import sys
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import Qt, QThread, pyqtSignal
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout


class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.resize(300, 300)

        self.label = QLabel('None', self)
        self.label.setAlignment(Qt.AlignCenter)

        self.movie = QMovie(self)
        self.movie.setFileName('loading.gif')

        self.btn = QPushButton('Start', self)
        self.btn.clicked.connect(self.start_countdown_func)

        self.thread = MyThread()
        self.thread.ok_signal.connect(self.show_result_func)

        self.v_layout = QVBoxLayout()
        self.v_layout.addWidget(self.label)
        self.v_layout.addWidget(self.btn)
        self.setLayout(self.v_layout)

    def start_countdown_func(self):
        self.label.setMovie(self.movie)
        self.movie.start()
        self.thread.start()

    def show_result_func(self):
        self.movie.stop()
        self.label.setText("Time's Up!")


class MyThread(QThread):
    ok_signal = pyqtSignal()

    def __init__(self):
        super(MyThread, self).__init__()
        self.countdown = 1000000

    def run(self):
        while self.countdown > 0:
            self.countdown -= 1
            print(self.countdown)

        self.ok_signal.emit()
        self.countdown = 1000000


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())