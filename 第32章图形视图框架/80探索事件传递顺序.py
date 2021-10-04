import sys
from PyQt5.QtWidgets import QApplication, QGraphicsRectItem, QGraphicsScene, QGraphicsView


class CustomItem(QGraphicsRectItem):
    def __init__(self, num):
        super(CustomItem, self).__init__()
        self.setRect(100, 30, 100, 30)
        self.num = num

    def mousePressEvent(self, event):
        print('event from QGraphicsItem{}'.format(self.num))
        super().mousePressEvent(event)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    view = QGraphicsView()
    scene = QGraphicsScene()
    item1 = CustomItem(1)
    item2 = CustomItem(2)
    item2.setParentItem(item1)
    # 调用setParentItem()方法将item1设置为item2的父类
    scene.addItem(item1)
    view.setScene(scene)

    view.show()
    sys.exit(app.exec_())
# result:
# event from QGraphicsItem2
# event from QGraphicsItem1
# 说明信号传递的顺序是：子类->父类
