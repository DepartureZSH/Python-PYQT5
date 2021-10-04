import sys
import json
import requests
from PyQt5.QtNetwork import QTcpServer, QHostAddress
from PyQt5.QtWidgets import QApplication, QWidget, QTextBrowser, QVBoxLayout


class Server(QWidget):
    def __init__(self):
        super(Server, self).__init__()
        self.resize(500, 450)

        # 实例化一个QTextBrowser控件并进行布局
        self.browser = QTextBrowser(self)

        self.v_layout = QVBoxLayout()
        self.v_layout.addWidget(self.browser)
        self.setLayout(self.v_layout)

        # 实例化一个QTcpServer对象，调用listen()方法对指定地址和端口进行监听
        # 如果能够监听，则返回True，否则返回False
        self.server = QTcpServer(self)
        # QHostAddress.LocalHost本机作为服务器地址，即127.0.0.1，6666端口
        if not self.server.listen(QHostAddress.LocalHost, 6666):
            self.browser.append(self.server.errorString())                  # 调用errorString()方法来获取监听失败的原因
        # 每当有来自客户端的新连接请求，QTcpServer就会发送newConnection信号。
        self.server.newConnection.connect(self.new_socket_slot)

    def new_socket_slot(self):
        # 调用nextPendingConnection()方法来得到一个与客户端连接的QTcpSocket对象
        sock = self.server.nextPendingConnection()

        # 通过peerAddress()方法和peerPort()方法获取到客户端所在的主机地址和以及使用的端口
        peer_address = sock.peerAddress().toString()
        peer_port = sock.peerPort()
        news = 'Connected with address {}, port {}'.format(peer_address, str(peer_port))
        self.browser.append(news)

        # 当准备可以读取新数据时，readyRead信号就会发射
        # readyRead信号连接read_data_slot()槽函数
        sock.readyRead.connect(lambda: self.read_data_slot(sock))
        # 当连接关闭的话，就会发射disconnected信号
        sock.disconnected.connect(lambda: self.disconnected_slot(sock))


    def read_data_slot(self, sock):
        while sock.bytesAvailable():
            # 将来自客户端的数据解码
            datagram = sock.read(sock.bytesAvailable())
            message = datagram.decode()
            # 然后作为参数传给get_answer()函数
            answer = self.get_answer(message).replace('{br}', '\n')
            # 当客户端窗口关闭，那么与服务端的连接就会关闭，此时disconnected信号就会发射
            new_datagram = answer.encode()
            sock.write(new_datagram)

    # get_answer()函数来获取青云客智能机器人的回答
    def get_answer(self, message):
        payload = {'key': 'free', 'appid': '0', 'msg': message}
        # 通过api连接青云客智能机器人，可以进入下面的网址看看
        r = requests.get("http://api.qingyunke.com/api.php", params=payload)
        answer = json.loads(r.text)['content']
        return answer

    # 在屏幕上显示失联客户端所在的主机地址和使用的端口
    def disconnected_slot(self, sock):
        peer_address = sock.peerAddress().toString()
        peer_port = sock.peerPort()
        news = 'Disconnected with address {}, port {}'.format(peer_address, str(peer_port))
        self.browser.append(news)
        # 调用close()方法关闭套接字
        sock.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Server()
    demo.show()
    sys.exit(app.exec_())
