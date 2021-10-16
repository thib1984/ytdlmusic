"""
update utils scripts
"""


import sys
import subprocess
from ytdlmusic.print import (
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
    bool_result = update_pip_package(pip3_or_pip(), "ytdlmusic")
    if not bool_result:
        print_error_full_update()
        sys.exit(1)


def fullupdate():
    """
    update ytdlmusic, youtube-search-python, yt-dlp
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
    boolean_ytdl = update_pip_package(pip3_or_pip(), "yt-dlp")
    boolean_ytdlm = update_pip_package(pip3_or_pip(), "ytdlmusic")

    if not (boolean_ysp and boolean_ytdl and boolean_ytdlm):
        print_error_full_update()
        sys.exit(1)
    print("Full-update ok")


def update_pip_package(prog, package):
    """
    update pip 'package' with 'prog'
    """
    try:
        print_try_update(package, prog)
        params = [
            prog,
            "install",
            "--upgrade",
            package,
        ]
        print_debug("full trace pip")
        output = subprocess.check_output(params)
        # print(output)
        for line in output.decode("utf-8").split("\n"):
            if is_verbose():
                print(line.strip(" "))
            elif "Successfully" in line:
                print(line.strip(" "))
            elif (
                "Requirement already satisfied: " + package
            ) in line or (
                "Requirement already up-to-date: " + package
            ) in line:
                print(line.strip(" "))
        print("Update ok")
        return True
    except Exception:
        print_error_update_package()
        return False


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
