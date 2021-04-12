import sys
import re
import os.path
import subprocess
from shutil import which


def download_song(song_url, song_title):

    import youtube_dl

    outtmpl = song_title + ".%(ext)s"
    # TODO test if exist
    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": outtmpl,
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            },
            {"key": "FFmpegMetadata"},
        ],
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.extract_info(song_url, download=True)


def ytdlmusic():

    if len(sys.argv) == 2 and sys.argv[1] == "update":
        prog = "pip3"
        if which(prog) is None:
            prog = "pip"
        print
        print("try to update youtube-dl with " + prog)
        subprocess.check_call(
            [
                prog,
                "install",
                "--upgrade",
                "youtube-dl",
            ]
        )
        print
        print("try to update youtube-search-python with " + prog)
        subprocess.check_call(
            [
                prog,
                "install",
                "--upgrade",
                "youtube-search-python",
            ]
        )
        print
        print("try to update ytdlmusic with " + prog)
        subprocess.check_call(
            [
                prog,
                "install",
                "--upgrade",
                "ytdlmusic",
            ]
        )
        exit(0)

    if not len(sys.argv) == 4 and not len(sys.argv) == 3:
        help_txt = """\

        NAME
            ytdlmusic

        SYNOPSIS
           With ytdlmusic, you can download from youtube a mp3 music without use browser. 5 choices are available with small summary 
           to facilitate the choice. You can also use auto mode to download the first item. 

            help            : display this help
                            -> ytdlmusic help
            update          : try to upgrade youtube-dl, youtube-search-python, and ytdlmusic
                            -> ytdlmusic update                            
            artist song     : display 5 choices from youtube with given search, then download the mp3 choosen by user
                            -> example : ytdlmusic "the beatles" "let it be"
            artist song auto: download mp3 of the first from youtube with given search
                            -> example : ytdlmusic "the beatles" "let it be" auto
            """
        print(help_txt)
        exit(0)

    try:
        from youtubesearchpython import VideosSearch
        import youtube_dl

        artist = sys.argv[1]
        song = sys.argv[2]

        print("artist : " + artist)
        print("song : " + song)

        print(
            "search "
            + artist
            + " "
            + song
            + " mp3 with youtubesearchpython"
        )
        videosSearch = VideosSearch(
            artist + " " + song + " mp3", limit=5
        )
        i = 0
        if len(videosSearch.result()["result"]) == 0:
            print("no result, retry with other other words")
            exit(0)
        answer = 1
        if not len(sys.argv) > 3 or not sys.argv[3] == "auto":
            print
            for children in videosSearch.result()["result"]:
                i = i + 1
                print(i)
                print(children["title"])
                print(children["link"])
                print(
                    children["duration"]
                    + " - "
                    + children["viewCount"]["text"]
                )
                print

            while True:
                answer = input(
                    "which (1-"
                    + str(len(videosSearch.result()["result"]))
                    + ", 0 to exit properly) ? "
                )
                if (
                    answer.isnumeric()
                    and int(answer) >= 0
                    and int(answer) <= 5
                ):
                    break
            if int(answer) == 0:
                print
                exit(0)
        file_name = re.sub("(\W+)", "_", artist.lower() + "_" + song.lower()
        )
        if os.path.exists(file_name + ".mp3"):
            i = 0
            while True:
                i = i + 1
                file_name_tmp = file_name + "_" + str(i)
                if not os.path.exists(file_name_tmp + ".mp3"):
                    file_name = file_name_tmp
                    break
        print("future filename is : " + file_name + ".mp3")
        print(
            "download "
            + videosSearch.result()["result"][int(answer) - 1]["link"]
            + " with youtubedl"
        )

        download_song(
            videosSearch.result()["result"][int(answer) - 1]["link"],
            file_name,
        )
        print(file_name + ".mp3 is ready")
    except Exception as err:
        print()
        print("Unexpected error:", err)
        print()
        print(
            "try to upgrade with 'ytdlmusic update' and retry. Have you too install ffmpeg?"
        )
        print(
            "if you reproduce the error after update : you can open an issue at https://github.com/thib1984/ytdlmusic/issues with this log"
        )


if __name__ == "__main__":
    ytdlmusic()