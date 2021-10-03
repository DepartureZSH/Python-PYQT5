import sys
from PyQt5.Qt import QUrl
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent, QMediaPlaylist
from PyQt5.QtWidgets import QApplication, QWidget, QListWidget, QLabel, QSlider, QPushButton, QHBoxLayout, \
    QVBoxLayout


class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()

        # 实例化需要用到的控件：
        #
        # time_label: 显示剩余时间
        # volume_slider: 音量滑动条
        # progress_slider: 播放进度条
        # sound_btn: 喇叭按钮
        # previous_btn: 上一首按钮
        # play_pause_btn: 播放和暂停按钮
        # next_btn: 下一首按钮
        # mode_btn: 播放模式按钮
        # list_btn: 显示和隐藏列表按钮
        # list_widget: 列表控件显示全部播放列表
        self.time_label = QLabel(self)
        self.volume_slider = QSlider(self)
        self.progress_slider = QSlider(self)
        self.sound_btn = QPushButton(self)
        self.previous_btn = QPushButton(self)
        self.play_pause_btn = QPushButton(self)
        self.next_btn = QPushButton(self)
        self.mode_btn = QPushButton(self)
        self.list_btn = QPushButton(self)
        self.list_widget = QListWidget(self)

        self.h1_layout = QHBoxLayout()
        self.h2_layout = QHBoxLayout()
        self.all_v_layout = QVBoxLayout()

        # 实例化QMediaPlayer和QMediaPlaylist
        self.playlist = QMediaPlaylist(self)
        self.player = QMediaPlayer(self)

        self.widget_init()
        self.layout_init()
        self.signal_init()

    def widget_init(self):
        self.time_label.setText('--/--')
        # QMediaPlayer的音量值范围为0-100，所以我们将其设置为volume_slider的音量值范围
        self.volume_slider.setRange(0, 100)
        self.volume_slider.setValue(100)
        self.volume_slider.setOrientation(Qt.Horizontal)

        # 媒体文件未播放前，播放进度条无法使用
        self.progress_slider.setEnabled(False)
        self.progress_slider.setOrientation(Qt.Horizontal)

        # 设置各个按钮的图标
        self.sound_btn.setIcon(QIcon('images/sound_on.png'))
        self.previous_btn.setIcon(QIcon('images/previous.png'))
        self.play_pause_btn.setIcon(QIcon('images/play.png'))
        self.next_btn.setIcon(QIcon('images/next.png'))
        self.mode_btn.setIcon(QIcon('images/list_loop.png'))
        self.list_btn.setIcon(QIcon('images/show.png'))

        self.player.setPlaylist(self.playlist)
        # media_list用于存储各个媒体文件的绝对路径
        self.media_list = ['E:\python save\pyqt\practices\第31章音频与视频\媒体文件\MP3\music1.mp3',
                           'E:\python save\pyqt\practices\第31章音频与视频\媒体文件\MP3\music2.mp4',
                           'E:\python save\pyqt\practices\第31章音频与视频\媒体文件\MP3\music3.mp3']
        for m in self.media_list:
            self.playlist.addMedia(QMediaContent(QUrl.fromLocalFile(m)))
        self.playlist.setPlaybackMode(QMediaPlaylist.Sequential)
        # 添加到列表中的应该是文件名，而不是路径，所以用split()方法获取到路径最后的文件名
        self.list_widget.addItems([m.split('\\')[-1] for m in self.media_list])

    def layout_init(self):
        # 布局
        self.h1_layout.addWidget(self.progress_slider)
        self.h1_layout.addWidget(self.time_label)
        self.h2_layout.addWidget(self.volume_slider)
        self.h2_layout.addWidget(self.sound_btn)
        self.h2_layout.addWidget(self.previous_btn)
        self.h2_layout.addWidget(self.play_pause_btn)
        self.h2_layout.addWidget(self.next_btn)
        self.h2_layout.addWidget(self.mode_btn)
        self.h2_layout.addWidget(self.list_btn)

        self.all_v_layout.addLayout(self.h1_layout)
        self.all_v_layout.addLayout(self.h2_layout)
        self.all_v_layout.addWidget(self.list_widget)
        self.all_v_layout.setSizeConstraint(QVBoxLayout.SetFixedSize)
        # 显示和隐藏列表会使窗口的大小发生改变，
        # 这里我们将布局的sizeConstraint属性设置为SetFixedSize值，
        # 这样用户无法修改窗口的大小，而是让布局管理器自己来负责调整。
        # 设置之后窗口大小发生改变的话，都能够以最佳的尺寸进行显示。

        self.setLayout(self.all_v_layout)

    def signal_init(self):
        # 将按钮全部连接到btn_func()槽函数上
        self.sound_btn.clicked.connect(lambda: self.btn_func(self.sound_btn))
        self.previous_btn.clicked.connect(lambda: self.btn_func(self.previous_btn))
        self.play_pause_btn.clicked.connect(lambda: self.btn_func(self.play_pause_btn))
        self.next_btn.clicked.connect(lambda: self.btn_func(self.next_btn))
        self.mode_btn.clicked.connect(lambda: self.btn_func(self.mode_btn))
        self.list_btn.clicked.connect(lambda: self.btn_func(self.list_btn))
        # 音量滑动条的功能以及列表双击播放的功能
        self.volume_slider.valueChanged.connect(self.volume_slider_func)
        self.list_widget.doubleClicked.connect(self.list_play_func)

        self.player.durationChanged.connect(self.get_duration_func)
        self.player.positionChanged.connect(self.get_position_func)
        self.progress_slider.sliderMoved.connect(self.update_position_func)

    def btn_func(self, btn):
        # 如果是喇叭按钮按下的话，
        # 调用QMediaPlayer类的isMuted()方法判断是否已经静音，
        # 再调用setMuted()方法来作出相应的操作，按钮图标同时改变
        if btn == self.sound_btn:
            if self.player.isMuted():
                self.player.setMuted(False)
                self.sound_btn.setIcon(QIcon('images/sound_on'))
            else:
                self.player.setMuted(True)
                self.sound_btn.setIcon(QIcon('images/sound_off'))

        # 如果是上一首按钮的话，
        # 则要先调用QMediaPlaylist的currentIndex()方法来知道当前播放文件的索引。
        # 如果等于0的话说明正在播放第一个文件，那此时已经没有上一首了，所以播放最后一首,
        # 最后一首的索引也就是mediaCount()-1；
        # 如果不等于0那就直接调用QMediaPlayer类的previous()方法来播放上一首歌曲
        elif btn == self.previous_btn:
            if self.playlist.currentIndex() == 0:
                self.playlist.setCurrentIndex(self.playlist.mediaCount() - 1)
            else:
                self.playlist.previous()

        # 先判断播放器的状态，如果正在播放的话，则暂停，否则开始/继续播放。
        # 下面是QMediaPlayer.state()可返回的值:
        # QMediaPlayer::StoppedState    0   停止状态
        # QMediaPlayer::PlayingState    1   正在播放状态
        # QMediaPlayer::PausedState     2   暂停状态
        elif btn == self.play_pause_btn:
            if self.player.state() == 1:
                self.player.pause()
                self.play_pause_btn.setIcon(QIcon('images/play.png'))
            else:
                self.player.play()
                self.play_pause_btn.setIcon(QIcon('images/pause.png'))

        # 逻辑同previous_btn类似
        elif btn == self.next_btn:
            if self.playlist.currentIndex() == self.playlist.mediaCount() - 1:
                self.playlist.setCurrentIndex(0)
            else:
                self.playlist.next()

        # 如果是播放模式按钮的话，就相应的调用setPlaybackMode()方法来改变播放模式，同时还要改变按钮的图标
        elif btn == self.mode_btn:
            if self.playlist.playbackMode() == 2:
                self.playlist.setPlaybackMode(QMediaPlaylist.Loop)
                self.mode_btn.setIcon(QIcon('images/item_loop.png'))

            elif self.playlist.playbackMode() == 3:
                self.playlist.setPlaybackMode(QMediaPlaylist.Random)
                self.mode_btn.setIcon(QIcon('images/random.png'))

            elif self.playlist.playbackMode() == 4:
                self.playlist.setPlaybackMode(QMediaPlaylist.Sequential)
                self.mode_btn.setIcon(QIcon('images/list_loop.png'))

        # 如果是列表按钮，就先判断列表控件当前是否可见，再做出相应操作即可
        elif btn == self.list_btn:
            if self.list_widget.isHidden():
                self.list_widget.show()
                self.list_btn.setIcon(QIcon('images/show.png'))
            else:
                self.list_widget.hide()
                self.list_btn.setIcon(QIcon('images/hide.png'))

    def volume_slider_func(self, value):        # value来自ValueChanged信号，也就是滑动条当前的值
        # 每次音量滑动条值发生改变，
        # 就调用setVolume()方法将播放器的音量设置成相应的值，
        # 如果音量为0的话还要记得将喇叭按钮图标改成静音图标
        self.player.setVolume(value)
        if value == 0:
            self.sound_btn.setIcon(QIcon('images/sound_off.png'))
        else:
            self.sound_btn.setIcon(QIcon('images/sound_on.png'))

    def list_play_func(self):
        self.playlist.setCurrentIndex(self.list_widget.currentRow())
        self.player.play()
        self.play_pause_btn.setIcon(QIcon('images/pause.png'))

    def get_duration_func(self, d):
        self.progress_slider.setRange(0, d)
        self.progress_slider.setEnabled(True)
        self.get_time_func(d)

    def get_time_func(self, d):
        seconds = int(d / 1000)
        minutes = int(seconds / 60)
        seconds -= minutes * 60
        if minutes == 0 and seconds == 0:
            self.time_label.setText('--/--')
            self.play_pause_btn.setIcon(QIcon('images/play.png'))
        else:
            self.time_label.setText('{}:{}'.format(minutes, seconds))

    def get_position_func(self, p):
        self.progress_slider.setValue(p)

    def update_position_func(self, v):
        self.player.setPosition(v)
        d = self.progress_slider.maximum() - v
        self.get_time_func(d)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())