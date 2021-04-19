"""
ytdlmusic batch
"""

import csv
import sys
from ytdlmusic.ytdlmusic import job
from ytdlmusic.print import print_error_batch
from ytdlmusic.params import is_verbose
from ytdlmusic.log import print_debug


def launch_batch(param):
    """
    batch launcher
    """
    try:
        batch(
            param[0], param[1], param[2], int(param[3]), int(param[4])
        )
    except Exception as err:
        print_error_batch(err)
        sys.exit(1)


def batch(
    file_path, has_header, separator, artist_column, song_column
):
    """
    batch job
    """
    with open(file_path, "r", encoding="utf-8") as csvfile:
        reader = csv.reader(
            csvfile, delimiter=separator, quotechar="|"
        )
        if has_header == "True":
            next(reader, None)
        for row in reader:
            if is_verbose():
                print_debug(
                    str(reader.line_num) + " en cours : " + str(row)
                )
            job(row[artist_column - 1], row[song_column - 1])
