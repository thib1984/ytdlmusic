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
from ytdlmusic.batch import batch, launch_batch
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
    check_options,
    no_param,
    check_classic_params,
)


def ytdlmusic():
    """
    entry point from ytdlmusic
    """
    try:
        if no_param():
            print_no_param()
            sys.exit(0)
        if not check_options():
            print_bad_launch()
            sys.exit(1)
        elif is_help():
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
            if not check_classic_params():
                print_bad_launch()
                sys.exit(1)
            job(param_author(), param_song())
        sys.exit(0)
    except Exception as err:
        print_error(err)
        sys.exit(1)
