import sys
from PyQt5.Qt import QUrl
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent, QMediaPlaylist
from PyQt5.QtWidgets import QApplication, QWidget


class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.playlist = QMediaPlaylist(self)                    # 实例化QMediaPlaylist对象
        self.player = QMediaPlayer(self)                        # 实例化QMediaPlayer对象
        self.player.setPlaylist(self.playlist)                  # 调用QMediaPlayer实例的setPlaylist()方法传入QMediaPlaylist实例

        # 调用addMedia()传入要播放的文件，类型为QMediaContent
        self.playlist.addMedia(QMediaContent(QUrl.fromLocalFile('E:\python save\pyqt\practices\第31章音频与视频\媒体文件\MP3\music1.mp3')))
        self.playlist.addMedia(QMediaContent(QUrl.fromLocalFile('E:\python save\pyqt\practices\第31章音频与视频\媒体文件\MP3\music2.mp3')))
        self.playlist.addMedia(QMediaContent(QUrl.fromLocalFile('E:\python save\pyqt\practices\第31章音频与视频\媒体文件\MP3\music3.mp3')))
        self.playlist.setPlaybackMode(QMediaPlaylist.Loop)      # 3
        self.playlist.setCurrentIndex(2)                        # 4

        self.player.setVolume(80)                               # 5
        self.player.play()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())