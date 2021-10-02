import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QStandardItem, QStandardItemModel
from PyQt5.QtWidgets import QApplication, QWidget, QTableView, QAbstractItemView, QLabel, QVBoxLayout

# PyQt5中所提供的模型种类及用处：
# QStringListModel                  存储一个字符串列表
# QStandardItemModel         存储任意的分层次的数据
# QDirModel                             封装本地文件系统
# QSqlQueryModel                  封装一个SQL结果集
# QSqlTableModel                   封装一个SQL表
# QSqlRelationTableModel    利用外键封装一个SQL表
# QSortFilterProxyModel        对模型数据进行排序或过滤

# 此程序使用了QStandardItemModel模型：存储任意的分层次的数据
class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.resize(650, 300)

        self.model = QStandardItemModel(6, 6, self)                                # 实例化一个QStandItemModel，传入行数和列数
        # self.model = QStandardItemModel(self)                                     # 通过setRowCount()和setColumn()方法来设置行数和列数
        # self.model.setColumnCount(6)
        # self.model.setRowCount(6)

        for row in range(6):
            for column in range(6):
                item = QStandardItem('({}, {})'.format(row, column))         # 循环实例化36个QStandardItem(每一个item代表一个单元格)
                self.model.setItem(row, column, item)                                  # setItem()方法将每一个Item放在相应的位置

        self.item_list = [QStandardItem('(6, {})'.format(column)) for column in range(6)]
        self.model.appendRow(self.item_list)                                            # appendRow()方法:把新行添加到表格最后，也就是说目前有7行

        self.item_list = [QStandardItem('(7, {})'.format(column)) for column in range(6)]
        self.model.insertRow(7, self.item_list)                                           # insertRow()方法:在指定方法添加一行，这里在最后一行插入一行，现在有8行

        self.table = QTableView(self)                                                            # 实例化一个QTableView
        self.table.setModel(self.model)                                                       # 设置模型
        self.table.horizontalHeader().setStretchLastSection(True)        # self.table.horizontalHeader().setStretchLastSection(True)可以让表格填满整个窗口
        # 如果拉伸窗口的话则为了填满窗口表格最后列会改变尺寸
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)  # setEditTriggers()方法设置编辑规则，这里我们设置无法编辑
        self.table.clicked.connect(self.show_info)                                     # 连接clicked信号与槽函数show_info

        self.info_label = QLabel(self)                                                            # info_label用于显示单元格文本
        self.info_label.setAlignment(Qt.AlignCenter)

        self.v_layout = QVBoxLayout()
        self.v_layout.addWidget(self.table)
        self.v_layout.addWidget(self.info_label)
        self.setLayout(self.v_layout)

    def show_info(self):
        row = self.table.currentIndex().row()                                             # currentIndex().row():获取当前点击单元格所在的行序号
        column = self.table.currentIndex().column()                                # currentIndex().column():获取当前点击单元格所在的列序号
        print('({}, {})'.format(row, column))

        data = self.table.currentIndex().data()                                           # currentIndex().data()可以获取到当前点击单元格的文本
        self.info_label.setText(data)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())