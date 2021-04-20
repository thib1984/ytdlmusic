"""
update utils scripts
"""


import sys
import subprocess
from ytdlmusic.print import (
    print_error_update,
    print_try_update,
    print_error_full_update,
    print_error_update_package,
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

    # try three updates
    boolean_ysp = update_pip_package(
        pip3_or_pip(), "youtube-search-python"
    )
    boolean_ytdl = update_pip_package(pip3_or_pip(), "youtube-dl")
    boolean_ytdlm = update_pip_package(pip3_or_pip(), "ytdlmusic")

    if boolean_ysp or boolean_ytdl or boolean_ytdlm:
        print_error_full_update()
        sys.exit(1)


def update_pip_package(prog, package):
    """
    update pip 'package' with 'prog'
    """
    try:
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
    except Exception as err:
        print_error_update_package(err)
        return False
    return True


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
