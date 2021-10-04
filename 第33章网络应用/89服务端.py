import sys
from PyQt5.QtCore import Qt, QTimer, QDateTime
from PyQt5.QtNetwork import QUdpSocket, QHostAddress
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout

# Udp类似于写信，给一个ip地址寄信
class Server(QWidget):

    def __init__(self):
        super(Server, self).__init__()

        # 实例化一个QUdpSocket对象
        self.sock = QUdpSocket(self)

        # 实例化QLabel控件
        self.label = QLabel('0', self)
        self.label.setAlignment(Qt.AlignCenter)
        # 实例化QPushButton控件
        self.btn = QPushButton('Start Server', self)
        # 按钮所连接的槽函数用来控制定时器QTimer的启动与停止
        self.btn.clicked.connect(self.start_stop_slot)

        self.v_layout = QVBoxLayout()
        self.v_layout.addWidget(self.label)
        self.v_layout.addWidget(self.btn)
        self.setLayout(self.v_layout)

        # 实例化一个QTimer对象，并将timeout信号和槽函数连接起来
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.send_data_slot)

    # 当定时器启动后，服务器每过一秒就会向客户端发送数据
    def start_stop_slot(self):
        if not self.timer.isActive():
            self.btn.setText('Stop Server')
            self.timer.start(1000)
        else:
            self.btn.setText('Start Server')
            self.timer.stop()


    def send_data_slot(self):
        message = QDateTime.currentDateTime().toString()    # 首先获取到当前的系统时间并存储到message变量中
        self.label.setText(message)                         # 将QLabel控件的值设为message显示在窗口中

        datagram = message.encode()                         # 调用encode()方法对message进行编码以用于传输
        # 调用QUdpSocket对象的writeDatagram()方法将编码后的字节数据发送到 目标主机地址 ，目标端口为6666
        self.sock.writeDatagram(datagram, QHostAddress.LocalHost, 6666)
# 常量                                                值描述
# QHostAddress.Null                 空地址对象,等同于QHostAddress()
# QHostAddress.LocalHost            IPv4本地主机地址。等同于QHostAddress(“127.0.0.17)
# QHostAddress.LocalHostIPv6        IPv6本地主机地址,等同于QHostAddress("::1"")
# QHostAddress.Broadcast            IPv4广播地址,等同于QHostAddress("255.255.255.255")
# QHostAddress.AnyIPv4              任何IPv4地址，等同于QHostAddress(0.0.0.0"),与该常量绑定的套接字只会监听IPv4接口
# QHostAddress.AnyIPv4              任何IPv6地址,等同于QHostAddress(::)，与该常量绑定的套接字只会监听IPv6接口
# QHostAddressAny                   任何双协议栈地址,与该常量绑定的套接字可以监听IPv4接口和IPv6接口

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Server()
    demo.show()
    sys.exit(app.exec_())
