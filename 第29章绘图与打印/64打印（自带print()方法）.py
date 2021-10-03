import sys
from PyQt5.QtPrintSupport import QPrintDialog, QPrinter
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QTextEdit, QVBoxLayout


class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.text_edit = QTextEdit(self)
        self.print_btn = QPushButton('Print', self)
        self.print_btn.clicked.connect(self.open_printer_func)

        self.printer = QPrinter()

        self.v_layout = QVBoxLayout()
        self.v_layout.addWidget(self.text_edit)
        self.v_layout.addWidget(self.print_btn)
        self.setLayout(self.v_layout)

    # self.text_edit->self.printer
    def open_printer_func(self):
        printer_dialog = QPrintDialog(self.printer)
        if printer_dialog.exec_():
            self.text_edit.print(self.printer)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())