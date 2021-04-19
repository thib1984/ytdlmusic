"""
log utils
"""

from ytdlmusic.params import is_verbose


def print_debug(message):
    """
    print "[debug] " + message only if --verbose
    """
    if is_verbose():
        print("[debug] " + message)
