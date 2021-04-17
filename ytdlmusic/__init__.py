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
)
from ytdlmusic.print import print_error


def ytdlmusic():
    """
    entry point from ytdlmusic
    """
    try:
        # special entries
        if len(sys.argv) == 1:
            print_no_param()
        elif len(sys.argv) == 2:
            if sys.argv[1] == "--help":
                print_help()

            elif sys.argv[1] == "--update":
                update()

            elif sys.argv[1] == "--full-update":
                fullupdate()

            elif sys.argv[1] == "--version":
                print_version_ytdlmusic()
                print_version_dependencies()
                print_licence()

            else:
                newmethod948()

        elif len(sys.argv) == 3:
            if sys.argv[1].startswith("--") or sys.argv[2].startswith(
                "--"
            ):
                newmethod948()
            else:
                job(sys.argv[1], sys.argv[2], False)
        elif len(sys.argv) == 4:
            if not sys.argv[1].startswith("--auto"):
                print_bad_launch()
                sys.exit(1)
            else:
                job(sys.argv[2], sys.argv[3], True)
        else:
            newmethod948()
        sys.exit(0)    
    except Exception as err:
        print_error(err)
        sys.exit(1)

def newmethod948():
    print_bad_launch()
    sys.exit(1)


if __name__ == "__main__":
    ytdlmusic()
