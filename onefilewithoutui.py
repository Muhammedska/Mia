import re
import os
from pytube import Playlist
from moviepy.editor import *

CURRENT_DIR = os.getcwd()


def core():
    if os.path.isdir('./core/t') == False:
        print(']=> '+'./core  not found')
        os.mkdir('./core')
        print(']=> '+'./core  was created')
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


def downPlaylist(url,downloadedlinklist,mp4dir):
    linklist = downloadedlinklist
    URL = url
    playlist = Playlist(URL)
    DOWNLOAD_DIR = mp4dir
    playlist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")
    print(len(playlist.video_urls))
    for url in playlist.video_urls:
        print(url)
    indi = 1
    for video in playlist.videos:
        print('\n')
        try:
            print('{} - {}  ::  downloading : {} with url : {} channel : {}'.format(str(indi),str(len(playlist.videos)), video.title, video.watch_url, video.author))
            x = [s for s in video.streams if "mp4" in str(s)]
            special_charsx = ['/', "|", '\\', '.', '"', "<", ">", "?", "*"]
            videoname =video.author+ " - " + video.title
            for i in special_charsx:
                videoname = videoname.replace(i, ' ')
            print(x[0].download(filename=DOWNLOAD_DIR+"/"+videoname+".mp4"))
        except:
            print(str(indi) + ' . videoda sıkıntı meydana geldi')
        
        indi += 1

def playlistChecker(url,file):
    URL = url
    playlist = Playlist(URL)
    DOWNLOAD_DIR = './mp4'
    playlist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")
    print(len(playlist.video_urls))
    indi = 1
    for url in playlist.video_urls:
        if len(playlist.video_urls) == indi:
            file.write(url)
        else:
            file.write(url+',')
            indi+=1
def opticore(url,mp4dir,mp3dir,downloadedlinklist):
    linklist = downloadedlinklist
    URL = url
    playlist = Playlist(URL)
    DOWNLOAD_DIR = mp4dir
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
        #video.author+' '+
        videoname = video.title
        for i in special_charsx:
            videoname = videoname.replace(i, ' ')
        print(x[0].download(filename=DOWNLOAD_DIR+"/"+videoname+".mp4"))
        print(':: {} :: Started to do convert'.format(videoname))
        mp4_file = mp4dir+'/'+videoname+".mp4"
        mp3_file = mp3dir+'/'+i.replace('.mp4', '.mp3')
        videoclip = VideoFileClip(mp4_file)
        audioclip = videoclip.audio
        audioclip.write_audiofile(mp3_file)
        
        audioclip.close()
        videoclip.close()        
        os.remove(mp4_file)
        indi += 1

def cleaner(path):
    files = os.listdir(path)
    indi = 1
    
    for i in files:
        os.remove(path+'/'+i)
        print("[{}/{} - ({})] files was removed".format(indi,len(files),i))
        indi+=1
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

MP4_PATH = './core/mp4'
MP3_PATH = './core/mp3'
APP_ITEM_CORE_DIR = './core/t'

LINK_LIST_FILE = open(APP_ITEM_CORE_DIR+'app.txt','w+',encoding='utf-8')
cleaner(MP4_PATH)
while True:
    a = str(input('Youtube-mp3 Downloader Mia BY:ÇÖZELTİ SOFTWARE\n1 = Single\n2 = PLaylist\n3 = Exit\n\n>>> '))
    if a == '3'  or a == 'exit':
        break
    elif a == '2':
        while True:
            b = str(input('\nPLaylist link (0 or exit for mainmenu)\n=> '))
            if b == '0' or b== 'exit':
                break
            else:
                if 'music.youtube' in b:
                    b.replace('music.youtube','youtube')
                lists = LINK_LIST_FILE.read().split(',')
                downPlaylist(b,lists,MP4_PATH)
                print('\n\nstarting Convertion sessions\n\n')
                dirScanCon(MP4_PATH,MP3_PATH)
                print('\n\nstarting Convertion sessions ended\n\n')
    elif a == '1':
        print('This Method wasn\'t available')
        b = str(input('\nPLaylist link (0 or exit for mainmenu)\n=> '))
        if b == '0' or b== 'exit':
            break
        else:
            if 'music.youtube' in b:
                b.replace('music.youtube','youtube')
            lists = LINK_LIST_FILE.read().split(',')
            opticore(b,MP4_PATH,MP3_PATH,lists)

                

