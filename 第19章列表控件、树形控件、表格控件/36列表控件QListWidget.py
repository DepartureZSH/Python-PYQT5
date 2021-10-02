import sys
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QListWidget, QListWidgetItem, QHBoxLayout


class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.pic_label = QLabel(self)                                                               # 实例化一个QLabel用于显示图片
        self.pic_label.setPixmap(QPixmap('arrow.png'))

        self.listwidget_1 = QListWidget(self)                                                # 实例化一个QListWidget控件listwidget_1放在左边用于显示可选的内容
        self.listwidget_2 = QListWidget(self)                                                # 实例化一个QListWidget控件listwidget_2放在右边用于显示可选的内容
        self.listwidget_1.doubleClicked.connect(lambda: self.change_func(self.listwidget_1))    # 连接doubleClicked信号和自定义的槽函数
        self.listwidget_2.doubleClicked.connect(lambda: self.change_func(self.listwidget_2))    # 每次双击QListWidget控件触发change_func

        for i in range(6):                                                                                   # 循环创建六个QListWidgetItem
            text = 'Item {}'.format(i)
            self.item = QListWidgetItem(text)
            self.listwidget_1.addItem(self.item)                                            # 调用addItem(QListWidgetItem)将其添加到listwidget_1中

        self.item_6 = QListWidgetItem('Item 6', self.listwidget_1)          # 也可以通过实例化时直接指定父类的方式进行添加

        self.listwidget_1.addItem('Item 7')                                                  # 也可以不用QListWidgetItem，直接调用addItem(str)方法来添加一项内容
        str_list = ['Item 9', 'Item 10']
        self.listwidget_1.addItems(str_list)                                                  # 也可以使用addItem(Iterable)来添加一组项内容
        # (不过若要让项呈现更多功能的话，还是应该选择QListWidgetItem)

        self.item_8 = QListWidgetItem('Item 8')
        self.listwidget_1.insertItem(8, self.item_8)                                    # 通过insertItem(row, QListWidgetItem)方法可以在指定行中加入一项内容
        # self.listwidget_1.insertItem(8, 'Item 8')

        self.h_layout = QHBoxLayout()
        self.h_layout.addWidget(self.listwidget_1)
        self.h_layout.addWidget(self.pic_label)
        self.h_layout.addWidget(self.listwidget_2)
        self.setLayout(self.h_layout)

    def change_func(self, listwidget):
        if listwidget == self.listwidget_1:                                                       # 判断信号是listwidget_1
            item = QListWidgetItem(self.listwidget_1.currentItem())        # 通过currentItem()获取到当前被双击的项，实例化为QListWidgetItem
            self.listwidget_2.addItem(item)                                                    # 通过addItem(QListWidgetItem)方法加入listwidget_2中
            print(self.listwidget_2.count())                                                     # count()用于获取项数量，打印出listwidget_2中一共有多少项内容
        else:
            self.listwidget_2.takeItem(self.listwidget_2.currentRow())    # currentRow()获取到当前被双击的行数，takeItem(int)来进行删除
            print(self.listwidget_2.count())                                                     #打印出listwidget_2中一共有多少项内容

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())