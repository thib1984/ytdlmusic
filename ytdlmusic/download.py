"""
download scripts
"""
from termcolor import colored
from ytdlmusic.params import (
    is_verbose,
    is_quiet,
    is_m4a,
    is_ogg,
    is_quality,
)
from ytdlmusic.file import extension
from ytdlmusic.file import name_without_extension, is_ffmpeg_installed
from ytdlmusic.log import print_debug

try:
    import youtube_dl
except ImportError:
    print_debug("youtubde_dl import problem")


def download_song(song_url, filename):
    """
    download song with youtube-dl
    in filename
    from url song_url
    """

    print(
        colored("download " + song_url + " with youtubedl", "green")
    )

    # m4a
    opts = {
        "outtmpl": name_without_extension(filename) + ".%(ext)s",
        "format": "m4a/best",
    }

    if extension(filename) == ".mp3":
        opts["format"] = "bestaudio/best"
        opts["postprocessors"] = [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "256",
            },
            {"key": "FFmpegMetadata"},
        ]
        if is_quality():
            opts.get("postprocessors")[0]["preferredquality"] = "320"

    if extension(filename) == ".ogg":
        opts["format"] = "bestaudio/best"
        opts["postprocessors"] = [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "vorbis",
            },
            {"key": "FFmpegMetadata"},
        ]

    if is_verbose():
        opts["verbose"] = "True"
        print_debug("debug youtube-dl is activated")
    if not is_quiet():
        print("start youtube-dl operation")
    elif is_quiet():
        opts["quiet"] = True
        opts["no_warnings"] = True
    with youtube_dl.YoutubeDL(opts) as ydl:
        ydl.extract_info(song_url, download=True)
    if not is_quiet():
        print("end youtube-dl operation")
    if not is_ffmpeg_installed() and not is_m4a() and not is_ogg():
        print(
            colored(
                "[warning] If you want MP3/OGG format, install ffmpeg.",
                "yellow",
            )
        )
        print(
            colored(
                "[warning] To disable this message activate -f",
                "yellow",
            )
        )
