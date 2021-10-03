import sys
from PyQt5.QtWidgets import QApplication, QComboBox

class Demo(QComboBox):
    def __init__(self):
        super(Demo, self).__init__()
        my_list = ['A', 'B', 'C', 'D']
        self.addItems(my_list)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    qss = 'QComboBox::drop-down {image: url(drop-down.png)}'  # 1
    demo.setStyleSheet(qss)
    demo.show()
    sys.exit(app.exec_())