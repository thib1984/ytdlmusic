"""
file utils scripts
"""


import os
import re
from shutil import which


def determine_filename(artist, song):
    """
    correct filename to escape special characters with '_'
    and force lower case from artist and song
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
    return file_name
