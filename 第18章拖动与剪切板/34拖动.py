import sys
from PyQt5.QtWidgets import QApplication, QTextBrowser

# DragEnterEvent: 所拖动目标进入接收该事件的窗口或控件时触发
# DragMoveEvent: 所拖动目标进入窗口或控件后，继续被拖动时触发
# DragLeaveEvent: 所拖动目标离开窗口或控件时触发
# DropEvent: 所拖动目标被放下时触发

# MIME类型数据 #
# 判断函数          获取函数            设置函数                MIME类型
# hasText()            text ()                  setText()                   text/plain
# hasHtml()           html()                 setHtml()                  text/html
# hasUrls()             urls()                   setUrls()                  text/url-list
# hasImage()     ImageData()      setImageData()            image/*
# hasColor()       colorData()        setColorData()        application/x-color

class Demo(QTextBrowser):                                               # 继承QTextBrowser
    def __init__(self):
        super(Demo, self).__init__()
        self.setAcceptDrops(True)                                           # setAcceptDrops(True)可让该控件接收放下(Drop)事件

    def dragEnterEvent(self, QDragEnterEvent):               # 当拖动目标进入QTextBrowser的那一刹那，触发dragEnterEvent事件
        print('Drag Enter')
        if QDragEnterEvent.mimeData().hasText():            # 判断所拖动目标的MIME类型是否为text/plain
            QDragEnterEvent.acceptProposedAction()         # 若是，调用acceptProposedAction()来表明可以在QTextBrowser上进行拖放动作
            # 表示已准备好接受传输的数据和由proposalAction()返回的默认操作。
            # 该方法(或者accept()方法)必须在dragEnterEvent()中调用，否则，dropEvent()不会被调用。

    def dragMoveEvent(self, QDragMoveEvent):              # 当目标进入窗体后，如果不放下而是继续移动，则触发dragMoveEvent事件
        print('Drag Move')

    def dragLeaveEvent(self, QDragLeaveEvent):              # 将进入控件后的目标再次拖动到控件之外，就会触发dragLeaveEvent()事件
        print('Drag Leave')

    def dropEvent(self, QDropEvent):                                # 将目标在QTextBrowser中放下后触发
        print('Drag Drop')
        # Windows
        # 通过QDropEvent.mimeData().text()方法获取到该文件的URI路径
        # replace()方法将其中的file:///替换为/，这样得到的值才是我们想要的本地文件路径
        txt_path = QDropEvent.mimeData().text().replace('file:///', '')
        with open(txt_path, 'r') as f:      # 打开my.txt文件进行读取
            self.setText(f.read())               # 用setText()方法将QTextBrowser的文本设为该my.txt的内容

        # MacOS
        # txt_path = QDropEvent.mimeData().text().replace('file:///', '/')

        # Linux
        # txt_path = QDropEvent.mimeData().text().replace('file:///', '/').strip()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())