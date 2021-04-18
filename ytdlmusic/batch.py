import csv
import sys
from ytdlmusic.ytdlmusic import job
from ytdlmusic.print import print_error_batch
from ytdlmusic.params import is_verbose


def launch_batch(param):
    try:
        batch(
            param[0], param[1], param[2], int(param[3]), int(param[4])
        )
    except Exception as err:
        print_error_batch(err)
        sys.exit(1)


def launch_batch(param):
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
    with open(file_path, "r", encoding="utf-8") as csvfile:
        reader = csv.reader(
            csvfile, delimiter=separator, quotechar="|"
        )
        boolean_header = False
        if has_header == "True":
            boolean_header = True
        if boolean_header:
            next(reader, None)
        for row in reader:
            if is_verbose():
                print(
                    "ligne numero "
                    + str(reader.line_num)
                    + " en cours : "
                    + str(row)
                )
            artist = row[artist_column - 1]
            song = row[song_column - 1]
            job(artist, song)
