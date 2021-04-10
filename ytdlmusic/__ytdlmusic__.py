from youtubesearchpython import VideosSearch
import sys
import youtube_dl

def download_song(song_url, song_title):

    outtmpl = song_title + '.%(ext)s'
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': outtmpl,
        'postprocessors': [
            {'key': 'FFmpegExtractAudio','preferredcodec': 'mp3',
             'preferredquality': '192',
            },
            {'key': 'FFmpegMetadata'},
        ],
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(song_url, download=True) 

def ytdlmusic() :

    artiste = sys.argv[1]
    titre = sys.argv[2]
    videosSearch = VideosSearch(artiste + ' '  + titre + ' mp3', limit = 5)
    i=0
    answer =1
    if (not len(sys.argv) >3 or not sys.argv[3] == "auto"):
        for children in videosSearch.result()["result"]:
            print("")
            i=i+1
            print(i)
            print(children["title"])
            print(children["link"])             
            print(children["duration"] + " - " + children["viewCount"]["text"])   
            print()

        print("")
        while True:
            answer = input("which (1-5, 0 to exit properly) ? ")
            if (answer.isnumeric() and int(answer) >= 0 and int(answer) <= 5):
                break
        if (int(answer) == 0):
            exit(0)
    print("")               
    download_song(videosSearch.result()["result"][int(answer)-1]["link"], artiste + ' '  + titre)

        
