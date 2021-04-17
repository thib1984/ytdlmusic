import csv
from ytdlmusic.ytdlmusic import job


def batch(
    file_path, has_header, separator, artist_column, song_column, auto
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
            job(artist, song, auto)
