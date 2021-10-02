import sys
from PyQt5.QtCore import QDir
from PyQt5.QtWidgets import QApplication, QWidget, QTreeView, QDirModel, QLabel, QVBoxLayout

# PyQt5中所提供的模型种类及用处：
# QStringListModel                  存储一个字符串列表
# QStandardItemModel         存储任意的分层次的数据
# QDirModel                             封装本地文件系统
# QSqlQueryModel                  封装一个SQL结果集
# QSqlTableModel                   封装一个SQL表
# QSqlRelationTableModel    利用外键封装一个SQL表
# QSortFilterProxyModel        对模型数据进行排序或过滤

# 此程序使用了QDirModel模型：封装本地文件系统
class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.resize(600, 300)
        self.model = QDirModel(self)                                                           # 实例化一个QDirModel
        self.model.setReadOnly(False)                                                        # setReadOnly(False)在QTreeView中直接对文件编辑，若设为True，则只读模式
        self.model.setSorting(QDir.Name | QDir.IgnoreCase)                # setSorting()让显示的文件或文件夹按照指定要求进行排序
        # setSorting可传入的参数:
        # QDir.Name             按照名称排序
        # QDir.Time               按照修改时间排序
        # QDir.Size                 按照文件大小类型排序
        # QDir.Type               按照文件类型排序
        # QDir.Unsorted       无排序
        # QDir.NoSort           不排序
        # QDir.DirsFirst         将文件夹置于文件前
        # QDir.DirsLast          将文件置于文件夹前
        # QDir.Reversed        反向排序
        # QDir.IgnoreCase     无视大小写排序
        # QDir.LocaleAware  按照本地设置进行排序

        self.tree = QTreeView(self)                                                                # 实例化一个树形视图
        self.tree.setModel(self.model)                                                         # 将其模型设为self.model
        self.tree.clicked.connect(self.show_info)                                       # 连接clicked信号与槽函数show_info()
        self.index = self.model.index(QDir.currentPath())                       # self.model.index()传入QDir.currentPath(),获取当前路径的QModelIndex索引值
        self.tree.expand(self.index)                                                              # self.tree.expand()方法:展开显示
        self.tree.scrollTo(self.index)                                                             # scrollTo()方法:将当前视图的视口滚动到self.index索引处

        self.info_label = QLabel(self)                                                            # 实例化一个 QLabel用于显示文件信息

        self.v_layout = QVBoxLayout()
        self.v_layout.addWidget(self.tree)
        self.v_layout.addWidget(self.info_label)
        self.setLayout(self.v_layout)

    def show_info(self):
        index = self.tree.currentIndex()                                                        # currentIndex()方法:获取当前鼠标所点击的QModelIndex索引值
        file_name = self.model.fileName(index)                                         # 将索引值传入self.model的fileName()中
        file_path = self.model.filePath(index)                                              # 将索引值传入self.model的filePath()中
        file_info = 'File Name: {}\nFile Path: {}'.format(file_name, file_path)
        self.info_label.setText(file_info)                                                      # 用info_label显示出file_info


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())