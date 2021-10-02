import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QTableWidget, QTableWidgetItem


class Demo(QTableWidget):                                                                      # 直接继承QTableWidget来实现程序
    def __init__(self):
        super(Demo, self).__init__()
        self.setRowCount(6)                                                                           # setRowCount(int)设置表格的行数
        self.setColumnCount(6)                                                                     # setColumnCount(int)设置列数
        # self.table = QTableWidget(6, 6, self)                                            # 或者在实例化的时候直接指定行列数

        print(self.rowCount())                                                                        # rowCount()获取行数
        print(self.columnCount())                                                                 # columnCount()获取列数

        self.setColumnWidth(0, 30)                                                              # setColumnWidth(int, int)设置列宽，参数分别是列序号、宽度值
        self.setRowHeight(0, 30)                                                                   # setRowHeight(int, int)设置行宽，参数分别是行序号、宽度值

        self.setHorizontalHeaderLabels(['h1', 'h2', 'h3', 'h4', ' h5', 'h6'])   # setHorizontalHeaderLabels(iterable)设置行的标题
        self.setVerticalHeaderLabels(['t1', 't2', 't3', 't4', 't5', 't6'])               # setVerticalHeaderLabels(iterable)设置列的标题

        # self.setShowGrid(False)                                           # setShowGird(bool)设置是否显示表格上的网格线，True为显示，False不显示

        self.item_1 = QTableWidgetItem('Hi')            # 实例化一个单元格,内容为Hi
        self.setItem(0, 0, self.item_1)                           # setItem(int, int, QTableWidgetItem)将单元格添加到表格,int参数分别为行序号和列序号

        self.item_2 = QTableWidgetItem('Bye')
        self.item_2.setTextAlignment(Qt.AlignCenter)                             # setTextAlignment()设置单元格的文本对齐方式

        # 水平标志：
        # Qt::AlignLeft     与左边缘对齐。
        # Qt::AlignRight    与右边缘对齐。
        # Qt::AlignHCenter  在可用空间中水平居中。
        # Qt::AlignJustify  在可用空间中对齐文本。
        # 垂直标志：
        # Qt::AlignTop  与顶部对齐。
        # Qt::AlignBottom   与底部对齐。
        # Qt::AlignVCenter  在可用空间中垂直居中
        # Qt::AlignBaseline 与基线对齐
        # 二维标志：
        # Qt::AlignCenter   在两个维度(水平、垂直)的中心居中
        # 一次最多可以使用一个水平和一个垂直标志

        self.setItem(2, 2, self.item_2)

        self.setSpan(2, 2, 2, 2)
        # setSpan(int, int, int, int)方法用来合并单元格，参数分别为行序号、列序号和要合并的行数和列数(合并成的矩形的长宽)

        print(self.findItems('Hi', Qt.MatchExactly))
        # findItems(str, Qt.MatchFlag)用来查找，str为用来匹配的字符串，后一个参数为匹配方式
        # Qt.MatchExactly   表示精确匹配
        print(self.findItems('B', Qt.MatchContains))
        # Qt.MatchContains  表示包含匹配
        # Qt.MatchFixedString  执行基于字符串的匹配。除非还指定了MatchCaseSensitive标志，否则基于字符串的比较不区分大小写。
        # Qt.MatchStartsWith 搜索词与字符串的开头匹配。
        # Qt.MatchEndsWith 搜索项与字符串的结尾匹配。
        # Qt.MatchCaseSensitive 搜索区分大小写。
        # Qt.MatchRegExp 使用正则表达式作为搜索词执行基于字符串的匹配。
        # Qt.MatchWildcard 使用带有通配符的字符串作为搜索词执行基于字符串的匹配。
        # Qt.MatchWrap
        # 执行环绕的搜索，在搜索到达模型中的最后一个项目时，从第一个项目再次开始搜索，并继续搜索，直到检查完所有项目。
        # Qt.MatchRecursive 搜索整个层次结构。

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())