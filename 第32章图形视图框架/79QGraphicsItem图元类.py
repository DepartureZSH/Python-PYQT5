import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QColor, QPainterPath
from PyQt5.QtWidgets import QApplication, QGraphicsItem, QGraphicsLineItem, QGraphicsRectItem,\
                QGraphicsEllipseItem, QGraphicsPixmapItem, QGraphicsTextItem, QGraphicsPathItem, \
                QGraphicsScene, QGraphicsView

# PyQt5中的图形视图可以让我们管理大量的自定义2D图元并与之交互。
# 该框架使用BSP（Binary Space Partitioning - 二叉空间分割）树，以快速查找图形元素。
# 所以就算一个视图场景中包含数百万的图元，它也可以实时进行显示。
# 如果要用PyQt5来制作稍微复杂点的游戏的话，图形视图是必定要用到的

# 图形视图框架主要包含三个类：
# QGraphicsItem图元类、QGraphicsScene场景类和QGraphicsView视图类。
# 简单一句话来概括下三者的关系就是：图元放在场景上，场景内容通过视图来显示
# 图元->场景，场景内容->视图显示

# 图元类
# 直线图元QGraphicsLineItem
# 矩形图元QGraphicsRectItem
# 椭圆图元QGraphicsEllipseItem
# 图片图元QGraphicsPixmapItem
# 文本图元QGraphicsTextItem
# 路径图元QGraphicsPathItem

class Demo(QGraphicsView):
    def __init__(self):
        super(Demo, self).__init__()

        # 该类直接继承QGraphicsView，那么窗口就是视图，且大小为300x300
        self.resize(300, 300)

        # 实例化一个QGraphicsScene场景
        # 调用setSceneRect(x, y, w, h)方法来设置场景坐标原点和大小
        self.scene = QGraphicsScene()
        self.scene.setSceneRect(0, 0, 300, 300)
        # 坐标原点为(0, 0)，之后往场景中添加的图元就会都根据该坐标来设置位置
        # 场景的大小为300x300，跟视图大小一样
# 图元
        # 实例化一个QGraphicsLineItem直线图元
        # 调用setLine()方法设置直线两端的坐标
        # 1、setLine(x1, y1, x2, y2)
        # 2、setLine(const QLineF &line)
        self.line = QGraphicsLineItem()
        self.line.setLine(100, 10, 200, 10)
        # self.line.setLine(QLineF(100, 10, 200, 10))

        # 实例化矩形图元
        # 调用相应的方法来设置位置和大小
        self.rect = QGraphicsRectItem()
        self.rect.setRect(100, 30, 100, 30)
        # self.rect.setRect(QRectF(100, 30, 100, 30))

        # 实例化椭圆图元
        # 调用相应的方法来设置位置和大小
        self.ellipse = QGraphicsEllipseItem()
        self.ellipse.setRect(100, 80, 100, 20)
        # self.ellipse.setRect(QRectF(100, 80, 100, 20))

        # 实例化一个图片图元
        # 调用setPixmap()方法设置图片，QPixmap.scaled()方法可以设置图片的大小
        # 当然我们也可以使用QGraphicsItem的setScale()方法来设置
        # 接着我们设置该图元的Flag属性，让他可以被选中以及移动，这是所有图元共有的方法(见帮助文档)。
        # 最后调用setOffset()方法来设置图片相对于场景坐标原点的偏移量
        self.pic = QGraphicsPixmapItem()
        self.pic.setPixmap(QPixmap('pic.png').scaled(60, 60))
        self.pic.setFlags(QGraphicsItem.ItemIsSelectable | QGraphicsItem.ItemIsMovable)
        self.pic.setOffset(100, 120)
        # self.pic.setOffset(QPointF(100, 120))

        # 实例化了三个文本图元，分别显示普通绿色文本，可编辑文本以及超链接文本(HTML)
        # setDefaultColor()方法可以用来设置文本的颜色
        # setPos()用来设置文本图元相对于场景坐标原点的位置(该方法是所有图元共有的方法)
        self.text1 = QGraphicsTextItem()
        self.text1.setPlainText('Hello PyQt5')
        self.text1.setDefaultTextColor(QColor(66, 222, 88))
        self.text1.setPos(100, 180)

        self.text2 = QGraphicsTextItem()
        self.text2.setPlainText('Hello World')

        # setTextInteractionFlags()用来设置文本属性
        # Qt.TextEditorInteraction参数表示为可编辑属性(相当于在QTextEdit上编辑文本)
        self.text2.setTextInteractionFlags(Qt.TextEditorInteraction)
        self.text2.setPos(100, 200)

        self.text3 = QGraphicsTextItem()
        self.text3.setHtml('<a href="https://baidu.com">百度</a>')
        # 使超链接文本能够被打开
        self.text3.setOpenExternalLinks(True)
        # Qt.TextBrowserInteraction表明该文本用于浏览(相当于在QTextBrowser上的文本)
        self.text3.setTextInteractionFlags(Qt.TextBrowserInteraction)
        self.text3.setPos(100, 220)

        # 路径图元可以用于显示任意形状的图形，
        # setPath()方法需要传入一个QPainterPath对象，而我们就是用该对象来进行绘画操作的。
        # moveTo()方法表示将画笔移动到相应位置上
        # lineTo()表示画一条直线，closeSubpath()方法表示当前作画结束
        # (查阅文档来了解更多有关QPaintPath对象的方法)
        # 这里我们画了一个直角三角形
        self.path = QGraphicsPathItem()

        self.tri_path = QPainterPath()
        self.tri_path.moveTo(100, 250)
        self.tri_path.lineTo(130, 290)
        self.tri_path.lineTo(100, 290)
        self.tri_path.lineTo(100, 250)
        self.tri_path.closeSubpath()

        self.path.setPath(self.tri_path)
# 场景
        # 调用场景的addItem()方法将所有图元添加进来
        self.scene.addItem(self.line)
        self.scene.addItem(self.rect)
        self.scene.addItem(self.ellipse)
        self.scene.addItem(self.pic)
        self.scene.addItem(self.text1)
        self.scene.addItem(self.text2)
        self.scene.addItem(self.text3)
        self.scene.addItem(self.path)
# 视图（类本身）
        # 调用setScene()方法来让场景居中显示在视图中
        self.setScene(self.scene)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
