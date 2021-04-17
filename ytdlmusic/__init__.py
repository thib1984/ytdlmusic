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

            elif sys.argv[1].startswith("--batch="):
                batch_param = sys.argv[1]
                launch_batch(False, batch_param)

            else:
                bad_launch()

        elif len(sys.argv) == 3:
            if sys.argv[1].startswith("--") or sys.argv[2].startswith(
                "--"
            ):
                if (
                    sys.argv[1].startswith("--auto")
                    and sys.argv[2].startswith("--batch")
                ) or (
                    sys.argv[2].startswith("--auto")
                    and sys.argv[1].startswith("--batch")
                ):
                    if sys.argv[1].startswith("--auto"):
                        launch_batch(True, sys.argv[2])
                    else:
                        launch_batch(True, sys.argv[1])
                else:
                    bad_launch()
            else:
                job(sys.argv[1], sys.argv[2], False)
        elif len(sys.argv) == 4:
            if not sys.argv[1].startswith("--auto"):
                print_bad_launch()
                sys.exit(1)
            else:
                job(sys.argv[2], sys.argv[3], True)
        else:
            bad_launch()
        sys.exit(0)
    except Exception as err:
        print_error(err)
        sys.exit(1)


def launch_batch(auto, batch_param):
    try:
        list_param = str.replace(
            batch_param, "--batch=", "", 1
        ).split("%")
        if len(list_param) != 5:
            bad_launch()
        batch(
            list_param[0],
            list_param[1],
            list_param[2],
            int(list_param[3]),
            int(list_param[4]),
            auto,
        )
    except Exception as err:
        print_error_batch(err)
        sys.exit(1)


def bad_launch():
    print_bad_launch()
    sys.exit(1)


if __name__ == "__main__":
    ytdlmusic()
