import re
import os
from pytube import Playlist
from moviepy.editor import *

CURRENT_DIR = os.getcwd()


def core():
    paths = ['mp4', 'mp3']
    for i in paths:
        if os.path.isdir('./core/'+i) == False:
            print(']=> '+'./core/'+i+' not found')
            os.mkdir('./core/'+i)
            print(']=> '+'./core/'+i+' was created')
    if os.path.isfile('./core/t/app.txt') == False:
        print(']=> '+'./core/t/app.txt'+' not found')
        if os.path.isdir('./core/t') == False:
            print(']=> '+'./core/t/'+' not found')
            os.mkdir('./core/t/')
            print(']=> '+'./core/t/'+' was created ')
        create = open('./core/t/app.txt', 'w').close()
        print(']=> '+'./core/t/app.txt'+' was created')


def downPlaylist(url):
    URL = url
    playlist = Playlist(URL)
    DOWNLOAD_DIR = './mp4'
    playlist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")
    print(len(playlist.video_urls))
    for url in playlist.video_urls:
        print(url)
    indi = 1
    for video in playlist.videos:
        print('\n')
        print('{} - {}  ::  downloading : {} with url : {}'.format(str(indi),
              str(len(playlist.videos)), video.title, video.watch_url))
        x = [s for s in video.streams if "mp4" in str(s)]

        special_charsx = ['/', "|", '\\', '.', '"', "<", ">", "?", "*"]
        videoname = video.title
        for i in special_charsx:
            videoname = videoname.replace(i, ' ')
        print(x[0].download(filename=DOWNLOAD_DIR+"/"+videoname+".mp4"))
        indi += 1

def dirScanCon(mp4dir,mp3dir):
    MP4_DIR = mp4dir
    MP3_DIR = mp3dir

    mp4 = os.listdir(MP4_DIR)
    filelen = len(mp4)
    indi = 1
    for i in mp4:
        print('%{} ::  {}/{} :: Started to do convert {}'.format(str((100 *indi)/filelen), filelen, indi, i))
        mp4_file = MP4_DIR+'/'+i
        mp3_file = MP3_DIR+'/'+i.replace('.mp4', '.mp3')
        videoclip = VideoFileClip(mp4_file)
        audioclip = videoclip.audio
        audioclip.write_audiofile(mp3_file)
        audioclip.close()
        videoclip.close()
        print('converting ended.. next one \n')
        indi += 1

print('checking system files and dirs')
core()
while True:
    a = str(input('Youtube-mp3 Downloader Mia \n1 = Single\n2 = PLaylist\n3 = Exit'))
    if a == '3':
        break
    elif a == '2':
        while True:
            b = str(input('\nPLaylist link (0 or exit for mainmenu)\n=> '))
            if b == '0' or b== 'exit':
                break

