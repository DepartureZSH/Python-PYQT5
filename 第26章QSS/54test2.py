import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QVBoxLayout


class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.button = QPushButton('button', self)
        self.label = QLabel('label', self)
        self.label.setAlignment(Qt.AlignCenter)
        self.line_edit = QLineEdit(self)

        self.v_layout = QVBoxLayout()
        self.v_layout.addWidget(self.button)
        self.v_layout.addWidget(self.label)
        self.v_layout.addWidget(self.line_edit)
        self.setLayout(self.v_layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    qss = 'QPushButton, QLabel, QLineEdit {color: red}'
    # qss = 'QPushButton {color: red}\
    #             QLabel {color: red}\
    #             QLineEdit {color: red}'
    demo.setStyleSheet(qss)
    demo.show()
    sys.exit(app.exec_())
