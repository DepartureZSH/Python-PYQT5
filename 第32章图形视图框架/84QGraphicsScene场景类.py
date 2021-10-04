import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QTransform
from PyQt5.QtWidgets import QApplication, QGraphicsItem, QGraphicsScene, QGraphicsView


class Demo(QGraphicsView):
    def __init__(self):
        super(Demo, self).__init__()
        self.resize(300, 300)

        self.scene = QGraphicsScene()
        self.scene.setSceneRect(0, 0, 300, 300)

        # 直接调用场景的addRect(), addEllipse()和addPixmap()方法来添加图元
        # 先添加的图元处于后添加的图元上方(Z轴方向)
        self.rect = self.scene.addRect(100, 30, 100, 30)
        self.ellipse = self.scene.addEllipse(100, 80, 50, 40)
        self.pic = self.scene.addPixmap(QPixmap('pic1.png').scaled(60, 60))
        self.pic.setOffset(100, 130)
        # 可以通过调用图元的setZValue()方法来改变上下位置

        # 设置图元的Flag属性。这里ItemIsFocusable表示让图元可以聚焦(默认是无法聚焦的)
        self.rect.setFlags(QGraphicsItem.ItemIsSelectable | QGraphicsItem.ItemIsMovable | QGraphicsItem.ItemIsFocusable)
        self.ellipse.setFlags(QGraphicsItem.ItemIsSelectable | QGraphicsItem.ItemIsMovable | QGraphicsItem.ItemIsFocusable)
        self.pic.setFlags(QGraphicsItem.ItemIsSelectable | QGraphicsItem.ItemIsMovable | QGraphicsItem.ItemIsFocusable)

        self.setScene(self.scene)

        # 调用items()方法可以返回场景中的所有图元，返回值类型为列表
        print(self.scene.items())       # 默认顺序从下到上
        print(self.scene.items(order=Qt.AscendingOrder))    # 设置顺序从上到下
        # itemsBoundingRect()返回所有图元所构成的整体的边界
        print(self.scene.itemsBoundingRect())
        # itemAt()可以返回指定位置上的图元，如果在这个位置上有两个重叠的图元的话，那就返回最上面的图元
        print(self.scene.itemAt(110, 40, QTransform()))

        # 场景有个focusChangedItem信号，当我们选中不同的图元时发出，
        # 前提是图元设置了ItemIsFocusable属性
        # 该信号传递两个值，第一个是新选中的图元，第二个是之前选中的图元
        self.scene.focusItemChanged.connect(self.my_slot)

    def my_slot(self, new_item, old_item):
        print('new item: {}\nold item: {}'.format(new_item, old_item))

    # 调用场景的collidingItems()打印出在指定碰撞触发条件下，所有和目标图元发生碰撞的其他图元
    def mouseMoveEvent(self, event):
        print(self.scene.collidingItems(self.ellipse, Qt.IntersectsItemShape))
        super().mouseMoveEvent(event)

    # 双击删除图元，还需要修改，因为event.pos()是鼠标在视图上的坐标，而不是场景上的坐标
    def mouseDoubleClickEvent(self, event):
        item = self.scene.itemAt(event.pos(), QTransform())
        self.scene.removeItem(item)
        super().mouseDoubleClickEvent(event)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
