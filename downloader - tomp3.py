import os
from moviepy.editor import *


def dirScanCon(mp4dir,mp3dir):
    MP4_DIR = mp4dir
    MP3_DIR = mp3dir

    mp4 = os.listdir(MP4_DIR)
    filelen = len(mp4)
    indi = 1
    for i in mp4:
        print('%{} ::  {}/{} :: Started to do convert {}'.format(str((100 *indi)/filelen), filelen, indi, i))
        mp4_file = MP4_DIR+'/'+i
        mp3_file = MP3_DIR+'/'+i.replace('.m4a', '.mp3')
        videoclip = VideoFileClip(mp4_file)
        audioclip = videoclip.audio
        audioclip.write_audiofile(mp3_file)
        audioclip.close()
        videoclip.close()
        print('converting ended.. next one \n')
        indi += 1
dirScanCon('./core/mp4','./mp3')