from dataclasses import replace
import webbrowser
import requests
from youtube_search import YoutubeSearch
import youtube_dl
from bs4 import BeautifulSoup
import os

import sys

from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import QTimer, QUrl
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import QPoint
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QWidget


import json

# Opening JSON file
f = open('app.json')

# returns JSON object as
# a dictionary
data = json.load(f)

# Close the JSON file
f.close()


class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('./app.ui', self)
        self.search.clicked.connect(self.search_clicked)
        self.download.clicked.connect(self.download_clicked)
        self.youtube.clicked.connect(self.youtube_clicked)
        self.me.clicked.connect(self.me_clicked)

    def search_clicked(self):
        self.video_ID = []
        self.songlist.clear()
        results = YoutubeSearch(self.sinput.text(), max_results=10).to_dict()
        for i in results:
            self.video_ID.append(i['url_suffix'])
            self.songlist.addItem(i['title'])

    def download_clicked(self):
        QMessageBox.information(
            self, "Download", "Downloading started please wait...")
        # print()
        video_url = "https://www.youtube.com" + \
            self.video_ID[self.songlist.currentRow()]
        video_info = youtube_dl.YoutubeDL().extract_info(url=video_url, download=False,)
        # print(video_info)
        vname = video_info['title'].replace(r"\\", ' ')
        filename = f"./songs/{vname}.mp3"
        options = {
            'format': 'bestaudio/best',
            'keepvideo': False,
            'outtmpl': filename,

        }
        with youtube_dl.YoutubeDL(options) as ydl:
            ydl.download([video_info['webpage_url']])

        QMessageBox.information(self,
                                "Download", "Download complete... {}".format(filename))

    def youtube_clicked(self):
        webbrowser.open("https://www.youtube.com" +
                        self.video_ID[self.songlist.currentRow()])

    def me_clicked(self):
        webbrowser.open("github.com/Muhammedska")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mw = Ui()
    mw.show()
    sys.exit(app.exec_())
