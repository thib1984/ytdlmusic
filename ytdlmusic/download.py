"""
download scripts
"""

from ytdlmusic.params import is_verbose, is_m4a
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

    print("download " + song_url + " with youtubedl")

    # m4a
    opts = {
        "quiet": True,
        "no_warnings": True,
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

    if extension(filename) == ".ogg":
        opts["format"] = "bestaudio/best"
        opts["postprocessors"] = [
            {"key": "FFmpegVideoConvertor", "preferedformat": "ogg"}
        ]

    if is_verbose():
        opts.pop("quiet")
        opts.pop("no_warnings")
        opts["verbose"] = "True"
        print_debug("debug youtube-dl : ")
    with youtube_dl.YoutubeDL(opts) as ydl:
        ydl.extract_info(song_url, download=True)
    if is_ffmpeg_installed() is None and not is_m4a():
        print(
            "[warning] M4A was used. If you want MP3/OGG format, install ffmpeg."
        )
    print(filename + " is ready")
