"""
main class ytdlmusic
"""

import sys
from ytdlmusic.search import search
from ytdlmusic.choice import choice
from ytdlmusic.file import determine_filename
from ytdlmusic.download import download_song
from ytdlmusic.print import print_error


def job(artist, song):
    """
    principale use case
    auto : True if not interactive choice
    """
    try:
        results = search(artist, song)
        answer = choice(results)
        if answer != 0:
            item = results.result()["result"][answer - 1]
            filename = determine_filename(artist, song, item["title"])
            download_song(
                item["link"],
                filename,
            )
    except Exception as err:
        print_error(err)
        sys.exit(1)
