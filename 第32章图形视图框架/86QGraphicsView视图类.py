import sys
from PyQt5.QtCore import QRectF
from PyQt5.QtWidgets import QApplication, QGraphicsScene, QGraphicsView


class Demo(QGraphicsView):
    def __init__(self):
        super(Demo, self).__init__()
        self.resize(300, 300)

        self.scene = QGraphicsScene()
        self.scene.setSceneRect(0, 0, 500, 500)
        self.scene.addEllipse(QRectF(200, 200, 50, 50))

        self.setScene(self.scene)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
