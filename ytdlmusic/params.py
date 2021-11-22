"""
ytdlmusic params scripts
"""

import argparse

import sys
import platform
from termcolor import colored


def compute_args():
    """
    argparse gestion
    """
    my_parser = argparse.ArgumentParser(
        description="ytdlmusic is a command-line program to search and download music files from YouTube without use browser.",
        epilog="""
        Full documentation at: <https://github.com/thib1984/ytdlmusic>.
        Report bugs to <https://github.com/thib1984/ytdlmusic/issues>.
        """,
    )

    my_group = my_parser.add_mutually_exclusive_group(required=True)

    my_group.add_argument(
        "search",
        metavar="search",
        type=str,
        nargs="?",
        help="words to search in YouTube",
    )

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
        help="upgrade ytdlmusic, and the dependencies yt-dlp and youtube-search-python",
    )
    my_group.add_argument(
        "-b",
        "--batch",
        metavar=("path", "bool_h", "s", "num_col1+num_col2"),
        action="store",
        nargs=4,
        type=str,
        help="batch mode, loop on a <path> csv file with an header <bool_h>, a separator <s>, and key words from concatenates columns separated by \"+\"",
    )

    my_parser.add_argument(
        "-y",
        "--auto",
        action="store_true",
        help="choose the first item for classic use, auto-accept other commands",
    )
    my_parser.add_argument(
        "-N",
        "--choices",
        metavar="X",
        action="store",
        type=int,
        default=5,
        choices=range(1, 11),
        help="set the number X of choices (default=5, min=1, max=10)",
    )
    my_third_group = my_parser.add_mutually_exclusive_group()
    my_third_group.add_argument(
        "-f",
        "--m4a",
        action="store_true",
        help="use M4A format",
    )
    my_third_group.add_argument(
        "-n",
        "--nocolor",
        action="store_true",
        help="disable colors in sysout",
    )
    my_third_group.add_argument(
        "-o",
        "--ogg",
        action="store_true",
        help="use OGG format",
    )

    my_third_group.add_argument(
        "-Q",
        "--quality",
        action="store_true",
        help="set quality to 320kbs instead of 256kbs for MP3 format",
    )
    my_fourth_group = my_parser.add_mutually_exclusive_group()
    my_fourth_group.add_argument(
        "-k",
        "--keep",
        action="store_true",
        help="keep the YouTube video title for the filename",
    )
    my_fourth_group.add_argument(
        "-t",
        "--tag",
        action="store_true",
        help="use tags of the downloaded file to rename it",
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

    # if no parameter
    if len(sys.argv) == 1:
        my_parser.print_help()
        sys.exit(0)

    args = my_parser.parse_args()

    return args


def check_classic_params():
    """
    check the classic params for classic use
    """
    # too classic parameters
    if compute_args().search is None:
        print("Missing search")
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


def is_tag():
    """
    Return True if flag --ogg, False otherwise
    """
    return compute_args().tag


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
    Return True if flag --N=, False otherwise
    """
    return compute_args().choices


def param_search():
    """
    Return true if the search exists from sys.argv
    """
    return compute_args().search


def param_batch():
    """
    Return the list of batch param without "--batch="
    """
    return compute_args().batch


def param_number():
    """
    Return the number of param number param without "--number="
    """
    return compute_args().choices


def my_colored(message, color):
    if compute_args().nocolor:
        return message
    return colored(message,color)

def my_colored_emoji(emoji, message, color):
    if compute_args().nocolor:
        return message
    if platform.system().lower() in "windows":
        return colored(message,color)        
    return colored(emoji + " " + message,color)
