"""
ytdlmusic entrypoint
"""

import sys
import colorama
from ytdlmusic.ytdlmusic import job
from ytdlmusic.batch import launch_batch
from ytdlmusic.print import (
    print_error,
    print_version_ytdlmusic,
    print_version_dependencies,
    print_licence,
)
from ytdlmusic.params import (
    is_version,
    is_batch,
    param_batch,
    param_search,
)


def ytdlmusic():
    """
    ytdlmusic entrypoint
    """
    colorama.init()
    """
    entry point from ytdlmusic
    """
    try:
        if is_version():
            print_version_ytdlmusic()
            print_version_dependencies()
            print_licence()
        elif is_batch():
            launch_batch(param_batch())
        else:
            job(param_search())
        sys.exit(0)
    except Exception:
        print_error()
        sys.exit(1)
