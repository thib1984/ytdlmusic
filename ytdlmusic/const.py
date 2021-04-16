"""
constants
"""


HELP_TXT = """\

    NAME
        ytdlmusic

    SYNOPSIS
        With ytdlmusic, you can download directly from YouTube music files in MP3/OGG format from your terminal, 
        without using your browser. By default, it will match your request with a selection of 5 results 
        with a brief summary to choose from or you can use auto mode to download automaticaly the first item.

        --help              : display this help
                            -> ytdlmusic --help
        --update            : upgrade ytdlmusic
                            -> ytdlmusic --update   
        --full-update       : upgrade youtube-dl, youtube-search-python and ytdlmusic
                            -> ytdlmusic --full-update                                                   
        --version           : display versions of ytdlmusic and his dependencies
                            -> ytdlmusic --version                         
        artist song         : display 5 choices from YouTube with given search, then download the MP3/OGG chosen by user
                            -> example : ytdlmusic "Rexlambo" "Stay With Me"
        --auto artist song  : download MP3/OGG of the first from YouTube with given search
                            -> example : ytdlmusic --auto "Rexlambo" "Stay With Me"

    Full documentation at: <https://github.com/thib1984/ytdlmusic>
    Report bugs to <https://github.com/thib1984/ytdlmusic/issues>
"""

VERSION_YTDLMUSIC = """\
ytdlmusic version             : $1"""

VERSION_DEPENDENCIES = """\
youtube-search-python version : $1
youtube-dl version            : $2
pip(3) version                : $3
Python version                : $4
ffmpeg                        : $5"""

LICENCE_TXT = """\

MIT Licence.
Copyright (c) 2021 thib1984.
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.

Written by Thibault Garçon.
"""

BAD_LAUNCH_TXT = """\
bad parameters for ytdlmusic
ytdlmusic --help for more information"""

EXCEPTION = """\
Unexpected error: $1"""

BUG_MESSSAGE = """\
try to upgrade with 'ytdlmusic update' or manually and retry.
if you reproduce the error after the update : you can open an issue at https://github.com/thib1984/ytdlmusic/issues with this log"""

EXCEPTION_UPDATE = """\
error during the update : $1
the update will could be finished at the restart of ytdlmusic
"""

BUG_UPDATE_MESSSAGE = """\
try to upgrade with 'ytdlmusic update' or manually and retry.
retest the update a second time. If you reproduce the error : you can open an issue at https://github.com/thib1984/ytdlmusic/issues with this log"""

NOT_INSTALLED = "NOT INSTALLED"

FULL_UPDATE_YN = """\
update the ytdlmusic package and the dependencies [y/n] ? """

UPDATE_YN = "update the ytdlmusic package [y/n] ? "

TRY_UPDATE = "try to update $1 with $2"
