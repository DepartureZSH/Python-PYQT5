import sys
from PyQt5.QtNetwork import QUdpSocket, QHostAddress
from PyQt5.QtWidgets import QApplication, QWidget, QTextBrowser, QVBoxLayout


class Client(QWidget):

    def __init__(self):
        super(Client, self).__init__()

        # 实例化QUdpSocket（QUdp插槽）对象
        # 调用bind()方法绑定地址和端口
        # 每次可以准备读取新数据时，readyRead信号就会发射，连接该信号与槽函数（进行读取操作）
        self.sock = QUdpSocket(self)
        self.sock.bind(QHostAddress.Any, 6666)
        self.sock.readyRead.connect(self.read_data_slot)

        # 实例化一个QTextBrowser文本浏览框对象并进行布局
        self.browser = QTextBrowser(self)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.browser)
        self.setLayout(self.layout)

    def read_data_slot(self):
        # 首先调用hasPendingDatagrams()来判断是否还有要读取的数据
        while self.sock.hasPendingDatagrams():
            # 如果有的话就调用readDatagram()来读取数据
            # 传入该方法的参数为要读取的数据大小（用pendingDatagramSize()方法获取）
            datagram, host, port = self.sock.readDatagram(self.sock.pendingDatagramSize())
            # readDatagram()一共返回三个值，分别是数据(字节)，主机地址(QHostAddress对象)以及端口号(整型值)
            # 用decode()将数据解码，用QHostAddress对象的toString()方法来获取到地址字符串
            message = 'Date time: {}\nHost: {}\nPort: {}\n\n'.format(datagram.decode(), host.toString(), port)
            # 最后调用append()方法将message值显示在QTextBrowser控件上
            self.browser.append(message)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Client()
    demo.show()
    sys.exit(app.exec_())
