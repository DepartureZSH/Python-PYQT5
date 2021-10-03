import sys
from PyQt5.QtCore import Qt
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel
from PyQt5.QtWidgets import QApplication, QMessageBox, QTableView


class Demo(QTableView):
    def __init__(self):
        super(Demo, self).__init__()
        self.resize(600, 200)
        self.db = None
        self.db_connect()
        self.sql_exec()

    def db_connect(self):
        self.db = QSqlDatabase.addDatabase('QMYSQL')
        self.db.setHostName('localhost')
        self.db.setDatabaseName('test_db')
        self.db.setUserName('root')
        self.db.setPassword('15828030238')
        if not self.db.open():
            QMessageBox.critical(self, 'Database Connection', self.db.lastError().text())

    def closeEvent(self, QCloseEvent):
        self.db.close()

    def sql_exec(self):
        model = QSqlTableModel()  # 实例化一个QSqlTableModel模型，
        model.setTable('students')  # 调用setTable()来选择要进行操作的数据表
        model.setEditStrategy(QSqlTableModel.OnFieldChange)
        # 调用setEditStrategy设置模型编辑策略
        # QSqlTableModel.OnFieldChange       0       所有变更立即更新到数据库中
        # QSqlTableModel.OnRowChange        1       当用户对某行数据操作后，点击其他行时再更新数据库
        # QSqlTableModel.OnManualSubmit   2       只有在调用SubmitAll()或者revertAll()后才会更新数据库
        model.setHeaderData(0, Qt.Horizontal, 'ID')
        model.setHeaderData(1, Qt.Horizontal, 'Class')
        model.setHeaderData(2, Qt.Horizontal, 'Name')
        model.setHeaderData(3, Qt.Horizontal, 'Score')
        model.select()

        self.setModel(model)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
