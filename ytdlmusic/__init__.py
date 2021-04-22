"""
ytdlmusic scripts
"""

import sys
from ytdlmusic.ytdlmusic import job
from ytdlmusic.update import update, fullupdate, check_list_packages
from ytdlmusic.batch import launch_batch
from ytdlmusic.print import (
    print_error,
    print_help,
    print_bad_launch,
    print_no_param,
    print_version_ytdlmusic,
    print_version_dependencies,
    print_licence,
)
from ytdlmusic.params import (
    is_fullupdate,
    is_help,
    is_update,
    is_version,
    is_batch,
    param_batch,
    param_artist,
    param_song,
    check_flags,
    no_param,
    check_classic_params,
    check_order_param_and_flags,
    is_check,
    is_check_all,
)


def ytdlmusic():
    """
    entry point from ytdlmusic
    """
    try:
        if no_param():
            print_no_param()
            sys.exit(0)
        if not check_flags() or not check_order_param_and_flags():
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
        elif is_check():
            check_list_packages(["ytdlmusic"])
        elif is_check_all():
            check_list_packages(
                ["ytdlmusic", "youtube-search-python", "youtube-dl"]
            )
        elif is_batch():
            launch_batch(param_batch())
        # classic use case
        else:
            if not check_classic_params():
                print_bad_launch()
                sys.exit(1)
            job(param_artist(), param_song())
        sys.exit(0)
    except Exception as err:
        print_error(err)
        sys.exit(1)
