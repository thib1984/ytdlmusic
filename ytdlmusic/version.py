"""
version utils scripts
"""


import sys
from shutil import which
import pkg_resources


def version():
    """
    search version
    """

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
