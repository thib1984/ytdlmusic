"""
download scripts
"""

from shutil import which
from ytdlmusic.params import is_verbose


def download_song(song_url, song_title):
    """
    download song with youtube-dl
    in song_title.mp3/ogg
    from url song_url
    """
    import youtube_dl

    print("download " + song_url + " with youtubedl")
    if which("ffmpeg") is None:
        ext = ".ogg"
        outtmpl = song_title + ".ogg"
        ydl_opts = {
            "quiet": True,
            "format": "bestaudio/best",
            "outtmpl": outtmpl,
        }
    else:
        ext = ".mp3"
        outtmpl = song_title + ".%(ext)s"
        ydl_opts = {
            "quiet": True,
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

    if is_verbose():
        ydl_opts.pop("quiet")
        ydl_opts["verbose"] = "True"
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.extract_info(song_url, download=True)
    if which("ffmpeg") is None:
        print(
            "Warning : ogg was used. If you want MP3 format, install ffmpeg fo your system."
        )
    print(song_title + ext + " is ready")
