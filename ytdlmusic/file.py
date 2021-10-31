"""
file utils scripts
"""


import os
import re
import pathlib
from shutil import which
import unidecode
from ytdlmusic.log import print_debug
from ytdlmusic.params import is_m4a, is_ogg, is_keep, is_tag, my_colored
from ytdlmusic.const import NOT_FOUND
from ytdlmusic.tag import obtain_tags


def unicode_and_trim(text_to_translate):
    """
    transcode text to unicode, without special characters, and trim spaces before after
    """
    print_debug("raw format : " + text_to_translate)
    step_1 = re.sub("(\\W+)", " ", text_to_translate)
    step_2 = re.sub(" +", " ", step_1)
    step_3 = re.sub("^ ", "", step_2)
    step_4 = re.sub(" $", "", step_3)
    transcode_text = unidecode.unidecode(step_4)
    print_debug("unicode format : " + transcode_text)
    return transcode_text


def determine_filename(search, title):
    """
    determine inital filename
    """
    if is_m4a() or not is_ffmpeg_installed():
        ext = ".m4a"
    elif is_ogg():
        ext = ".ogg"
    else:
        ext = ".mp3"
    print_debug("extension used : " + ext)

    if is_keep():
        print_debug("file name will be deduced from YouTube : ")
        return find_unique_name(unicode_and_trim(title) + ext)
    if is_tag():
        print_debug(
            "temporary file name will be deduced from YouTube : "
        )
        return find_unique_name(unicode_and_trim(title) + ext)
    print_debug("file name will be deduced key words : ")
    return find_unique_name(unicode_and_trim(search) + ext)


def find_unique_name(filename):
    """
    determine final filename to escape already existing filename
    """
    print_debug("initial filename found : " + filename)
    if os.path.exists(filename):
        # loop to find non existent filename
        print_debug(filename + " already exists")
        i = 0
        while True:
            i += 1
            tmp = (
                name_without_extension(filename)
                + "_"
                + str(i)
                + extension(filename)
            )
            if not os.path.exists(tmp):
                filename = tmp
                break
            print_debug(tmp + " already exists")
    print_debug("final available filename found : " + filename)
    return filename


def determine_finame_from_tag(filename):
    """
    determine final filename from metatags
    """
    print(my_colored("filename conversion with metadata", "green"))
    nom_genere = ""
    if not is_ffmpeg_installed() or is_m4a():
        print(
            my_colored(
                "[warning] If you want use metadata tags, install ffmpeg and use MP3 or OGG format.",
                "yellow",
            )
        )
        print(my_colored("[warning] keep the YouTube format.", "yellow"))
        return filename

    title, artist, album = obtain_tags(filename)

    if not title or not artist:
        print(
            my_colored("[warning] Not enough tags information", "yellow")
        )
        return filename
    if album:
        nom_genere = (
            unicode_and_trim(artist)
            + " - "
            + unicode_and_trim(album)
            + " - "
            + unicode_and_trim(title)
        )
    else:
        nom_genere = (
            unicode_and_trim(artist) + " - " + unicode_and_trim(title)
        )
    print_debug("file name deduced from metadata : ")
    return find_unique_name(nom_genere + extension(filename))


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
