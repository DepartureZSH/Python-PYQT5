import sys
from PyQt5.QtCore import Qt
from PyQt5.QtNetwork import QTcpSocket, QHostAddress
from PyQt5.QtWidgets import QApplication, QWidget, QTextBrowser, QTextEdit, QSplitter, QPushButton, \
    QHBoxLayout, QVBoxLayout


class Client(QWidget):
    def __init__(self):
        super(Client, self).__init__()
        self.resize(500, 450)
        # 实例化控件并完成界面布局，布局代码放在layout_init()函数中
        self.browser = QTextBrowser(self)
        self.edit = QTextEdit(self)

        self.splitter = QSplitter(self)
        self.splitter.setOrientation(Qt.Vertical)
        self.splitter.addWidget(self.browser)
        self.splitter.addWidget(self.edit)
        self.splitter.setSizes([350, 100])

        self.send_btn = QPushButton('Send', self)
        self.close_btn = QPushButton('Close', self)

        self.h_layout = QHBoxLayout()
        self.v_layout = QVBoxLayout()

        # 实例化一个QTcpSocket对象
        self.sock = QTcpSocket(self)
        # 调用connectToHost()方法在指定端口上连接目标主机(此时会进行三次握手操作)
        # 如果客户端和服务端连接成功，则会发射connected()信号
        self.sock.connectToHost(QHostAddress.LocalHost, 6666)

        self.layout_init()
        self.signal_init()

    def layout_init(self):
        self.h_layout.addStretch(1)
        self.h_layout.addWidget(self.close_btn)
        self.h_layout.addWidget(self.send_btn)
        self.v_layout.addWidget(self.splitter)
        self.v_layout.addLayout(self.h_layout)
        self.setLayout(self.v_layout)

    def signal_init(self):
        self.send_btn.clicked.connect(self.write_data_slot)  # 当用户在文本编辑框QTextEdit中打完字后，点击发送按钮就可以将文本发送给服务端
        self.close_btn.clicked.connect(self.close_slot)      # 当用户点击关闭按钮后，调用close()方法关闭QTcpSocket套接字，当然窗口也得关掉
        self.sock.connected.connect(self.connected_slot)     # 将sock成功连接信号连接到connected_slot()槽函数上
        # 当客户端和服务端连接成功的话，就会发射connected信号
        self.sock.readyRead.connect(self.read_data_slot)     # 将sock准备读取新数据信号连接到read_data_slot()槽函数上
        # 当准备可以读取新数据时，readyRead信号就会发射

    def write_data_slot(self):
        message = self.edit.toPlainText()                   # 首先获取文本编辑框中的文字
        self.browser.append('Client: {}'.format(message))
        datagram = message.encode()
        self.sock.write(datagram)                           # 用write()方法发送
        # (不用再写目标地址和端口，因为之前已经用connectToHost()方法指定了)
        self.edit.clear()                                   # 发送完后我们还有把文本编辑框清空掉

    def connected_slot(self):
        message = 'Connected! Ready to chat! :)'
        self.browser.append(message)

    def read_data_slot(self):
        while self.sock.bytesAvailable():                           # 通过bytesAvailable()方法判断是否有数据
            datagram = self.sock.read(self.sock.bytesAvailable())   # 如果是，则调用read()方法获取bytesAvailable()大小的数据
            message = datagram.decode()
            self.browser.append('Server: {}'.format(message))

    def close_slot(self):
        self.sock.close()
        self.close()

    def closeEvent(self, event):
        self.sock.close()
        event.accept()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Client()
    demo.show()
    sys.exit(app.exec_())
