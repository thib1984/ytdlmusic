"""
string constants
"""


VERSION_YTDLMUSIC = """\
ytdlmusic version             : $1"""

VERSION_DEPENDENCIES = """\
youtube-search-python version : $1
yt-dlp version                : $2
pip(3) version                : $3
Python version                : $4
ffmpeg                        : $5"""

PLATFORM_OS = """\
OS platform                   : $1"""

LICENCE_TXT = """\

MIT Licence.
Copyright (c) 2021 thib1984.
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.

Written by thib1984.
"""

EXCEPTION = """\
[error] Unexpected error: Try to upgrade with 'ytdlmusic --update' or 'ytdlmusic --fullupdate'
and retry."""

EXCEPTION_UPDATE = """\
[error] Unexpected error during the update : The update will could be finished at the restart of ytdlmusic.
Retest the update a second time."""

EXCEPTION_BATCH = """\
[error] Unexpected error during the batch : Verify the params of --batch."""

BUG_MESSSAGE = """\
[warning] If you reproduce the error : add the flag '--verbose' flag and open an issue at
https://github.com/thib1984/ytdlmusic/issues with the complete log"""

BUG_MESSSAGE_DEBUG = """\
[warning] If you reproduce the error : open an issue at
https://github.com/thib1984/ytdlmusic/issues with this complete log"""

NOT_INSTALLED = "NOT INSTALLED"
NOT_FOUND = "NOT FOUND"

FULL_UPDATE_YN = """\
Update [Y/n] ? """

UPDATE_YN = "Update [Y/n] ? "

TRY_UPDATE = "Try to update $1 with $2"

DEBUG_HEADER = "[debug] stack trace :"

CHOICE_RESULT_QUESTION = "Which (1-$1, 0 to exit, 1 by default) ? "
