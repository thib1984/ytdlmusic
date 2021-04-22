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
    if not check_list_packages(["ytdlmusic"]):
        return
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

    if not check_list_packages(
        ["ytdlmusic", "youtube-search-python", "youtube-dl"]
    ):
        return
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
            "--quiet",
            "--upgrade",
            package,
        ]
        if is_verbose():
            params.remove("--quiet")
            print_debug("install process : ")

        subprocess.check_call(params)
        print("Update ok")
        return True
    except Exception as err:
        print_error_update_package(err)
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


def check_list_packages(list_of_search_packages):
    print("Search available update...")
    try:
        excludes = []
        update_available = False
        # list all packages without search update
        list_packages = str(
            subprocess.check_output([pip3_or_pip(), "list"]).decode(
                "utf-8"
            )
        )
        # if a package in paramater does not appear -> need update
        for package in list_of_search_packages:
            if package not in list_packages:
                print(package + " : not installed !")
                update_available = True
        # suppress all others packages not in parameter
        for line in list_packages.split("\n", 2)[2].splitlines():
            # print(line.split()[0])
            if line.split(" ")[0] not in list_of_search_packages:
                excludes.append("--exclude")
                excludes.append(line.split(" ")[0])

        # search outdated package in the small list obtained
        for line in str(
            subprocess.check_output(
                [pip3_or_pip(), "list", "--outdated"] + excludes
            ).decode("utf-8")
        ).splitlines():
            if line.split(" ")[0] in list_of_search_packages:
                print(
                    line.split()[0]
                    + " : available update : "
                    + line.split()[1]
                    + " -> "
                    + line.split()[2]
                )
                update_available = True
        if not update_available:
            print("No update available")
        else:
            print("Update available!")
        return update_available
    except Exception as err:
        print_debug(str(err))
        print(
            "Can't check if update available. You can relaunch with --verbose/-d for analysis."
        )
        return True