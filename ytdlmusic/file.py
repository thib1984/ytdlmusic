"""
file utils scripts
"""


import os
import re
import pathlib
from shutil import which
from ytdlmusic.log import print_debug
from ytdlmusic.params import is_m4a, is_ogg, is_keep
from ytdlmusic.const import NOT_FOUND


def determine_filename(artist, song, title):
    """
    correct filename to escape special characters with '_'
    and force lower case from artist and song
    """
    if is_m4a() or not is_ffmpeg_installed():
        ext = ".m4a"
    elif is_ogg():
        ext = ".ogg"
    else:
        ext = ".mp3"
    print_debug("extension used : " + ext)
    filename = (
        re.sub("(\\W+)", "_", artist + "_" + song).lower() + ext
    )
    if is_keep():
        print_debug(" file name deduced from YouTube")
        filename = re.sub("(\\W+)", "_", title).lower() + ext
    print_debug("filename found " + filename)
    if os.path.exists(filename):
        # loop to find non existent filename
        print_debug(filename + " already exists")
        i = 0
        while True:
            i += 1
            tmp = (
                name_without_extension(filename) + "_" + str(i) + ext
            )
            if not os.path.exists(tmp):
                filename = tmp
                break
            print_debug(tmp + " already exists")
    print_debug(filename + " will be used as filename")
    return filename


def name_without_extension(filename):
    """
    return the extension of filename with point
    """
    return pathlib.Path(filename).stem


def extension(filename):
    """
    return the filename without the extension
    """
    return pathlib.Path(filename).suffix


def binary_path(binary):
    """
    obtain 'binary' patha
    """
    if which(binary) is None:
        path = NOT_FOUND
    else:
        path = which(binary)
    return path


def is_ffmpeg_installed():
    """
    test if ffmpeg is installed
    """
    return is_binary_installed("ffmpeg")


def is_binary_installed(binary):
    """
    test if binary is installed
    """
    return which(binary) is not None
