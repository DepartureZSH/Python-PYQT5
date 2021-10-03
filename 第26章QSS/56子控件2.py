import sys
from PyQt5.QtWidgets import QApplication, QSpinBox


class Demo(QSpinBox):
    def __init__(self):
        super(Demo, self).__init__()
        self.setMinimum(0)
        self.setMaximum(100)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    qss = """
          QSpinBox::up-button {image: url(up-arrow.png)}
          QSpinBox::down-button {image: url(down-arrow.png)}  
          """
    demo.setStyleSheet(qss)
    demo.show()
    sys.exit(app.exec_())