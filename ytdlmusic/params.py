"""
ytdlmusic parameters and scripts
"""

import argparse
import sys
import platform
from termcolor import colored


def compute_args():
    """
    Function to handle argparse
    """
    my_parser = argparse.ArgumentParser(
        description="ytdlmusic is a command-line program to search and download music files from YouTube without using a browser.",
        epilog="""
        Full documentation is available at: <https://github.com/thib1984/ytdlmusic>.
        Report bugs to <https://github.com/thib1984/ytdlmusic/issues>.
        """
    )

    my_group = my_parser.add_mutually_exclusive_group(required=True)

    my_group.add_argument(
        "search",
        metavar="search",
        type=str,
        nargs="?",
        help="Specify the search term(s) to search on YouTube"
    )

    my_group.add_argument(
        "-v",
        "--version",
        action="store_true",
        help="Display ytdlmusic version number"
    )

    my_group.add_argument(
        "-b",
        "--batch",
        metavar=("path", "bool_h", "s", "num_col1+num_col2"),
        action="store",
        nargs=4,
        type=str,
        help="Run ytdlmusic in batch mode on a CSV <path> file with a header <bool_h>, a separator <s>, and concatenate columns of key words separated by \"+\""
    )

    my_parser.add_argument(
        "-y",
        "--auto",
        action="store_true",
        help="Automatically choose the first search result and accept subsequent prompts"
    )

    my_parser.add_argument(
        "-N",
        "--choices",
        metavar="X",
        action="store",
        type=int,
        default=5,
        choices=range(1, 11),
        help="Set the number of choices to display. The default value is 5, and the acceptable range is 1 to 10."
    )

    my_third_group = my_parser.add_mutually_exclusive_group()

    my_third_group.add_argument(
        "-f",
        "--m4a",
        action="store_true",
        help="Download files in M4A format"
    )

    my_third_group.add_argument(
        "-n",
        "--nocolor",
        action="store_true",
        help="Disable colors in output"
    )

    my_third_group.add_argument(
        "-o",
        "--ogg",
        action="store_true",
        help="Download files in OGG format"
    )

    my_third_group.add_argument(
        "-Q",
        "--quality",
        action="store_true",
        help="Set download quality to 320kbs instead of 256kbs for MP3 format"
    )

    my_fourth_group = my_parser.add_mutually_exclusive_group()

    my_fourth_group.add_argument(
        "-k",
        "--keep",
        action="store_true",
        help="Use the YouTube video title for the downloaded file name"
    )

    my_fourth_group.add_argument(
        "-t",
        "--tag",
        action="store_true",
        help="Use tags of the downloaded file to rename it"
    )

    my_fourth_group.add_argument(
        "--nocover",
        action="store_true",
        help="Do not add cover art (from youtube thumbnail) to file produced"
    )

    my_second_group = my_parser.add_mutually_exclusive_group()

    my_second_group.add_argument(
        "-d",
        "--verbose",
        action="store_true",
        help="Increase the amount of output shown",
    )
    my_second_group.add_argument(
        "-q",
        "--quiet",
        action="store_true",
        help="Decrease the amount of output shown",
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

def has_cover():
    return not compute_args().nocover

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
