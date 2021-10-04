import sys
from PyQt5.QtWidgets import QApplication, QGraphicsRectItem, QGraphicsScene, QGraphicsView

# 矩形图元被鼠标点中释放
class CustomItem(QGraphicsRectItem):
    def __init__(self):
        super(CustomItem, self).__init__()
        self.setRect(100, 30, 100, 30)

    def mousePressEvent(self, event):
        print('event from QGraphicsItem')
        super().mousePressEvent(event)
        # super()调用父类(QGraphicsRectItem)的mousePressEvent函数

# 场景被鼠标点中释放
class CustomScene(QGraphicsScene):
    def __init__(self):
        super(CustomScene, self).__init__()
        self.setSceneRect(0, 0, 300, 300)

    def mousePressEvent(self, event):
        print('event from QGraphicsScene')
        super().mousePressEvent(event)
        # super()调用父类(QGraphicsScene)的mousePressEvent函数

# 视图被鼠标点中释放
class CustomView(QGraphicsView):
    def __init__(self):
        super(CustomView, self).__init__()
        self.resize(300, 300)

    def mousePressEvent(self, event):
        print('event from QGraphicsView')
        super().mousePressEvent(event)
        # super()调用父类(QGraphicsView)的mousePressEvent函数

# 注意：当点击矩形图元时
# event from QGraphicsView
# event from QGraphicsScene
# event from QGraphicsItem
# 说明事件的传递顺序为视图（孙）->场景（儿）->图元（父）

if __name__ == '__main__':
    app = QApplication(sys.argv)
    view = CustomView()
    scene = CustomScene()
    item = CustomItem()

    scene.addItem(item)
    view.setScene(scene)

    view.show()
    sys.exit(app.exec_())
