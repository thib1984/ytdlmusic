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

    for children in videosSearch.result()["result"]:
        print("")
        i=i+1
        print(i)
        print(children["title"])
        print(children["duration"])    
        print(str(children["publishedTime"]) +" - "+ children["viewCount"]["text"])
        print("************************************")

    print("")
    answer = input("which? ")
    download_song(videosSearch.result()["result"][int(answer)-1]["link"], artiste + ' '  + titre)

        
