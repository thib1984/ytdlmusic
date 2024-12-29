"""
main class ytdlmusic
"""
import validators
import sys
import os
import re
from ytdlmusic.download import download_song
from ytdlmusic.print import print_error
from ytdlmusic.params import is_tag, is_batch, my_colored_emoji
from ytdlmusic.search import search
from ytdlmusic.choice import choice
from ytdlmusic.file import (
    determine_filename,
    determine_finame_from_tag,
)


def job(keywords):
    """
    principale use case
    auto : True if not interactive choice
    """
    try:
        if validators.url(keywords):
            print(
                my_colored_emoji(
                    "\U0001F50E", keywords + ' is an url : skip choice',
                    "green",
                )
            )
            filename = determine_filename(keywords, "temp")
            download_song(
                keywords,
                filename,
            )
            newfilename = determine_finame_from_tag(filename)
            os.rename(filename, newfilename)
            filename = newfilename
            print(my_colored_emoji("\u2705 ", filename + " is ready", "green"))
        else:    
            results = search(keywords)
            answer = choice(results)
            if answer != 0:
                item = results['entries'][answer - 1]
                filename = determine_filename(keywords, item["title"])
                download_song(
                    item["url"],
                    filename,
                )
                if is_tag():
                    newfilename = determine_finame_from_tag(filename)
                    os.rename(filename, newfilename)
                    filename = newfilename
                print(my_colored_emoji("\u2705 ", filename + " is ready", "green"))
    except Exception:
        print_error()
        if not is_batch():
            sys.exit(1)
