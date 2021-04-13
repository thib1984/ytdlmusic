"""
ytdlmusic scripts
"""

import sys
import re
import os.path
import subprocess
from shutil import which


def ytdlmusic():
    """
    entry point from ytdlmusic
    """

    # special entries
    if len(sys.argv) == 2 and sys.argv[1] == "help":
        display_help()
        sys.exit(0)

    if len(sys.argv) == 2 and sys.argv[1] == "update":
        update()
        sys.exit(0)

    if len(sys.argv) == 2 and sys.argv[1] == "version":
        version()
        sys.exit(0)

    if len(sys.argv) != 4 and len(sys.argv) != 3:
        display_help()
        sys.exit(0)

    try:
        artist = sys.argv[1]
        song = sys.argv[2]

        r_search = search(artist, song)
        answer = choice(r_search)
        file_name = determine_filename(artist, song)
        u_choice = r_search.result()["result"][answer - 1]
        download_song(
            u_choice["link"],
            file_name,
        )
    except Exception as err:
        print_error(err)


def print_error(err):
    """
    print generic error
    """
    print("Unexpected error:", err)

    version()
    print(
        "try to upgrade with 'ytdlmusic update' or manually and retry. Have-you too install ffmpeg for your system?"
    )
    print(
        "if you reproduce the error after the update : you can open an issue at https://github.com/thib1984/ytdlmusic/issues with this log"
    )


def version():
    """
    print version
    """
    import pkg_resources

    try:
        ytdlmusicversion = pkg_resources.get_distribution(
            "ytdlmusic"
        ).version
    except Exception as err:
        ytdlmusicversion = "NON INSTALLE"
    try:
        ytsearchpythonversion = pkg_resources.get_distribution(
            "youtube-search-python"
        ).version
    except Exception as err:
        ytsearchpythonversion = "NON INSTALLE"
    try:
        youtubedlversion = pkg_resources.get_distribution(
            "youtube-dl"
        ).version
    except Exception as err:
        youtubedlversion = "NON INSTALLE"
    if which("ffmpeg") is None:
        ffmpeg_binary = "NON INSTALLE"
    else:
        ffmpeg_binary = which("ffmpeg")
    print("ytdlmusic version             : " + ytdlmusicversion)
    print("youtube-search-python version : " + ytsearchpythonversion)
    print("youtube-dl version            : " + youtubedlversion)
    print("ffmpeg                        : " + ffmpeg_binary)


def determine_filename(artist, song):
    """
    correct filename to escape special characters
    """
    file_name = re.sub(
        "(\\W+)", "_", artist.lower() + "_" + song.lower()
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
    return file_name


def search(artist, song):
    """
    search the items
    """
    from youtubesearchpython import VideosSearch

    print("artist : " + artist)
    print("song : " + song)
    print(
        "search "
        + artist
        + " "
        + song
        + " mp3 with youtubesearchpython"
    )
    results_search = VideosSearch(
        artist + " " + song + " mp3", limit=5
    )

    return results_search


def choice(results_search):
    """
    user choice
    """
    i = 0
    if len(results_search.result()["result"]) == 0:
        print("no result, retry with other words")
        sys.exit(0)
    answer = 1
    if len(sys.argv) <= 3 or sys.argv[3] != "auto":
        for children in results_search.result()["result"]:
            i = i + 1
            print(i)
            print(children["title"])
            print(children["link"])
            print(
                children["duration"]
                + " - "
                + children["viewCount"]["text"]
            )

        while True:
            answer = input(
                "which (1-"
                + str(len(results_search.result()["result"]))
                + ", 0 to exit properly) ? "
            )
            if (
                answer.isnumeric()
                and int(answer) >= 0
                and int(answer) <= 5
            ):
                break
        if int(answer) == 0:
            sys.exit(0)
    return int(answer)


def download_song(song_url, song_title):
    """
    download song in song_title.mp3 format with youtube_dl from url song_url
    """
    import youtube_dl

    print("download " + song_url + " with youtubedl")
    outtmpl = song_title + ".%(ext)s"
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
    print(song_title + ".mp3 is ready")


def display_help():
    """
    help
    """
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
        version         : display versions of ytdlmusic and his dependencies
                        -> ytdlmusic version                         
        artist song     : display 5 choices from youtube with given search, then download the mp3 choosen by user
                        -> example : ytdlmusic "the beatles" "let it be"
        artist song auto: download mp3 of the first from youtube with given search
                        -> example : ytdlmusic "the beatles" "let it be" auto
        """
    print(help_txt)


def update():
    """
    update
    """
    prog = "pip3"
    if which(prog) is None:
        prog = "pip"
    print("try to update youtube-dl with " + prog)
    subprocess.check_call(
        [
            prog,
            "install",
            "--upgrade",
            "youtube-dl",
        ]
    )
    print("try to update youtube-search-python with " + prog)
    subprocess.check_call(
        [
            prog,
            "install",
            "--upgrade",
            "youtube-search-python",
        ]
    )
    print("try to update ytdlmusic with " + prog)
    subprocess.check_call(
        [
            prog,
            "install",
            "--upgrade",
            "ytdlmusic",
        ]
    )


if __name__ == "__main__":
    ytdlmusic()
