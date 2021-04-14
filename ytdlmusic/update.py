"""
update utils scripts
"""


import sys
import subprocess
from shutil import which
from ytdlmusic.print import print_error_update


def update():
    """
    update
    """
    while True:
        answer = input("update the ytdlmusic package [y/n] ? ")
        if answer == "y":
            break
        if answer == "n":
            sys.exit(0)
    try:
        prog = "pip3"
        if which(prog) is None:
            prog = "pip"
        update_ytdlmusic(prog)
    except Exception as err:
        print_error_update(err)


def fullupdate():
    """
    fullupdate
    """
    while True:
        answer = input(
            "update the ytdlmusic package and the dependencies [y/n] ? "
        )
        if answer == "y":
            break
        if answer == "n":
            sys.exit(0)
    try:
        prog = "pip3"
        if which(prog) is None:
            prog = "pip"
        update_ytdlmusic(prog)
        update_dependencies(prog)
    except Exception as err:
        print_error_update(err)


def update_dependencies(prog):
    """
    update of dependencies
    """
    print("try to update youtube-search-python with " + prog)
    subprocess.check_call(
        [
            prog,
            "install",
            "--upgrade",
            "youtube-search-python",
        ]
    )
    print("try to update youtube-dl with " + prog)
    subprocess.check_call(
        [
            prog,
            "install",
            "--upgrade",
            "youtube-dl",
        ]
    )


def update_ytdlmusic(prog):
    """
    update of ytdlmusic
    """
    print("try to update ytdlmusic with " + prog)
    subprocess.check_call(
        [
            prog,
            "install",
            "--upgrade",
            "ytdlmusic",
        ]
    )
