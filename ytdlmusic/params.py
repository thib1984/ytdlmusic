"""
ytdlmusic params scripts
"""

import argparse

import sys
import re


def compute_args():
    my_parser = argparse.ArgumentParser(
        description="ytdlmusic is a command-line program to search and download music files from YouTube without use browser.",
        epilog="""
        Full documentation at: <https://github.com/thib1984/ytdlmusic>.
        Report bugs to <https://github.com/thib1984/ytdlmusic/issues>.
        """,
    )

    my_third_group = my_parser.add_mutually_exclusive_group()
    my_third_group.add_argument(
        "-f",
        "--m4a",
        action="store_true",
        help="force use m4a format",
    )
    my_third_group.add_argument(
        "-o",
        "--ogg",
        action="store_true",
        help="force use m4a format",
    )

    my_parser.add_argument(
        "-Q",
        "--quality",
        action="store_true",
        help="set quality to 320kbs instead of 256kbs for mp3 format",
    )
    my_parser.add_argument(
        "-y",
        "--auto",
        action="store_true",
        help="auto-choose first item for classic use, auto-accept for other commands",
    )
    my_parser.add_argument(
        "-k",
        "--keep",
        action="store_true",
        help="keep the YouTube video title for the filename",
    )
    my_parser.add_argument(
        "-n",
        "--choices",
        metavar="X",
        action="store",
        type=int,
        default=5,
        choices=range(1, 5),
        help="set the number X of choices (default=5, min=1, max=10)",
    )

    my_group = my_parser.add_mutually_exclusive_group()
    my_group.add_argument(
        "-v",
        "--version",
        action="store_true",
        help="display ytdlmusic version",
    )
    my_group.add_argument(
        "-u",
        "--update",
        action="store_true",
        help="upgrade ytdlmusic",
    )
    my_group.add_argument(
        "-U",
        "--fullupdate",
        action="store_true",
        help="upgrade ytdlmusic, youtube-dl and youtube-search-python",
    )
    my_group.add_argument(
        "-b",
        "--batch",
        metavar=("path", "bool_h", "s", "art_col", "song_col"),
        action="store",
        nargs=5,
        type=str,
        help="batch mode, loop on a <path> csv file with an header <bool_h>, with separator <s>, artist on column number <art_col>, song on column number <song_col>",
    )

    my_group.add_argument(
        "artist", metavar="artist", type=str, nargs="?"
    )

    my_second_group = my_parser.add_mutually_exclusive_group()
    my_second_group.add_argument(
        "-d",
        "--verbose",
        action="store_true",
        help="give more output",
    )
    my_second_group.add_argument(
        "-q",
        "--quiet",
        action="store_true",
        help="give less output",
    )

    my_parser.add_argument(
        "song", metavar="song", type=str, nargs="?"
    )

    args = my_parser.parse_args()
    # if no parameter
    if len(sys.argv) == 1:
        my_parser.print_help()
        exit(0)

    return args


def check_classic_params():
    """
    check the classic params for classic use
    """
    # too classic parameters
    if compute_args().artist == None:
        print("Missing artist")
        return False
    if compute_args().song == None:
        print("Missing song")
        return False
    return True


def is_quiet():
    """
    Return True if flag --quiet, False otherwise
    """
    return compute_args().quiet


def is_quality():
    """
    Return True if flag --quality, False otherwise
    """
    return compute_args().quality


def is_verbose():
    """
    Return True if flag --verbose, False otherwise
    """
    return compute_args().verbose


def is_auto():
    """
    Return True if flag --auto, False otherwise
    """
    return compute_args().auto


def is_m4a():
    """
    Return True if flag --m4a, False otherwise
    """
    return compute_args().m4a


def is_keep():
    """
    Return True if flag --ogg, False otherwise
    """
    return compute_args().keep


def is_ogg():
    """
    Return True if flag --ogg, False otherwise
    """
    return compute_args().ogg


def is_version():
    """
    Return True if flag --version, False otherwise
    """
    return compute_args().version


def is_update():
    """
    Return True if flag --update, False otherwise
    """
    return compute_args().update


def is_fullupdate():
    """
    Return True if flag --fullupdate, False otherwise
    """
    return compute_args().fullupdate


def is_batch():
    """
    Return True if flag --batch=, False otherwise
    """
    return compute_args().batch


def is_number():
    """
    Return True if flag --n=, False otherwise
    """
    return compute_args().choices


def is_artist():
    """
    Return the artist from sys.argv
    """
    return not param_artist() is None


def is_song():
    """
    Return true if the song exists from sys.argv
    """
    return not param_song() is None


def param_artist():
    """
    Return true if the artist exists from sys.argv
    """
    return compute_args().artist


def param_song():
    """
    Return the song from sys.argv
    """
    return compute_args().song


def param_batch():
    """
    Return the list of batch param without "--batch="
    """
    return compute_args().batch.split("%")


def param_number():
    """
    Return the number of param number param without "--number="
    """
    return compute_args().choices
