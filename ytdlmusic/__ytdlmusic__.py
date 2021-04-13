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

    if len(sys.argv) == 2 and sys.argv[1] == "full-update":
        fullupdate()
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
        "try to upgrade with 'ytdlmusic update' or manually and retry."
    )
    print(
        "if you reproduce the error after the update : you can open an issue at https://github.com/thib1984/ytdlmusic/issues with this log"
    )


def print_error_update(err):
    """
    print generic error
    """
    print("Unexpected error:", err)

    version()
    print(
        "if you reproduce the error : you can open an issue at https://github.com/thib1984/ytdlmusic/issues with this log"
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
    except Exception:
        ytdlmusicversion = "NON INSTALLE"
    try:
        ytsearchpythonversion = pkg_resources.get_distribution(
            "youtube-search-python"
        ).version
    except Exception:
        ytsearchpythonversion = "NON INSTALLE"
    try:
        youtubedlversion = pkg_resources.get_distribution(
            "youtube-dl"
        ).version
    except Exception:
        youtubedlversion = "NON INSTALLE"
    try:
        pipversion = pkg_resources.get_distribution("pip3").version
    except Exception:
        try:
            pipversion = pkg_resources.get_distribution("pip").version
        except Exception:
            pipversion = "NON INSTALLE"
    try:
        pythonversion = "".join(sys.version.splitlines())
    except Exception:
        pythonversion = "NON INSTALLE"
    if which("ffmpeg") is None:
        ffmpeg_binary = "NON INSTALLE"
    else:
        ffmpeg_binary = which("ffmpeg")
    print("ytdlmusic version             : " + ytdlmusicversion)
    print("youtube-search-python version : " + ytsearchpythonversion)
    print("youtube-dl version            : " + youtubedlversion)
    print("pip(3) version                : " + pipversion)
    print("python version                : " + pythonversion)
    print("ffmpeg                        : " + ffmpeg_binary)


def determine_filename(artist, song):
    """
    correct filename to escape special characters
    """
    file_name = re.sub(
        "(\\W+)", "_", artist.lower() + "_" + song.lower()
    )
    if which("ffmpeg") is None:
        ext = ".ogg"
    else:
        ext = ".mp3"
    if os.path.exists(file_name + ext):
        i = 0
        while True:
            i = i + 1
            file_name_tmp = file_name + "_" + str(i)
            if not os.path.exists(file_name_tmp + ext):
                file_name = file_name_tmp
                break
    print("future filename is : " + file_name + ext)
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
    download song in song_title.mp3/ogg format with youtube_dl from url song_url
    """
    import youtube_dl

    print("download " + song_url + " with youtubedl")
    if which("ffmpeg") is None:
        ext = ".ogg"
        outtmpl = song_title + ".ogg"
        ydl_opts = {"format": "bestaudio/best", "outtmpl": outtmpl}
    else:
        ext = ".mp3"
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
    if which("ffmpeg") is None:
        print(
            "warning : ogg was used. If you want mp3 format, install ffmpeg fo your system."
        )
    print(song_title + ext + " is ready")


def display_help():
    """
    help
    """
    help_txt = """\

    NAME
        ytdlmusic

    SYNOPSIS
       With ytdlmusic, you can download from youtube a mp3 or ogg music without use browser. 5 choices are available with small summary 
       to facilitate the choice. You can also use auto mode to download the first item. 

        help            : display this help
                        -> ytdlmusic help
        update          : try to upgrade ytdlmusic
                        -> ytdlmusic update   
        full-update     : try to upgrade youtube-dl, youtube-search-python and ytdlmusic
                        -> ytdlmusic update                                                   
        version         : display versions of ytdlmusic and his dependencies
                        -> ytdlmusic version                         
        artist song     : display 5 choices from youtube with given search, then download the mp3 or ogg choosen by user
                        -> example : ytdlmusic "the beatles" "let it be"
        artist song auto: download mp3 or ogg of the first from youtube with given search
                        -> example : ytdlmusic "the beatles" "let it be" auto
        """
    print(help_txt)


def update():
    """
    update
    """
    while True:
        answer = input("update the youtube-dl package [y/n] ? ")
        if answer == "y":
            break
        elif answer == "n":
            sys.exit(0)
    try:
        print("versions before update")
        version()
        prog = "pip3"
        if which(prog) is None:
            prog = "pip"
        update_ytdlmusic(prog)
        print("versions after update")
        version()
    except Exception as err:
        print_error(err)


def fullupdate():
    """
    fullupdate
    """
    while True:
        answer = input(
            "update the youtube-dl package and the dependencies [y/n] ? "
        )
        if answer == "y":
            break
        elif answer == "n":
            sys.exit(0)
    try:
        print("versions before update")
        version()
        prog = "pip3"
        if which(prog) is None:
            prog = "pip"
        update_ytdlmusic(prog)
        update_dependencies(prog)
        version()
    except Exception as err:
        print_error(err)


def update_dependencies(prog):
    """
    update of dependencies
    """
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
    print("versions after update")


def update_ytdlmusic(prog):
    """
    update of ytdlmusic
    """
    print("try to update youtube-dl with " + prog)
    subprocess.check_call(
        [
            prog,
            "install",
            "--upgrade",
            "youtube-dl",
        ]
    )


if __name__ == "__main__":
    ytdlmusic()
