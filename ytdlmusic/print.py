"""
print utils scripts
"""

from ytdlmusic.version import version


def display_help():
    """
    help
    """
    help_txt = """\

    NAME
        ytdlmusic

    SYNOPSIS
        With ytdlmusic, you can download directly from YouTube music files in MP3/OGG format from your terminal, 
        without using your browser. By default, it will match your request with a selection of 5 results 
        with a brief summary to choose from or you can use auto mode to download automaticaly the first item.

        --help              : display this help
                            -> ytdlmusic --help
        --update            : upgrade ytdlmusic
                            -> ytdlmusic --update   
        --full-update       : upgrade youtube-dl, youtube-search-python and ytdlmusic
                            -> ytdlmusic --full-update                                                   
        --version           : display versions of ytdlmusic and his dependencies
                            -> ytdlmusic --version                         
        artist song         : display 5 choices from YouTube with given search, then download the MP3/OGG chosen by user
                            -> example : ytdlmusic "Rexlambo" "Stay With Me"
        --auto artist song  : download MP3/OGG of the first from YouTube with given search
                            -> example : ytdlmusic --auto "Rexlambo" "Stay With Me"
        """
    print(help_txt)


def print_bad_launch():
    """
    print bad launch
    """
    print("bad parameters for ytdlmusic")
    print("ytdlmusic --help for more information")


def print_error(err):
    """
    print generic error
    """
    print("Unexpected error:", err)

    version()
    print(
        "try to upgrade with 'ytdlmusic update' or manually and retry."
    )
    print(
        "if you reproduce the error after the update : you can open an issue at https://github.com/thib1984/ytdlmusic/issues with this log"
    )


def print_error_update(err):
    """
    print generic error
    """
    print(
        "error during the update : the update will could be finished at the restart of ytdlmusic",
        err,
    )

    print(
        "retest the update a second time. If you reproduce the error : you can open an issue at https://github.com/thib1984/ytdlmusic/issues with this log"
    )
