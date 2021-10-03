import sys
import time
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import QMimeData, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QAction, QFileDialog, QMessageBox,\
                            QFontDialog, QColorDialog, QSplashScreen

class Demo(QMainWindow):
    is_saved = True                                                                                        # 判断文本是否已经保存
    is_saved_first = True                                                                               # 判断是否是第一次保存
    path = ''                                                                                                      # 文件路径

    def __init__(self):
        super(Demo, self).__init__()
        self.file_menu = self.menuBar().addMenu('File')                         # 实例化菜单栏
        self.edit_menu = self.menuBar().addMenu('Edit')
        self.help_menu = self.menuBar().addMenu('Help')

        self.file_toolbar = self.addToolBar('File')                                       # 实例化工具栏
        self.edit_toolbar = self.addToolBar('Edit')

        self.status_bar = self.statusBar()                                                      # 实例化状态栏

        # 添加各种动作
        # 可以将一个动作看作一种命令，每当用户点击某个动作时，就会触发某种命令，程序从而执行相应的命令
        self.new_action = QAction('New', self)                                           # 新建new_action
        self.open_action = QAction('Open', self)                                       # 打开open_action
        self.save_action = QAction('Save', self)                                          # 保存save_action
        self.save_as_action = QAction('Save As', self)                               # 另存为save_as_action
        self.close_action = QAction('Close', self)                                        # 关闭close_action
        self.cut_action = QAction('Cut', self)                                               # 剪切cut_action
        self.copy_action = QAction('Copy', self)                                         # 复制copy_action
        self.paste_action = QAction('Paste', self)                                       # 粘贴paste_action
        self.font_action = QAction('Font', self)                                           # 字体改变font_action
        self.color_action = QAction('Color', self)                                        # 颜色改变color_action
        self.about_action = QAction('Qt', self)                                            # 关于about_action

        self.text_edit = QTextEdit(self)                                                         # 实例化一个QTextEdit控件

        self.mime_data = QMimeData()                                                      # 实例化一共QMimeData类
        # QMimeData被用来描述可以被存储到剪贴板中，通过drag and drop机制来传输的数据
        self.clipboard = QApplication.clipboard()                                      # 实例化一个剪贴板

        self.setCentralWidget(self.text_edit)                                               # QMainWindow.setCentralWidget()将文本编辑框设置为主窗口的中央控件
        self.resize(450, 600)                                                                            # 调用resize()方法将窗口设置到合适的大小

        # 在代码量比较多的情况下，将各个对象分开来设置会让代码更加清晰
        # 如果都同时挤在__init__()中的话会显得非常混乱，也不方便日后维护
        self.menu_init()
        self.toolbar_init()
        self.status_bar_init()
        self.action_init()
        self.text_edit_int()

    def menu_init(self):                                                                                # 菜单栏初始化
        self.file_menu.addAction(self.new_action)                                   # 调用addAction()将动作添加进file_menu
        self.file_menu.addAction(self.open_action)
        self.file_menu.addAction(self.save_action)
        self.file_menu.addAction(self.save_as_action)
        self.file_menu.addSeparator()                                                         # addSeparator()方法:添加一个分割条
        self.file_menu.addAction(self.close_action)

        self.edit_menu.addAction(self.cut_action)                                   # 调用addAction()将动作添加进edit_menu
        self.edit_menu.addAction(self.copy_action)
        self.edit_menu.addAction(self.paste_action)
        self.edit_menu.addSeparator()                                                        # addSeparator()方法:添加一个分割条
        self.edit_menu.addAction(self.font_action)
        self.edit_menu.addAction(self.color_action)

        self.help_menu.addAction(self.about_action)

    def toolbar_init(self):                                                                             # 工具栏初始化
        self.file_toolbar.addAction(self.new_action)                                # 调用addAction()将动作添加进file_toolbar
        self.file_toolbar.addAction(self.open_action)
        self.file_toolbar.addAction(self.save_action)
        self.file_toolbar.addAction(self.save_as_action)

        self.edit_toolbar.addAction(self.cut_action)                                 # 调用addAction()将动作添加进edit_toolbar
        self.edit_toolbar.addAction(self.copy_action)
        self.edit_toolbar.addAction(self.paste_action)
        self.edit_toolbar.addAction(self.font_action)
        self.edit_toolbar.addAction(self.color_action)

    def status_bar_init(self):                                                                       # 状态栏初始化
        self.status_bar.showMessage('Ready to compose')                    # 调用showMessage()，传入程序打开时想要显示的状态

    def action_init(self):
        self.new_action.setIcon(QIcon('images/new.ico'))                      # 通过setIcon()方法传入QIcon参数来设置动作的图标
        self.new_action.setShortcut('Ctrl+N')                                             # setShortCut()方法用来设置快捷键的，这里将新建动作的快捷键设置为Ctrl+N
        self.new_action.setToolTip('Create a new file')                            # setToolTip()方法可以用来设置小气泡提示
        # 当鼠标停留在该动作上时，就会显示相应的提示
        # 也可以对其他对象使用该方法，比如QPushButton
        self.new_action.setStatusTip('Create a new file')                        # setStatusTip()就是设置状态栏信息
        # 当鼠标停留在该动作上时，状态栏会显示相应的信息
        self.new_action.triggered.connect(self.new_func)                     # 连接new_action的triggered信号与槽函数new_func

        self.open_action.setIcon(QIcon('images/open.ico'))  # 2
        self.open_action.setShortcut('Ctrl+O')
        self.open_action.setToolTip('Open an existing file')
        self.open_action.setStatusTip('Open an existing file')
        self.open_action.triggered.connect(self.open_file_func)

        self.save_action.setIcon(QIcon('images/save.ico'))  # 3
        self.save_action.setShortcut('Ctrl+S')
        self.save_action.setToolTip('Save the file')
        self.save_action.setStatusTip('Save the file')
        self.save_action.triggered.connect(lambda: self.save_func(self.text_edit.toHtml()))

        self.save_as_action.setIcon(QIcon('images/save_as.ico'))  # 4
        self.save_as_action.setShortcut('Ctrl+A')
        self.save_as_action.setToolTip('Save the file to a specified location')
        self.save_as_action.setStatusTip('Save the file to a specified location')
        self.save_as_action.triggered.connect(lambda: self.save_as_func(self.text_edit.toHtml()))

        self.close_action.setIcon(QIcon('images/close.ico'))  # 5
        self.close_action.setShortcut('Ctrl+E')
        self.close_action.setToolTip('Close the window')
        self.close_action.setStatusTip('Close the window')
        self.close_action.triggered.connect(self.close_func)

        self.cut_action.setIcon(QIcon('images/cut.ico'))  # 6
        self.cut_action.setShortcut('Ctrl+X')
        self.cut_action.setToolTip('Cut the text to clipboard')
        self.cut_action.setStatusTip('Cut the text')
        self.cut_action.triggered.connect(self.cut_func)

        self.copy_action.setIcon(QIcon('images/copy.ico'))  # 7
        self.copy_action.setShortcut('Ctrl+C')
        self.copy_action.setToolTip('Copy the text')
        self.copy_action.setStatusTip('Copy the text')
        self.copy_action.triggered.connect(self.copy_func)

        self.paste_action.setIcon(QIcon('images/paste.ico'))  # 8
        self.paste_action.setShortcut('Ctrl+V')
        self.paste_action.setToolTip('Paste the text')
        self.paste_action.setStatusTip('Paste the text')
        self.paste_action.triggered.connect(self.paste_func)

        self.font_action.setIcon(QIcon('images/font.ico'))  # 9
        self.font_action.setShortcut('Ctrl+T')
        self.font_action.setToolTip('Change the font')
        self.font_action.setStatusTip('Change the font')
        self.font_action.triggered.connect(self.font_func)

        self.color_action.setIcon(QIcon('images/color.ico'))  # 10
        self.color_action.setShortcut('Ctrl+R')
        self.color_action.setToolTip('Change the color')
        self.color_action.setStatusTip('Change the color')
        self.color_action.triggered.connect(self.color_func)

        self.about_action.setIcon(QIcon('images/about.ico'))  # 11
        self.about_action.setShortcut('Ctrl+Q')
        self.about_action.setToolTip('What is Qt?')
        self.about_action.setStatusTip('What is Qt?')
        self.about_action.triggered.connect(self.about_func)

    def save_func(self, text):
        if self.is_saved_first:
            self.save_as_func(text)
        else:
            with open(self.path, 'w') as f:
                f.write(text)
            self.is_saved = True

    def save_as_func(self, text):
        self.path, _ = QFileDialog.getSaveFileName(self, 'Save File', './', 'Files (*.html *.txt *.log)')
        if self.path:
            with open(self.path, 'w') as f:
                f.write(text)
            self.is_saved = True
            self.is_saved_first = False

    def new_func(self):                                                                                 # 新建文件槽函数
        if not self.is_saved and self.text_edit.toPlainText():                    # 判断当前文本是否有保存
            choice = QMessageBox.question(self, '', 'Do you want to save the text?',
                                          QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel)    # 弹框询问是否要保存
            if choice == QMessageBox.Yes:                                                    # 按Yes的话就调用save_func()函数进行保存
                self.save_func(self.text_edit.toHtml())
                # 由于我们的记事本涉及到颜色，所以不能调用QTextEdit的toPlainText()方法
                # 因为该方法获取的是纯文本，所以颜色会丢失掉。应该要调用toHtml()方法保留颜色
                self.text_edit.clear()                                                                   # 保存好了将当前的文本编辑框清空好方便让用户重新写作
                self.is_saved_first = True
            elif choice == QMessageBox.No:                                                  # 若按No不进行保存，就直接清空
                self.text_edit.clear()
            else:                                                                                                    # 若按下Cancel取消，则不进行任何动作
                pass
        else:                                                                                                        # 如果已经保存了，那么就直接清空文本编辑框，并设置相应变量
            self.text_edit.clear()
            self.is_saved = False
            self.is_saved_first = True

    def open_file_func(self):                                                                       # 打开文件槽函数，与新建动作非常相似
        if not self.is_saved:
            choice = QMessageBox.question(self, '', 'Do you want to save the text?',
                                          QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel)
            if choice == QMessageBox.Yes:
                self.save_func(self.text_edit.toHtml())
                file, _ = QFileDialog.getOpenFileName(self, 'Open File', './', 'Files (*.html *.txt *.log)')
                if file:
                    with open(file, 'r') as f:
                        self.text_edit.clear()
                        self.text_edit.setText(f.read())
                        self.is_saved = True
            elif choice == QMessageBox.No:
                file, _ = QFileDialog.getOpenFileName(self, 'Open File', './', 'Files (*.html *.txt *.log)')
                if file:
                    with open(file, 'r') as f:
                        self.text_edit.clear()
                        self.text_edit.setText(f.read())
                        self.is_saved = True
            else:
                pass
        else:
            file, _ = QFileDialog.getOpenFileName(self, 'Open File', './', 'Files (*.html *.txt *.log)')
            if file:
                with open(file, 'r') as f:
                    self.text_edit.clear()
                    self.text_edit.setText(f.read())
                    self.is_saved = True

    def close_func(self):                                                                               # close_func()跟45文件对话框的窗口关闭事件实现方法类似
        if not self.is_saved:
            choice = QMessageBox.question(self, 'Save File', 'Do you want to save the text?',
                                          QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel)
            if choice == QMessageBox.Yes:
                self.save_func(self.text_edit.toHtml())
                self.close()                                                                                    # QCloseEvent.accept()换成了self.close()
            elif choice == QMessageBox.No:
                self.close()
            else:
                pass                                                                                                # QCloseEvent.ignore()其实功能上就相当于pass

    def closeEvent(self, QCloseEvent):
        if not self.is_saved:
            choice = QMessageBox.question(self, 'Save File', 'Do you want to save the text?',
                                          QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel)
            if choice == QMessageBox.Yes:
                self.save_func(self.text_edit.toHtml())
                QCloseEvent.accept()
            elif choice == QMessageBox.No:
                QCloseEvent.accept()
            else:
                QCloseEvent.ignore()

    def cut_func(self):                                                                                   # 剪切文本槽函数
        self.mime_data.setHtml(self.text_edit.textCursor().selection().toHtml())
        # self.text_edit.textCursor()方法:获取文本编辑框当前的指针(类型为QTextCursor)
        # selection()方法:获取到指针当前所选择的内容
        # 但类型为QTextDocumentFragment，需要再调用toHtml()方法来获取到文本内容
        self.clipboard.setMimeData(self.mime_data)
        self.text_edit.textCursor().removeSelectedText()
        # 调用QTextCursor的removeSelectedText()方法
        # 使用户进行剪切后，被剪切的文本消失

    def copy_func(self):                                                                                # 复制文本槽函数，方法同理
        self.mime_data.setHtml(self.text_edit.textCursor().selection().toHtml())
        self.clipboard.setMimeData(self.mime_data)

    def paste_func(self):                                                                               # 粘贴文本槽函数
        self.text_edit.insertHtml(self.clipboard.mimeData().html())
        # 调用insetHtml()方法将剪贴板中的文本插入(该方法会在指针位置插入文本)

    def font_func(self):                                                                                 # 字体对话框槽函数，见43颜色对话框和字体对话框
        font, ok = QFontDialog.getFont()
        if ok:
            self.text_edit.setFont(font)

    def color_func(self):                                                                                # 颜色对话框槽函数，见43颜色对话框和字体对话框
        color = QColorDialog.getColor()
        if color.isValid():
            self.text_edit.setTextColor(color)

    def about_func(self):                                                                              # 打开一个关于Qt的消息框
        QMessageBox.aboutQt(self, 'About Qt')

    def text_edit_int(self):                                                                            # QTextEdit文本编辑框初始化
        self.text_edit.textChanged.connect(self.text_changed_func)    # 连接textChanged信号和槽函数text_changed_func

    def text_changed_func(self):                                                                # 文本编辑槽函数
        if self.text_edit.toPlainText():                                                           # 对self.is_saved变量进行设置
            self.is_saved = False
        else:
            self.is_saved = True

if __name__ == '__main__':
    app = QApplication(sys.argv)

    splash = QSplashScreen()
    splash.setPixmap(QPixmap('images/notebook.jpeg'))
    splash.show()
    splash.showMessage('Welcome to Mr.Zhang\'s Notebook',
                       Qt.AlignBottom | Qt.AlignCenter, Qt.red)
    time.sleep(2)

    demo = Demo()
    demo.show()
    splash.finish(demo)

    sys.exit(app.exec_())
