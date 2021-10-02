import sys
from PyQt5.QtWidgets import QApplication, QWidget
# x()——得到窗口左上角在显示屏屏幕上的x坐标
# y()——得到窗口左上角在显示屏屏幕上的y坐标
# pos()——得到窗口左上角在显示屏屏幕上的x和y坐标，类型为QPoint()
# geometry().x()——的到客户区左上角在显示屏屏幕上的x坐标
# geometry().y()——的到客户区左上角在显示屏屏幕上的y坐标
# geometry()——的到客户区左上角在显示屏屏幕上的x和y坐标，以及客户区的宽度和长度，类型为QRect()
# width()——得到客户区的宽度
# height()——得到客户区的长度
# geometry().width()——得到客户区的宽度
# geometry().height()——得到客户区的长度
# frameGeometry().width()——得到窗口的宽度
# frameGeometry().height()——得到窗口的长度
# frameGeometry().x()——即x()，得到窗口左上角在显示屏屏幕上的x坐标
# frameGeometry().y()——即y()，得到窗口左上角在显示屏屏幕上的y坐标
# frameGeometry()——即pos()，得到窗口左上角在显示屏屏幕上的x和y坐标，以及窗口的宽度和长度，类型为QRect()
# 注：通过geometry()和frameGeometry()获取坐标的相关方法需要在窗口调用show()方法之后才能使用，否则获取的将是无用数据。

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = QWidget()
    widget.resize(200, 200)                                       # 通过resize(200, 200)方法来设置窗口大小
    widget.move(100, 100)                                       # 通过move(100, 100)方法将窗口移到屏幕坐标为(100, 100)的位置上
    # widget.setGeometry(100, 100, 200, 200)     # 以上两个方法可以单单通过setGeometry(x, y, width, height)方法来完成
    widget.show()

    print('-----------------x(), y(), pos()-----------------')
    print(widget.x())
    print(widget.y())
    print(widget.pos())

    print('-----------------width(), height()-----------------')
    print(widget.width())
    print(widget.height())

    print('-----------------geometry().x(), geometry.y(), geometry()-----------------')
    print(widget.geometry().x())
    print(widget.geometry().y())
    print(widget.geometry())

    print('-----------------geometry.width(), geometry().height()-----------------')
    print(widget.geometry().width())
    print(widget.geometry().height())

    print('-----------------frameGeometry().x(), frameGeometry().y(), frameGeometry(), '
          'frameGeometry().width(), frameGeometry().height()-----------------')
    print(widget.frameGeometry().x())
    print(widget.frameGeometry().y())
    print(widget.frameGeometry())
    print(widget.frameGeometry().width())
    print(widget.frameGeometry().height())

    sys.exit(app.exec_())