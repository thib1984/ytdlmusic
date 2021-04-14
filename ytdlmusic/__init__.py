"""
ytdlmusic scripts
"""

import sys
from ytdlmusic.version import version
from ytdlmusic.ytdlmusic import job
from ytdlmusic.update import update, fullupdate
from ytdlmusic.print import display_help, print_bad_launch
from ytdlmusic.print import print_error


def ytdlmusic():
    """
    entry point from ytdlmusic
    """
    try:
        # special entries
        if len(sys.argv) == 1:
            display_help()
        elif len(sys.argv) == 2:
            if sys.argv[1] == "--help":
                display_help()
                sys.exit(0)

            if sys.argv[1] == "--update":
                update()
                sys.exit(0)

            if sys.argv[1] == "--full-update":
                fullupdate()
                sys.exit(0)

            if sys.argv[1] == "--version":
                version()
                sys.exit(0)

            if sys.argv[1].startswith("--"):
                print_bad_launch()
                sys.exit(1)

            print_bad_launch()
            sys.exit(1)

        elif len(sys.argv) == 3:
            if sys.argv[1].startswith("--") or sys.argv[2].startswith(
                "--"
            ):
                print_bad_launch()
                sys.exit(1)
            else:
                job(sys.argv[1], sys.argv[2], False)
                sys.exit(0)
        elif len(sys.argv) == 4:
            if not sys.argv[1].startswith("--auto"):
                print_bad_launch()
                sys.exit(1)
            else:
                job(sys.argv[2], sys.argv[3], True)
                sys.exit(0)
        else:
            print_bad_launch()
            sys.exit(1)
    except Exception as err:
        print_error(err)
        sys.exit(1)


if __name__ == "__main__":
    ytdlmusic()
