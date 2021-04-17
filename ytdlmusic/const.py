"""
string constants
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
    
    INFORMATION
        It may be illegal to download restricted content with this software, depending on the law in your country.                            

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

Written by thib1984.
"""

BAD_LAUNCH_TXT = """\
Bad parameters for ytdlmusic.
ytdlmusic --help for more information"""

EXCEPTION = """\
Unexpected error: $1
Try to upgrade with 'ytdlmusic update' or even 'ytdlmusic full-update' and retry."""

BUG_MESSSAGE = """\
You can also try  to manually upgrade ytdlmusic or the dependencies with 'pip(3) install --upgrade name_package'.
If you reproduce the error : you can open an issue at https://github.com/thib1984/ytdlmusic/issues with this log."""

EXCEPTION_UPDATE = """\
Unexpected error during the update : $1
The update will could be finished at the restart of ytdlmusic.
Retest the update a second time."""

BUG_UPDATE_MESSSAGE = """\ 
you can also try  to manually upgrade ytdlmusic or the dependencies with 'pip(3) install --upgrade name_package'
If you reproduce the error : you can open an issue at https://github.com/thib1984/ytdlmusic/issues with this log"""

NOT_INSTALLED = "NOT INSTALLED"

FULL_UPDATE_YN = """\
Update the ytdlmusic package and the dependencies [y/n] ? """

UPDATE_YN = "Update the ytdlmusic package [y/n] ? "

TRY_UPDATE = "Try to update $1 with $2"
