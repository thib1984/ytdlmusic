"""
ytdlmusic scripts
"""

import sys
from ytdlmusic.ytdlmusic import job
from ytdlmusic.update import update, fullupdate
from ytdlmusic.print import (
    print_help,
    print_bad_launch,
    print_no_param,
    print_version_ytdlmusic,
    print_version_dependencies,
    print_licence,
    print_error_batch,
)
from ytdlmusic.batch import batch
from ytdlmusic.print import print_error
from ytdlmusic.params import (
    is_auto,
    is_fullupdate,
    is_help,
    is_update,
    is_version,
    is_batch,
    param_batch,
    is_author,
    is_song,
    param_author,
    param_song,
)


def ytdlmusic():
    """
    entry point from ytdlmusic
    """
    try:
        # special entries
        if len(sys.argv) == 1:
            print_no_param()
        elif len(sys.argv) == 2:
            if is_help():
                print_help()
            elif is_update():
                update()
            elif is_fullupdate():
                fullupdate()
            elif is_version():
                print_version_ytdlmusic()
                print_version_dependencies()
                print_licence()
            elif is_batch():
                launch_batch(param_batch())
            else:
                bad_launch()
        elif len(sys.argv) == 3:
            if is_auto() and is_batch():
                launch_batch(param_batch())
            elif is_song() and is_author():
                job(param_author(), param_song())
            else:
                bad_launch()
        elif len(sys.argv) == 4:
            if not is_auto:
                bad_launch()
            else:
                job(param_author(), param_song())
        else:
            bad_launch()
        sys.exit(0)
    except Exception as err:
        print_error(err)
        sys.exit(1)


def launch_batch(param):
    try:
        batch(
            param[0], param[1], param[2], int(param[3]), int(param[4])
        )
    except Exception as err:
        print_error_batch(err)
        sys.exit(1)


def bad_launch():
    print_bad_launch()
    sys.exit(1)


if __name__ == "__main__":
    ytdlmusic()
