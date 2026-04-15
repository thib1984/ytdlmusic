"""
ytdlmusic entrypoint
"""
import static_ffmpeg
import sys
import colorama
from ytdlmusic.ytdlmusic import job
from ytdlmusic.batch import launch_batch
from ytdlmusic.print import (
    print_error
)
from ytdlmusic.params import (
    is_batch,
    param_batch,
    param_search,
)


def ytdlmusic():
    """
    ytdlmusic entrypoint
    """
    colorama.init()
    static_ffmpeg.add_paths()
    """
    entry point from ytdlmusic
    """
    try:
        if is_batch():
            launch_batch(param_batch())
        else:
            job(param_search())
        sys.exit(0)
    except Exception:
        print_error()
        sys.exit(1)
