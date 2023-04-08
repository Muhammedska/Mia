import os
from pydub import AudioSegment as fc
from youtube_search import YoutubeSearch


def convert(path, exportPath):
    file = path
    if os.path.isfile(file):
        None
    elif os.path.isdir(file):
        files = os.listdir(file)
        for i in files:

            dot = 0
            for m in i:
                if m == '.':
                    dot += 1
            if dot > 1:
                fi = i.replace('.', ' ', dot-1)
            print(path+i, fi)
            if os.path.isfile(path+i):
                wav_audio = fc.from_file(path+i)
                filename = exportPath+fi.replace('.m4a', '.mp3')
                wav_audio.export(filename, format="mp3")


path = './mp3/'
l = []
k = []
for i in os.listdir(path):
    l.append(i.replace('.m4a', ' '))

for m in l:
    z = []
    results = YoutubeSearch(m, max_results=1).to_dict()
    for c in results:
        z.append(c['url_suffix'])
        z.append(c['title'])
    k.append(z)

