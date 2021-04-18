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
]

batch_option = "--batch="


def is_good_launch():
    # too classic parameters
    if is_third_param():
        print("Max only 2 classic params")
        return False
    # option not recognized
    for i in sys.argv:
        if (
            i.startswith("--")
            and not i.startswith(batch_option)
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
    if len(sys.argv) == 1:
        return True
    return False


def number_options():
    j = -1
    for i in sys.argv:
        if not i.startswith(batch_option) or i in option_list:
            j = j + 1
    return j


def is_verbose():
    if "--verbose" in sys.argv:
        return True
    else:
        return False


def is_auto():
    if "--auto" in sys.argv:
        return True
    else:
        return False


def is_help():
    if "--help" in sys.argv:
        return True
    else:
        return False


def is_version():
    if "--version" in sys.argv:
        return True
    else:
        return False


def is_update():
    if "--update" in sys.argv:
        return True
    else:
        return False


def is_fullupdate():
    if "--full-update" in sys.argv:
        return True
    else:
        return False


def is_batch():
    if [i for i in sys.argv if i.startswith(batch_option)]:
        return True
    else:
        return False


def is_third_param():
    if param_third() == None:
        return False
    return True


def is_author():
    if param_author() == None:
        return False
    return True


def is_song():
    if param_song() == None:
        return False
    return True


def param_author():
    j = 0
    for i in sys.argv:
        if not i.startswith("--"):
            j = j + 1
            if j == 2:
                return i
    return None


def param_song():
    j = 0
    for i in sys.argv:
        if not i.startswith("--"):
            j = j + 1
            if j == 3:
                return i
    return None


def param_third():
    j = 0
    for i in sys.argv:
        if not i.startswith("--"):
            j = j + 1
            if j == 4:
                return i
    return None


def param_batch():
    for i in sys.argv:
        if i.startswith(batch_option):
            return str.replace(i, batch_option, "", 1).split("%")
    return ""


def had_alone_option():
    for i in sys.argv:
        if i in option_list_alone:
            return True
    return False