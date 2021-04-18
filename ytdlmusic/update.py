"""
update utils scripts
"""


import sys
import subprocess
from shutil import which
from ytdlmusic.print import print_error_update, print_try_update
from ytdlmusic.const import (
    UPDATE_YN,
    FULL_UPDATE_YN,
)
from ytdlmusic.params import is_verbose, is_auto


def update():
    """
    update ytdlmusic
    """
    if not is_auto():
        while True:
            answer = input(UPDATE_YN)
            if answer == "y":
                break
            if answer == "n":
                sys.exit(0)
    try:
        update_pip_package(pip3_or_pip(), "ytdlmusic")
    except Exception as err:
        print_error_update(err)
        sys.exit(1)


def fullupdate():
    """
    update ytdlmusic, youtube-search-python, youtube-dl
    """
    if not is_auto():
        while True:
            answer = input(FULL_UPDATE_YN)
            if answer == "y":
                break
            if answer == "n":
                sys.exit(0)
    try:
        update_pip_package(pip3_or_pip(), "ytdlmusic")
        update_pip_package(pip3_or_pip(), "youtube-search-python")
        update_pip_package(pip3_or_pip(), "youtube-dl")
    except Exception as err:
        print_error_update(err)
        sys.exit(1)


def update_pip_package(prog, package):
    """
    update pip 'package' with 'prog'
    """
    print_try_update(package, prog)
    if is_verbose():
        print("[debug] install process : ")
        subprocess.check_call(
            [
                prog,
                "install",
                "--upgrade",
                package,
            ]
        )
    else:
        subprocess.check_call(
            [
                prog,
                "install",
                "--quiet",
                "--upgrade",
                package,
            ]
        )
    print("Update ok")


def pip3_or_pip():
    """
    obtain pip3 if installed, otherwise pip if installed, otherwise,
    print_error and exit
    """
    prog = "pip3"
    if which(prog) is None:
        prog = "pip"
        if which(prog) is None:
            print_error_update("not pip por pip3 package")
            sys.exit(1)
    return prog
