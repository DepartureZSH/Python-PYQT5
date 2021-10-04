import pyqtgraph.examples
pyqtgraph.examples.run()
#################################################################
#       参数        类型        默认值                     解释
# leftButtonPan     bool        True      值为True的话，可以用鼠标左键来上下左右拖动图表;若为False,拖动鼠标左键会形成一个矩形框，视图镜头会随之深入
# foreground     参考mkColor()   'd'      设置前景颜色(包括文本、线条、坐标轴等)，'d'为灰色
# background     参考mkColor()   'K'      设置背景颜色，'K'为黑色
# antialias         bool        False     是否启用抗锯齿(可以让曲线更加光滑)
# useOpenGL         bool        False     是否在视图中启用OpenGL
# crashWarning      bool        False     则会打印针对可能导致程序崩溃情况的警告
#################################################################
# pyqtgraph.plot()
# 在一个新窗口中绘制数据(窗口中包含一个plotWidget)
# PlotWidget.plot()
# 在plotWidget控件中绘制数据
#################################################################
# plot()方法的基本参数如下：
# x - X轴数据(可选)。如果没有赋值的话，程序则自动生成特定范围的整数值
# y - Y轴数据
# pen - 图表线条的画笔参数，若设为None则不显示线条
# symbol - 参数为字符串类型，用于描述图表每个坐标点的形状。比如设为'o'，则坐标点的形状就为o。
#       可选值总共有这么几种：'o', 's', 't', 't1', 't2', 't3','d', '+', 'x', 'p', 'h', 'star'
# symbolPen - 描绘符号轮廓的画笔参数
# symbolBrush - 填充符号的画刷参数
# fillLevel - 用于计算曲线下面积的Y坐标值
# brush - 用于填充曲线下面积的画刷
#################################################################
# 在PyQtGraph中，可以使用mkColor()，mkPen()以及mkBrush()方法来实例化相应的对象
#################################################################
# 可以给传参给mkColor()方法来实例化一个QColor颜色对象，可传参数类型有：
# 'c'               r, g. b, c.m, y, k, w中的一种
# R, G,B,[A]        整数0-255
# (R,G,B.[A])       整数元组0-255
# float             灰度值0.0-1.0
# "RGB"             十六进制字符串,可以在前面加#
# "RGBA"            同上
# "RRGGBB"          同上
# "RRGGBBAA"        同上
# QColor            QColor实例

# 第一行中的单个字符串所对应的值如下：
# 'b': QtGui.QColor(0,0,255,255)
# 'g': QtGui.QColor(0,255,0,255)
# 'r': QtGui.QColor(255,0,0,255)
# 'c': QtGui.QColor(0,255,255,255)
# 'm': QtGui.QColor(255,0,255,255)
# 'y': QtGui.QColor(255,255,0,255)
# 'k': QtGui.QColor(0,0,0,255)
# 'w': QtGui.QColor(255,255,255,255)
# 'd': QtGui.QColor(150,150,150,255)
# 'l': QtGui.QColor(200,200,200,255)
# 's': QtGui.QColor(100,100,150,255)
#################################################################
# 准确来说，能被mkColor()接受的参数都能用在mkPen()中。
# mkPen('r')
# mkPen(255, 255, 255)
# mkPen((255, 255, 255, 255))
# mkPen('#0000FF')
# mkPen(QColor)
# 除了颜色我们还可以设置画笔粗细：
# mkPen(color='r', width=2)
# mkPen({'color': '#0000FF', width: 2})
# 如果不想设置画笔，我们可以传入None：
# mkPen(None)
# 画刷设置同理，可以接受所有能被mkColor()接受的参数。可传入None不设置画刷。
#################################################################
