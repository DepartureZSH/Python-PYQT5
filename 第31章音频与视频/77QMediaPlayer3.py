import sys
from PyQt5.Qt import QUrl, QVideoWidget
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent, QMediaPlaylist
from PyQt5.QtWidgets import QApplication, QWidget


class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.resize(960, 800)
        self.playlist = QMediaPlaylist(self)
        self.video_widget = QVideoWidget(self)              # 实例化QVideoWidget控件，并将该控件的初始大小调整为窗口大小
        self.video_widget.resize(self.width(), self.height())

        self.player = QMediaPlayer(self)
        self.player.setPlaylist(self.playlist)
        self.player.setVideoOutput(self.video_widget)       # 调用播放器的setVideoOutput()方法并传入QVideoWidget实例来设置视频播放设备

        self.playlist.addMedia(QMediaContent(QUrl.fromLocalFile('./媒体文件/MP4/video1.mp4')))  # 将媒体文件换为视频
        self.playlist.addMedia(QMediaContent(QUrl.fromLocalFile('./媒体文件/MP4/video2.mp4')))
        self.playlist.addMedia(QMediaContent(QUrl.fromLocalFile('./媒体文件/MP4/video3.mp4')))
        self.playlist.setPlaybackMode(QMediaPlaylist.Loop)
        self.playlist.setCurrentIndex(2)

        self.player.setVolume(80)
        self.player.play()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())