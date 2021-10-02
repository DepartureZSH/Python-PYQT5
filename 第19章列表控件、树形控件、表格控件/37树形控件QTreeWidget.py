import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QTreeWidget, QTreeWidgetItem, QLabel, QHBoxLayout

class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.resize(500, 300)
        self.label = QLabel('No Click')                                                            # QLabel控件用于显示每个QTreeWidgetItem的文本

        self.tree = QTreeWidget(self)                                                            # 实例化一个QTreeWidget
        self.tree.setColumnCount(2)                                                             # setColumnCount(int)将该树状控件的列数设为2(默认为1列)
        self.tree.setHeaderLabels(['Install Components', 'Test'])            # setHeaderLabels(Iterable)设置每列的标题
        # 如果只有一列的话，则应该通过setHeaderLabel(str)方法设置
        self.tree.itemClicked.connect(self.change_func)                          # 连接itemClicked信号(QTreeWidget中的任意一项被点击)与槽函数
        # 这是一个带参数的信号
        # 当该信号被触发时，参数item保存被点击的项，column保存列数，而这两个参数会自动传给槽函数

        self.preview = QTreeWidgetItem(self.tree)                                   # 实例化一个QTreeWidgetItem，并将其父类设为self.tree
        # 表示self.preview为最外层(最顶层)的项
        self.preview.setText(0, 'Preview')                                                    # setText(int, str)设置文本，int参数为该文本所在的列，0即第一列

        # self.preview = QTreeWidgetItem()                                               # 也可以在实例化时不指定父类
        # self.preview.setText(0, 'Preview')
        # self.tree.addTopLevelItem(self.preview)                                    # 让self.tree调用addTopLevelItem()来设置最顶层的项

        self.qt5112 = QTreeWidgetItem()
        self.qt5112.setText(0, 'Qt 5.11.2 snapshot')
        self.qt5112.setCheckState(0, Qt.Unchecked)                                 # setCheckState(int, CheckState)方法可以让该项以复选框形式呈现出来
        self.preview.addChild(self.qt5112)                                                  # addChild(QTreeWidgetItem)方法可以添加子项
        # 这里让self.preview添加一个self.qt5112选项

        choice_list = ['macOS', 'Android x86', 'Android ARMv7', 'Sources', 'iOS']
        self.item_list = []
        for i, c in enumerate(choice_list):                                                     # 实例化5个子项，将他们添加到self.qt5112中，并以复选框形式显示
            # enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标
            item = QTreeWidgetItem(self.qt5112)
            item.setText(0, c)
            item.setCheckState(0, Qt.Unchecked)
            self.item_list.append(item)

        self.test_item = QTreeWidgetItem(self.qt5112)                           # self.test项只是拿来作为对比，看看将QTreeWidget设为两列时的样子
        self.test_item.setText(0, 'test1')
        self.test_item.setText(1, 'test2')

        self.tree.expandAll()                                                                           # expandAll()可以让QTreeWidget所有的项都是以打开状态显示
        # 必须要在所有项都已经实例化好之后再调用该方法

        self.h_layout = QHBoxLayout()
        self.h_layout.addWidget(self.tree)
        self.h_layout.addWidget(self.label)
        self.setLayout(self.h_layout)

    def change_func(self, item, column):                                                  # self.label显示对应的项文本，item就是被点击的项
        self.label.setText(item.text(column))                                              # 调用text(int)传入列数，获得文本

        print(item.text(column))
        print(column)
        if item == self.qt5112:                                                                         # 如果被点击的项为qt5112，则我们判断是否其被选中
            if self.qt5112.checkState(0) == Qt.Checked:                               # 若是的话，将它的所有子项都设为选中状态
                [x.setCheckState(0, Qt.Checked) for x in self.item_list]
            else:                                                                                                    # 若为无选中状态的话，则将其子项全部设为无选中状态
                [x.setCheckState(0, Qt.Unchecked) for x in self.item_list]
        else:                                                                                                        # 若被点击是qt5112的子项时，我们判断有多少个子项已经被选中了
            check_count = 0
            for x in self.item_list:
                if x.checkState(0) == Qt.Checked:
                    check_count += 1

            if check_count == 5:                                                                        # 若数量为5，则设置qt5112为选中状态
                self.qt5112.setCheckState(0, Qt.Checked)
            elif 0 < check_count < 5:                                                                 # 若为0-5之间，则设为半选中状态
                self.qt5112.setCheckState(0, Qt.PartiallyChecked)
            else:                                                                                                    # 若等于0，则设为无选中状态
                self.qt5112.setCheckState(0, Qt.Unchecked)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())