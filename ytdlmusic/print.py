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
       With ytdlmusic, you can download from youtube a mp3 or ogg music without use browser. 5 choices are available with small summary 
       to facilitate the choice. You can also use auto mode to download the first item. 

        --help              : display this help
                            -> ytdlmusic --help
        --update            : upgrade ytdlmusic
                            -> ytdlmusic --update   
        --full-update       : upgrade youtube-dl, youtube-search-python and ytdlmusic
                            -> ytdlmusic --full-update                                                   
        --version           : display versions of ytdlmusic and his dependencies
                            -> ytdlmusic --version                         
        artist song         : display 5 choices from youtube with given search, then download the mp3 or ogg choosen by user
                            -> example : ytdlmusic "the beatles" "let it be"
        --auto artist song  : download mp3 or ogg of the first from youtube with given search
                            -> example : ytdlmusic --auto "the beatles" "let it be"
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
        "Error during the update : the update will could be finished at the restart of ytdlmusic",
        err,
    )

    print(
        "Retest the update a second time. If you reproduce the error : you can open an issue at https://github.com/thib1984/ytdlmusic/issues with this log"
    )