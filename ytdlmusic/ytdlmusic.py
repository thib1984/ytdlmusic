"""
main class ytdlmusic
"""

import sys
from ytdlmusic.search import search
from ytdlmusic.choice import choice
from ytdlmusic.file import determine_filename
from ytdlmusic.download import download_song
from ytdlmusic.print import print_error


def job(artist, song, auto):
    """
    principale use case
    auto : True if not interactive choice
    """
    try:
        results = search(artist, song)
        answer = choice(results, auto)
        file_name = determine_filename(artist, song)
        u_choice = results.result()["result"][answer - 1]
        download_song(
            u_choice["link"],
            file_name,
        )
    except Exception as err:
        print_error(err)
        sys.exit(1)
