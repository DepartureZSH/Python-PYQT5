import sys
from PyQt5.QtCore import QPropertyAnimation, QPointF, QRectF, pyqtSignal
from PyQt5.QtWidgets import QApplication, QGraphicsScene, QGraphicsView, QGraphicsObject

# 出于性能考虑，QGraphicsItem不继承自QObject，
# 不继承自QObject，所以本身并不能使用信号和槽机制，也无法给它添加动画。
# 不过我们可以自定义一个类，并让该类继承自QGraphicsObject。
class CustomRect(QGraphicsObject):
    # 自定义一个信号
    my_signal = pyqtSignal()

    def __init__(self):
        super(CustomRect, self).__init__()

    # 把boundingRect()和paint()方法重新实现
    def boundingRect(self):
        return QRectF(0, 0, 100, 30)            # 返回一个QRectF类型值来确定CustomRect的默认位置和大小

    def paint(self, painter, styles, widget=None):
        painter.drawRect(self.boundingRect())   # 调用drawRect()方法将矩形画到界面上

class Demo(QGraphicsView):
    def __init__(self):
        super(Demo, self).__init__()
        self.resize(300, 300)

        # 将自定义的信号和槽函数连接，槽函数中打印“signal and slot”字符串。
        # 接着调用信号的emit()方法来发射信号，那么槽函数也就会启动了
        self.rect = CustomRect()
        self.rect.my_signal.connect(lambda: print('signal and slot'))
        self.rect.my_signal.emit()

        self.scene = QGraphicsScene()
        self.scene.setSceneRect(0, 0, 300, 300)
        self.scene.addItem(self.rect)

        self.setScene(self.scene)

        # 加上QPropertyAnimation属性动画
        self.animation = QPropertyAnimation(self.rect, b'pos')
        # 时间为3秒
        self.animation.setDuration(3000)
        # 将矩形从(100, 30)移动到(100, 200)
        self.animation.setStartValue(QPointF(100, 30))
        self.animation.setEndValue(QPointF(100, 200))
        # 动画无限循环
        self.animation.setLoopCount(-1)
        self.animation.start()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
