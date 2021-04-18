"""
ytdlmusic params scripts
"""

import sys


option_list_alone = [
    "--help",
    "--version",
]

option_list_others = [
    "--update",
    "--full-update",
    "--auto",
    "--verbose",
    "--ogg",
]

BATCH_OPTION = "--batch="


def is_good_launch():
    """
    is_launch_ok for ytdlmusic
    """
    if no_param():
        return True
    # too classic parameters
    if is_third_param():
        print("Max only 2 classic params")
        return False
    # option not recognized
    for i in sys.argv:
        if (
            i.startswith("--")
            and not i.startswith(BATCH_OPTION)
            and i not in option_list_alone
            and i not in option_list_others
        ):
            print("Not recognized param option : " + i)
            return False
    # option not alone
    if (had_alone_option()) and (
        number_options() > 1 or (is_author() or is_song())
    ):
        print(
            "Options "
            + str(option_list_alone)
            + " will be given alone"
        )
        return False
    # batch and clasic param
    if is_batch() and (is_author() or is_song()):
        print("For --batch option do not give classic params")
        return False
    if (
        not is_batch()
        and not is_version()
        and not is_help()
        and not is_fullupdate()
        and not is_update()
        and (not is_author() or not is_song())
    ):
        print("For param options given you shoud give classic params")
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
    return len(sys.argv) - 1


def is_verbose():
    """
    Return True if flag --verbose, False otherwise
    """
    return "--verbose" in sys.argv


def is_auto():
    """
    Return True if flag --auto, False otherwise
    """
    return "--auto" in sys.argv


def is_ogg():
    """
    Return True if flag --ogg, False otherwise
    """
    return "--ogg" in sys.argv


def is_help():
    """
    Return True if flag --help, False otherwise
    """
    return "--help" in sys.argv


def is_version():
    """
    Return True if flag --version, False otherwise
    """
    return "--version" in sys.argv


def is_update():
    """
    Return True if flag --update, False otherwise
    """
    return "--update" in sys.argv


def is_fullupdate():
    """
    Return True if flag --full-update, False otherwise
    """
    return "--full-update" in sys.argv


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
        if not i.startswith("--"):
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
        if not i.startswith("--"):
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
        if not i.startswith("--"):
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


def had_alone_option():
    """
    Return True if one or more param should be alone
    """
    for i in sys.argv:
        if i in option_list_alone:
            return True
    return False
