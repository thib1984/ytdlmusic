import csv
from ytdlmusic.ytdlmusic import job


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
    with open(file_path, "r") as csvfile:
        if has_header:
            reader = csv.reader(
                csvfile, delimiter=separator, quotechar="|"
            )
        next(reader, None)
        for row in reader:
            artist = row[artist_column - 1]
            song = row[song_column - 1]
            job(artist, song)
