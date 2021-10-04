import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPen, QBrush
from PyQt5.QtWidgets import QApplication, QGraphicsItem, QGraphicsRectItem, QGraphicsEllipseItem, QGraphicsScene, \
                            QGraphicsView, QGraphicsItemGroup


class Demo(QGraphicsView):
    def __init__(self):
        super(Demo, self).__init__()
        self.resize(300, 300)

        self.scene = QGraphicsScene()
        self.scene.setSceneRect(0, 0, 300, 300)

        # 实例化四个图元，两个为矩形，两个为椭圆
        self.rect1 = QGraphicsRectItem()
        self.rect2 = QGraphicsRectItem()
        self.ellipse1 = QGraphicsEllipseItem()
        self.ellipse2 = QGraphicsEllipseItem()
        # 调用setRect()方法设置坐标和大小
        self.rect1.setRect(100, 30, 100, 30)
        self.rect2.setRect(100, 80, 100, 30)
        self.ellipse1.setRect(100, 140, 100, 20)
        self.ellipse2.setRect(100, 180, 100, 50)

        # 实例化两种画笔和两种画刷
        pen1 = QPen(Qt.SolidLine)
        pen1.setColor(Qt.blue)
        pen1.setWidth(3)
        pen2 = QPen(Qt.DashLine)
        pen2.setColor(Qt.red)
        pen2.setWidth(2)
        brush1 = QBrush(Qt.SolidPattern)
        brush1.setColor(Qt.blue)
        brush2 = QBrush(Qt.SolidPattern)
        brush2.setColor(Qt.red)
        # 设置图元的画笔\笔刷样式
        self.rect1.setPen(pen1)
        self.rect1.setBrush(brush1)
        self.rect2.setPen(pen2)
        self.rect2.setBrush(brush2)
        self.ellipse1.setPen(pen1)
        self.ellipse1.setBrush(brush1)
        self.ellipse2.setPen(pen2)
        self.ellipse2.setBrush(brush2)

        # 实例化两个QGraphicsGroup分组对象，并将矩形和椭圆都添加进来
        self.group1 = QGraphicsItemGroup()
        self.group2 = QGraphicsItemGroup()
        # rect1和ellipse1在group1里，而rect2和ellipse2在group2里
        self.group1.addToGroup(self.rect1)
        self.group1.addToGroup(self.ellipse1)
        self.group2.addToGroup(self.rect2)
        self.group2.addToGroup(self.ellipse2)
        # 调用setFlags()方法设置属性，让分组可以选中和移动
        self.group1.setFlags(QGraphicsItem.ItemIsSelectable | QGraphicsItem.ItemIsMovable)
        self.group2.setFlags(QGraphicsItem.ItemIsSelectable | QGraphicsItem.ItemIsMovable)
        # boundRect()方法放回一个QRectF值，该值可以显示出分组的边界位置和大小
        print(self.group1.boundingRect())
        print(self.group2.boundingRect())

        # 将分组添加到场景当中
        self.scene.addItem(self.group1)
        self.scene.addItem(self.group2)

        self.setScene(self.scene)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
