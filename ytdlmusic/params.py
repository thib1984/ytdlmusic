"""
ytdlmusic params scripts
"""

import sys
import re


option_list = [
    "--help",
    "--version",
    "--update",
    "--full-update",
    "--auto",
    "--verbose",
    "--ogg",
]

option_list_light = [
    "h",
    "v",
    "u",
    "U",
    "a",
    "d",
    "f",
]

BATCH_OPTION = "--batch="
LONG_OPTION_FORMAT = "^--[A-Za-z]+"
SHORT_OPTION_FORMAT = "^-[A-Za-z]+$"
OPTION_FORMAT = "^-(-[A-Za-z]+|[A-Za-z]+$)"


def check_options():
    """
    is_launch_ok for ytdlmusic
    """
    # option not recognized
    for i in sys.argv:
        if not check_param(i):
            print(i)
            return False
    return True


def check_param(sysargv):
    """
    test_param
    """
    if sysargv.startswith("-") and not re.search(
        OPTION_FORMAT, sysargv
    ):
        return bad_options(sysargv)
    if (
        re.search(LONG_OPTION_FORMAT, sysargv)
        and sysargv not in option_list
        and not sysargv.startswith(BATCH_OPTION)
    ):
        return bad_options(sysargv)
    if re.search(SHORT_OPTION_FORMAT, sysargv):
        for k in range(1, len(sysargv)):
            element = sysargv[k]
            if element not in option_list_light:
                return bad_options(sysargv)
    return True


def bad_options(i):
    """
    return false and print message
    """
    print("Not recognized option : " + i)
    return False


def check_classic_params():
    """
    check the classic params for classic use
    """
    # too classic parameters
    if is_third_param():
        print("Max only 2 classic params")
        return False
    if not is_author() or not is_song:
        print("Missing author")
        return False
    if not is_song:
        print("Missing song")
        return False
    return True


def no_param():
    """
    True if no param in sys.argv (except sys.argv(0)), False other
    """
    if len(sys.argv) == 1:
        return True
    return False


def number_options():
    """
    Return number of options (except sys.argv(0)) in sys.argv
    """
    j = 0
    for element in range(1, len(sys.argv)):
        i = sys.argv[element]
        if re.search(SHORT_OPTION_FORMAT, i):
            j = j + len(i) - 1
        else:
            j = j + 1
    return j


def is_verbose():
    """
    Return True if flag --verbose, False otherwise
    """
    return "--verbose" in sys.argv or [
        i
        for i in sys.argv
        if (
            re.search("^-.*d.*", i)
            and re.search(SHORT_OPTION_FORMAT, i)
        )
    ]


def is_auto():
    """
    Return True if flag --auto, False otherwise
    """
    return "--auto" in sys.argv or [
        i
        for i in sys.argv
        if (
            re.search("^-.*a.*", i)
            and re.search(SHORT_OPTION_FORMAT, i)
        )
    ]


def is_ogg():
    """
    Return True if flag --ogg, False otherwise
    """
    return "--ogg" in sys.argv or [
        i
        for i in sys.argv
        if (
            re.search("^-.*f.*", i)
            and re.search(SHORT_OPTION_FORMAT, i)
        )
    ]


def is_help():
    """
    Return True if flag --help, False otherwise
    """
    return "--help" in sys.argv or [
        i
        for i in sys.argv
        if (
            re.search("^-.*h.*", i)
            and re.search(SHORT_OPTION_FORMAT, i)
        )
    ]


def is_version():
    """
    Return True if flag --version, False otherwise
    """
    return "--version" in sys.argv or [
        i
        for i in sys.argv
        if (
            re.search("^-.*v.*", i)
            and re.search(SHORT_OPTION_FORMAT, i)
        )
    ]


def is_update():
    """
    Return True if flag --update, False otherwise
    """
    return "--update" in sys.argv or [
        i
        for i in sys.argv
        if (
            re.search("^-.*u.*", i)
            and re.search(SHORT_OPTION_FORMAT, i)
        )
    ]


def is_fullupdate():
    """
    Return True if flag --full-update, False otherwise
    """
    return "--full-update" in sys.argv or [
        i
        for i in sys.argv
        if (
            re.search("^-.*U.*", i)
            and re.search(SHORT_OPTION_FORMAT, i)
        )
    ]


def is_batch():
    """
    Return True if flag --batch=, False otherwise
    """
    return [i for i in sys.argv if i.startswith(BATCH_OPTION)]


def is_third_param():
    """
    Return True if number classic params >=3 (sys.argv excluded)
    """
    return not param_third() is None


def is_author():
    """
    Return the author from sys.argv
    """
    return not param_author() is None


def is_song():
    """
    Return true if the song exists from sys.argv
    """
    return not param_song() is None


def param_author():
    """
    Return true if the author exists from sys.argv
    """
    j = 0
    for i in sys.argv:
        if not i.startswith("-"):
            j = j + 1
            if j == 2:
                return i
    return None


def param_song():
    """
    Return the song from sys.argv
    """
    j = 0
    for i in sys.argv:
        if not i.startswith("-"):
            j = j + 1
            if j == 3:
                return i
    return None


def param_third():
    """
    Return the third classic param from sys.argv
    """
    j = 0
    for i in sys.argv:
        if not i.startswith("-"):
            j = j + 1
            if j == 4:
                return i
    return None


def param_batch():
    """
    Return the list of batch param without "--batch="
    """
    for i in sys.argv:
        if i.startswith(BATCH_OPTION):
            return str.replace(i, BATCH_OPTION, "", 1).split("%")
    return ""
