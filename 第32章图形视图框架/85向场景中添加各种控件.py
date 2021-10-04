import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QGraphicsScene, QGraphicsView, QGraphicsWidget, QGraphicsGridLayout, \
                            QGraphicsLinearLayout, QLabel, QLineEdit, QPushButton


class Demo(QGraphicsView):
    def __init__(self):
        super(Demo, self).__init__()
        self.resize(220, 110)
#########################################################################
#                     实例化控件并添加入场景                              #
        # 实例化需要的控件，因为父类不是QGraphicsView，所以不加self
        self.user_label = QLabel('Username:')
        self.pwd_label = QLabel('Password:')
        self.user_line = QLineEdit()
        self.pwd_line = QLineEdit()
        self.login_btn = QPushButton('Log in')
        self.signin_btn = QPushButton('Sign in')

        # 实例化一个场景对象，然后调用addWidget()方法来添加控件
        self.scene = QGraphicsScene()
        # addWidget()方法返回的值是一个QGraphicsProxyWidget代理对象
        # 可以在场景中通过控制代理对象来操作控件
        # 不过信号和槽还是要直接应用到控件上
        self.user_label_proxy = self.scene.addWidget(self.user_label)
        self.pwd_label_proxy = self.scene.addWidget(self.pwd_label)
        self.user_line_proxy = self.scene.addWidget(self.user_line)
        self.pwd_line_proxy = self.scene.addWidget(self.pwd_line)
        self.login_btn_proxy = self.scene.addWidget(self.login_btn)
        self.signin_btn_proxy = self.scene.addWidget(self.signin_btn)
        print(type(self.user_label_proxy))
###########################################################################
#          布局器->QGraphicsWidget->scene->QGraphicsView                  #
        # 进行布局：
        # QGraphicsGridLayout网格布局
        # QGraphicsLinearLayout线形布局(水平和垂直布局结合)
        self.g_layout = QGraphicsGridLayout()
        self.l_h_layout = QGraphicsLinearLayout()               # 默认是水平
        self.l_v_layout = QGraphicsLinearLayout(Qt.Vertical)
        # addWidget()和addLayout() -> addItem()
        self.g_layout.addItem(self.user_label_proxy, 0, 0, 1, 1)
        self.g_layout.addItem(self.user_line_proxy, 0, 1, 1, 1)
        self.g_layout.addItem(self.pwd_label_proxy, 1, 0, 1, 1)
        self.g_layout.addItem(self.pwd_line_proxy, 1, 1, 1, 1)
        self.l_h_layout.addItem(self.login_btn_proxy)
        self.l_h_layout.addItem(self.signin_btn_proxy)
        self.l_v_layout.addItem(self.g_layout)
        self.l_v_layout.addItem(self.l_h_layout)

        # 实例化一个QGraphicsWidget
        self.widget = QGraphicsWidget()
        # 调用setLayout()方法来设置整体布局
        self.widget.setLayout(self.l_v_layout)

        # 将QGraphicsWidget对象添加到场景中
        # 嵌入的控件自然也就在场景上了
        self.scene.addItem(self.widget)

        self.setScene(self.scene)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
