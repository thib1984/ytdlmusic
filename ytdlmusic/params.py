"""
ytdlmusic params scripts
"""

import sys
import re
from ytdlmusic.const import (
    FLAG_HELP_LONG,
    FLAG_VERSION_LONG,
    FLAG_UPDATE_LONG,
    FLAG_FULL_UPDATE_LONG,
    FLAG_AUTO_LONG,
    FLAG_VERSBOSE_LONG,
    FLAG_M4A_LONG,
    FLAG_OGG_LONG,
    FLAG_HELP_SHORT,
    FLAG_VERSION_SHORT,
    FLAG_UPDATE_SHORT,
    FLAG_FULL_UPDATE_SHORT,
    FLAG_AUTO_SHORT,
    FLAG_VERBOSE_SHORT,
    FLAG_M4A_SHORT,
    FLAG_OGG_SHORT,
    FLAG_BATCH_LONG,
    FLAG_NUMBER_LONG,
    FLAG_CHECK_LONG,
    FLAG_CHECK_SHORT,
    FLAG_CHECKALL_LONG,
    FLAG_CHECKALL_SHORT,
    FLAG_QUIET_SHORT,
    FLAG_QUIET_LONG,
    FLAG_QUALITY_SHORT,
    FLAG_QUALITY_LONG,
    FLAG_KEEP_SHORT,
    FLAG_KEEP_LONG,
    OPTION_FORMAT,
    LONG_OPTION_FORMAT,
    SHORT_OPTION_FORMAT,
)

option_list = [
    FLAG_HELP_LONG,
    FLAG_VERSION_LONG,
    FLAG_UPDATE_LONG,
    FLAG_FULL_UPDATE_LONG,
    FLAG_AUTO_LONG,
    FLAG_VERSBOSE_LONG,
    FLAG_M4A_LONG,
    FLAG_OGG_LONG,
    FLAG_CHECK_LONG,
    FLAG_CHECKALL_LONG,
    FLAG_QUIET_LONG,
    FLAG_QUALITY_LONG,
    FLAG_KEEP_LONG,
    FLAG_NUMBER_LONG,
]


option_list_light = [
    FLAG_HELP_SHORT,
    FLAG_VERSION_SHORT,
    FLAG_UPDATE_SHORT,
    FLAG_FULL_UPDATE_SHORT,
    FLAG_AUTO_SHORT,
    FLAG_VERBOSE_SHORT,
    FLAG_M4A_SHORT,
    FLAG_OGG_SHORT,
    FLAG_CHECK_SHORT,
    FLAG_CHECKALL_SHORT,
    FLAG_QUIET_SHORT,
    FLAG_QUALITY_SHORT,
    FLAG_KEEP_SHORT,
]


def check_flags():
    """
    verify the flags
    True if ok
    False otherwise
    """
    # option not recognized
    for i in sys.argv:
        if not check_param(i):
            return False
    if is_number() and (
        not param_number().isnumeric()
        or int(param_number()) < 1
        or int(param_number()) > 10
    ):
        print("the flag --n=" + param_number() + " is not valid")
        return False
    return True


def check_order_param_and_flags():
    """
    verify order of flags and params
    True if ok
    False otherwise
    """
    one_param = False
    for i in range(1, len(sys.argv)):
        if not sys.argv[i].startswith("-"):
            one_param = True
        if one_param and sys.argv[i].startswith("-"):
            print("the flags must be set before [ARTIST] and [SONG]")
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
        and not sysargv.startswith(FLAG_BATCH_LONG)
        and not sysargv.startswith(FLAG_NUMBER_LONG)
    ):
        return bad_options(sysargv)
    if re.search(SHORT_OPTION_FORMAT, sysargv):
        for k in range(1, len(sysargv)):
            element = sysargv[k]
            if "^-.*" + element + ".*" not in option_list_light:
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
    if not is_artist():
        print("Missing artist")
        return False
    if not is_song():
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


def is_quiet():
    """
    Return True if flag --quiet, False otherwise
    """
    return FLAG_QUIET_LONG in sys.argv or [
        i
        for i in sys.argv
        if (
            re.search(FLAG_QUIET_SHORT, i)
            and re.search(SHORT_OPTION_FORMAT, i)
        )
    ]


def is_quality():
    """
    Return True if flag --quality, False otherwise
    """
    return FLAG_QUALITY_LONG in sys.argv or [
        i
        for i in sys.argv
        if (
            re.search(FLAG_QUALITY_SHORT, i)
            and re.search(SHORT_OPTION_FORMAT, i)
        )
    ]


def is_verbose():
    """
    Return True if flag --verbose, False otherwise
    """
    return FLAG_VERSBOSE_LONG in sys.argv or [
        i
        for i in sys.argv
        if (
            re.search(FLAG_VERBOSE_SHORT, i)
            and re.search(SHORT_OPTION_FORMAT, i)
        )
    ]


def is_check():
    """
    Return True if flag --check, False otherwise
    """
    return FLAG_CHECK_LONG in sys.argv or [
        i
        for i in sys.argv
        if (
            re.search(FLAG_CHECK_SHORT, i)
            and re.search(SHORT_OPTION_FORMAT, i)
        )
    ]


def is_check_all():
    """
    Return True if flag --check, False otherwise
    """
    return FLAG_CHECKALL_LONG in sys.argv or [
        i
        for i in sys.argv
        if (
            re.search(FLAG_CHECKALL_SHORT, i)
            and re.search(SHORT_OPTION_FORMAT, i)
        )
    ]


def is_auto():
    """
    Return True if flag --auto, False otherwise
    """
    return FLAG_AUTO_LONG in sys.argv or [
        i
        for i in sys.argv
        if (
            re.search(FLAG_AUTO_SHORT, i)
            and re.search(SHORT_OPTION_FORMAT, i)
        )
    ]


def is_m4a():
    """
    Return True if flag --m4a, False otherwise
    """
    return FLAG_M4A_LONG in sys.argv or [
        i
        for i in sys.argv
        if (
            re.search(FLAG_M4A_SHORT, i)
            and re.search(SHORT_OPTION_FORMAT, i)
        )
    ]


def is_keep():
    """
    Return True if flag --ogg, False otherwise
    """
    return FLAG_KEEP_LONG in sys.argv or [
        i
        for i in sys.argv
        if (
            re.search(FLAG_KEEP_SHORT, i)
            and re.search(SHORT_OPTION_FORMAT, i)
        )
    ]


def is_ogg():
    """
    Return True if flag --ogg, False otherwise
    """
    return FLAG_OGG_LONG in sys.argv or [
        i
        for i in sys.argv
        if (
            re.search(FLAG_OGG_SHORT, i)
            and re.search(SHORT_OPTION_FORMAT, i)
        )
    ]


def is_help():
    """
    Return True if flag --help, False otherwise
    """
    return FLAG_HELP_LONG in sys.argv or [
        i
        for i in sys.argv
        if (
            re.search(FLAG_HELP_SHORT, i)
            and re.search(SHORT_OPTION_FORMAT, i)
        )
    ]


def is_version():
    """
    Return True if flag --version, False otherwise
    """
    return FLAG_VERSION_LONG in sys.argv or [
        i
        for i in sys.argv
        if (
            re.search(FLAG_VERSION_SHORT, i)
            and re.search(SHORT_OPTION_FORMAT, i)
        )
    ]


def is_update():
    """
    Return True if flag --update, False otherwise
    """
    return FLAG_UPDATE_LONG in sys.argv or [
        i
        for i in sys.argv
        if (
            re.search(FLAG_UPDATE_SHORT, i)
            and re.search(SHORT_OPTION_FORMAT, i)
        )
    ]


def is_fullupdate():
    """
    Return True if flag --full-update, False otherwise
    """
    return FLAG_FULL_UPDATE_LONG in sys.argv or [
        i
        for i in sys.argv
        if (
            re.search(FLAG_FULL_UPDATE_SHORT, i)
            and re.search(SHORT_OPTION_FORMAT, i)
        )
    ]


def is_batch():
    """
    Return True if flag --batch=, False otherwise
    """
    return [i for i in sys.argv if i.startswith(FLAG_BATCH_LONG)]


def is_number():
    """
    Return True if flag --n=, False otherwise
    """
    return [i for i in sys.argv if i.startswith(FLAG_NUMBER_LONG)]


def is_third_param():
    """
    Return True if number classic params >=3 (sys.argv excluded)
    """
    return not param_third() is None


def is_artist():
    """
    Return the artist from sys.argv
    """
    return not param_artist() is None


def is_song():
    """
    Return true if the song exists from sys.argv
    """
    return not param_song() is None


def param_artist():
    """
    Return true if the artist exists from sys.argv
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
        if i.startswith(FLAG_BATCH_LONG):
            return str.replace(i, FLAG_BATCH_LONG, "", 1).split("%")
    return ""


def param_number():
    """
    Return the number of param number param without "--number="
    """
    for i in sys.argv:
        if i.startswith(FLAG_NUMBER_LONG):
            return str.replace(i, FLAG_NUMBER_LONG, "", 1)
    return ""
