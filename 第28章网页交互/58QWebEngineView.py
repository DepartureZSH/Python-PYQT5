import sys
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtGui import QIcon
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QVBoxLayout, QHBoxLayout


class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.resize(1000, 600)              # 通过resize()方法来将窗口大小设为1000x600

        self.back_btn = QPushButton(self)   # 实例化按钮控件、输入框控件以及QWebEngineView控件；
        self.forward_btn = QPushButton(self)
        self.refresh_btn = QPushButton(self)
        self.zoom_in_btn = QPushButton(self)
        self.zoom_out_btn = QPushButton(self)
        self.url_le = QLineEdit(self)

        self.browser = QWebEngineView()

        self.h_layout = QHBoxLayout()
        self.v_layout = QVBoxLayout()

        self.layout_init()
        self.btn_init()
        self.le_init()
        self.browser_init()

    def layout_init(self):
        self.h_layout.setSpacing(0)             # setSpacing()传入参数0代表让各个控件之间不存在间隔
        self.h_layout.addWidget(self.back_btn)
        self.h_layout.addWidget(self.forward_btn)
        self.h_layout.addWidget(self.refresh_btn)
        self.h_layout.addStretch(2)             # 使用addStretch()让输入框和按钮分离开来
        self.h_layout.addWidget(self.url_le)
        self.h_layout.addStretch(2)
        self.h_layout.addWidget(self.zoom_in_btn)
        self.h_layout.addWidget(self.zoom_out_btn)

        self.v_layout.addLayout(self.h_layout)
        self.v_layout.addWidget(self.browser)

        self.setLayout(self.v_layout)

    def browser_init(self):         # 首次运行程序时，QWebEngineView显示百度网页
        self.browser.load(QUrl('https://baidu.com'))
        self.browser.urlChanged.connect(lambda: self.url_le.setText(self.browser.url().toDisplayString()))
        # 信号urlChanged（QWebEngineView控件中），该信号会在每次要加载的网址发生变化时产生
        # 调用QWebEngineView的url()方法获取QUrl对象，然后调用toDisplayString()方法来获取url文本字符串

    def btn_init(self):             # 设置输入框宽度为400并设置占位符提示用户在这里输入网址
        self.back_btn.setIcon(QIcon('images/back.png'))
        self.forward_btn.setIcon(QIcon('images/forward.png'))
        self.refresh_btn.setIcon(QIcon('images/refresh.png'))
        self.zoom_in_btn.setIcon(QIcon('images/zoom_in.png'))
        self.zoom_out_btn.setIcon(QIcon('images/zoom_out.png'))

        self.back_btn.clicked.connect(self.browser.back)
        self.forward_btn.clicked.connect(self.browser.forward)
        self.refresh_btn.clicked.connect(self.browser.reload)
        self.zoom_in_btn.clicked.connect(self.zoom_in_func)
        self.zoom_out_btn.clicked.connect(self.zoom_out_func)

    def le_init(self):
        self.url_le.setFixedWidth(400)
        self.url_le.setPlaceholderText('Search or enter website name')

    def keyPressEvent(self, QKeyEvent):     # Key_Return为大回车，Key_Enter为小回车
        if QKeyEvent.key() == Qt.Key_Return or QKeyEvent.key() == Qt.Key_Enter:
            if self.url_le.hasFocus():      # 判断是否在输入框被编辑的状态下敲击回车
                if self.url_le.text().startswith('https://') or self.url_le.text().startswith('http://'):
                    self.browser.load(QUrl(self.url_le.text()))
                    # 用QUrl()把字符串转为QUrl对象，调用load()方法传入QUrl对象
                else:
                    self.browser.load(QUrl('https://'+self.url_le.text()))

    def zoom_in_func(self):
        self.browser.setZoomFactor(self.browser.zoomFactor()+0.1)

    def zoom_out_func(self):
        self.browser.setZoomFactor(self.browser.zoomFactor()-0.1)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())