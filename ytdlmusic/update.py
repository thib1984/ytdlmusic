"""
update utils scripts
"""


import sys
import subprocess
from ytdlmusic.print import (
    print_error_update,
    print_try_update,
)
from ytdlmusic.const import (
    UPDATE_YN,
    FULL_UPDATE_YN,
)
from ytdlmusic.params import is_verbose, is_auto
from ytdlmusic.file import is_binary_installed
from ytdlmusic.log import print_debug


def update():
    """
    update ytdlmusic
    """
    if not is_auto():
        answer = input(UPDATE_YN)
        if answer.lower() not in ["y", ""]:
            print("Abort.")
            sys.exit(1)
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
        answer = input(FULL_UPDATE_YN)
        if answer.lower() not in ["y", ""]:
            print("Abort.")
            sys.exit(1)
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
    params = [
        prog,
        "install",
        "--quiet",
        "--upgrade",
        package,
    ]
    if is_verbose():
        params.remove("--quiet")
        print_debug("install process : ")

    subprocess.check_call(params)
    print("Update ok")


def pip3_or_pip():
    """
    obtain pip3 if installed, otherwise pip if installed, otherwise,
    print_error and exit
    """
    if is_binary_installed("pip3"):
        return "pip3"
    if is_binary_installed("pip"):
        return "pip"
    print_error_update("Not pip por pip3 package")
    sys.exit(1)
