"""import re
from pytube import Playlist

YOUTUBE_STREAM_AUDIO = '144' # modify the value to download a different stream
DOWNLOAD_DIR = './nokia'

playlist = Playlist('https://www.youtube.com/playlist?list=PLwYzzR712Au9pf8DwZ2OVbrN0OVvbhG7j')

# this fixes the empty playlist.videos list
playlist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")

print(len(playlist.video_urls))

for url in playlist.video_urls:
    print(url)

# physically downloading the audio track
for video in playlist.videos:

    audioStream = video.streams.get_by_itag(YOUTUBE_STREAM_AUDIO).get_audio_only()
    audioStream.download(output_path=DOWNLOAD_DIR)"""



"""import re
from pytube import Playlist
playlist = Playlist('https://www.youtube.com/playlist?list=PLwYzzR712Au9pf8DwZ2OVbrN0OVvbhG7j')   
DOWNLOAD_DIR = './nokia'
playlist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")    
print(len(playlist.video_urls))    
for url in playlist.video_urls:
    print(url)    
for video in playlist.videos:
    print('downloading : {} with url : {}'.format(video.title, video.watch_url))
    video.streams.\
        filter(type='audio',only_audio=True, progressive=True, file_extension='mp3').\
        order_by('resolution').\
        desc().\
        first().\
        download(DOWNLOAD_DIR)"""

import re
from pytube import Playlist
playlist = Playlist('https://www.youtube.com/playlist?list=PLwYzzR712Au9pf8DwZ2OVbrN0OVvbhG7j')   
DOWNLOAD_DIR = './nokia'
playlist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")    
print(len(playlist.video_urls))    
for url in playlist.video_urls:
    print(url)
indi = 1    
for video in playlist.videos:
    print('\n')
    print('{} - {}  ::  downloading : {} with url : {}'.format(str(indi),str(len(playlist.videos)),video.title, video.watch_url))
    x = [s for s in video.streams if "mp4" in str(s)]
    
    special_charsx = ['/',"|",'\\','.','"',"<",">","?","*"]
    videoname = video.title
    for i in special_charsx:
        videoname = videoname.replace(i,' ')
    print(x[0].download(filename=DOWNLOAD_DIR+"/"+videoname+".mp3"))
    indi += 1