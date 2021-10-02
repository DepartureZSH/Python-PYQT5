import sys
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QStringListModel
from PyQt5.QtWidgets import QApplication, QWidget, QListView, QLabel, QHBoxLayout, QAbstractItemView

# PyQt5中所提供的模型种类及用处：
# QStringListModel                  存储一个字符串列表
# QStandardItemModel         存储任意的分层次的数据
# QDirModel                             封装本地文件系统
# QSqlQueryModel                  封装一个SQL结果集
# QSqlTableModel                   封装一个SQL表
# QSqlRelationTableModel    利用外键封装一个SQL表
# QSortFilterProxyModel        对模型数据进行排序或过滤

# 此程序使用了QStringListModel模型：存储一个字符串列表
class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
######################################################################################################
        self.item_list = ['item %s' % i for i in range(11)]                            # 用列表推导式生成11个item
        self.model_1 = QStringListModel(self)                                            # 实例化一个QStringListModel
        self.model_1.setStringList(self.item_list)                                        # setStringList(iterable)将数据添加到到模型中

        self.model_2 = QStringListModel(self)                                            # model_1用于listview_1，model_2用于listview_2
######################################################################################################
        self.listview_1 = QListView(self)                                                        # 实例化一个列表视图listview_1
        self.listview_1.setModel(self.model_1)                                          # setModel(model)方法将model_1作为参数传入
        # 此时，列表视图就会显示出模型中的数据，模型数据发生任何改变，视图也会自动作出相应改变
        self.listview_1.setEditTriggers(QAbstractItemView.NoEditTriggers)  # setEditTriggers()方法可设置视图的编辑规则
        # 可传入的参数如下:
        # QAbstractItemView.NoEditTriggers      无法编辑
        # QAbstractItemView.CurrentChanged      当前选择项发生改变时可编辑
        # QAbstractItemView.DoubleClicked       双击时可编辑
        # QAbstractItemView.SelectedClicked     单击一选中的内容时可编辑
        # QAbstractItemView.EditKeyPressed      当编辑键被按下时可编辑
        # QAbstractItemView.AnyKeyPressed       按下任意键可编辑
        # QAbstractItemView.AllEditTriggers         包括以上全部触发条件
        self.listview_1.doubleClicked.connect(lambda: self.change_func(self.listview_1))    # 连接视图的doubleClicked信号与槽函数change_func()
#######################################################################################################
        self.listview_2 = QListView(self)                                                       # 实例化一个listview_2，设置模型和编辑规则并将信号和槽函数进行连接
        self.listview_2.setModel(self.model_2)
        self.listview_2.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.listview_2.doubleClicked.connect(lambda: self.change_func(self.listview_2))
########################################################################################################
        self.pic_label = QLabel(self)                                                               # pic_label用于显示图片
        self.pic_label.setPixmap(QPixmap('arrow.png'))
########################################################################################################
        self.h_layout = QHBoxLayout()
        self.h_layout.addWidget(self.listview_1)
        self.h_layout.addWidget(self.pic_label)
        self.h_layout.addWidget(self.listview_2)
        self.setLayout(self.h_layout)
########################################################################################################

    def change_func(self, listview):                                                                        # 在此函数中先判断触发doubleClicked信号的视图
        if listview == self.listview_1:                                                                          # 如果是listview_1
            self.model_2.insertRows(self.model_2.rowCount(), 1)                      # insertRows(int, int)先在model_2中插入一个空行
            # 该方法的第一个参数为行序号，即要将数据插入哪一行，第二个为要插入的行数量
            # rowCount()方法获取总行数(在这里正好可以当做行序号，表示将新行添加到最后一行)
            # 1表示我们在每次双击时都只插入一行

            data = self.listview_1.currentIndex().data()                              # currentIndex().data()方法可以获取到被双击行的数据
            index = self.model_2.index(self.model_2.rowCount()-1)       # QStringListModel.index(int)获取指定的QModelIndex，传入的参数为行序号
            self.model_2.setData(index, data)                                              # 由于插入的空行，所以要setData(QModelindex, data)将空行设为相应内容
        else:                                                                                                        # 如果是listview_2触发doubleClicked信号
            self.model_2.removeRows(self.listview_2.currentIndex().row(), 1)
            # 调用removeRows(int, int)，方法将被双击的行给删除掉
            # currentIndex().row()方法获取被双击行的行序号,1表示我们只删除一行
########################################################################################################
if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())