import sys


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
    if [i for i in sys.argv if i.startswith("--batch=")]:
        return True
    else:
        return False


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


def param_batch():
    for i in sys.argv:
        if i.startswith("--batch="):
            return str.replace(i, "--batch=", "", 1).split("%")
    return ""