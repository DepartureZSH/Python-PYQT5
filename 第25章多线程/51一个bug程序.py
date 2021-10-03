import sys
import time
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout


class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.count = 0

        self.button = QPushButton('Count', self)
        self.button.clicked.connect(self.count_func)
        self.label = QLabel('0', self)
        self.label.setAlignment(Qt.AlignCenter)

        self.v_layout = QVBoxLayout()
        self.v_layout.addWidget(self.label)
        self.v_layout.addWidget(self.button)
        self.setLayout(self.v_layout)

    def count_func(self):
        while True:
            self.count += 1
            self.label.setText(str(self.count))
            print(self.count)
            time.sleep(1)
        # 出现的现象：程序无响应，但是count不断计数
        # 因为time库是纯python的，而PyQt的背后是Qt，这是纯C++的
        # 当time.sleep(1)时，它占用了UI线程（主线程）
        # 没有将CPU控制权交还给Qt，从而造成界面卡死

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())