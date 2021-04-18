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

        The short options can ben combined into one (example : "-au" for "--auto --update")

        artist song         : display 5 choices from YouTube with given search, then download the MP3/OGG chosen by user
                            -> example : ytdlmusic "Rexlambo" "Stay With Me"
        -h, --help          : display this help (alone option)
                            -> ytdlmusic -h
        -v, --version       : display versions of ytdlmusic and his dependencies (alone option)
                            -> ytdlmusic -v                        
        -u, --update        : upgrade ytdlmusic
                            -> ytdlmusic -u   
        -U, --full-update   : upgrade youtube-dl, youtube-search-python and ytdlmusic
                            -> ytdlmusic -U 
        -a, --auto          : automatic mode (first choide for classic use, auto accept for other options)
                            -> example : ytdlmusic -a "Rexlambo" "Stay With Me"
                            -> example : ytdlmusic -a --update
        -f, --ogg           : force ogg extension even if ffmpeg is installed
                            -> example : ytdlmusic -f "Rexlambo" "Stay With Me"
        -d, --verbose       : verbose mode
                            -> example : ytdlmusic -d "Rexlambo" "Stay With Me"
                            -> example : ytdlmusic -du
        --batch=path_file%had_header%sep%artist_column%song_column  
                            : loop on a csv and call for each line `ytdlmusic artist song`
                            -> example : ytdlmusic --batch="~/test.csv"%False%,%1%2
                                #loop on csv file : ~/test.csv
                                #without header line the csv file
                                #coma separator
                                #artist on the first field
                                #song on the second field         
                            -> example : ytdlmusic --afd --batch="~/test.csv"%False%,%1%2
                                #same with auto-mode, force ogg and debug

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

PLATFORM_OS = """\
OS platform                   : $1"""

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

EXCEPTION_UPDATE = """\
Unexpected error during the update : $1
The update will could be finished at the restart of ytdlmusic.
Retest the update a second time."""

EXCEPTION_BATCH = """\
Unexpected error during the batch : $1
Verify the params of --batch."""

BUG_MESSSAGE = """\
You can also try  to manually upgrade ytdlmusic or the dependencies with 'pip(3) install --upgrade name_package'
If you reproduce the error : add the flag '--verbose' flag and open an issue at https://github.com/thib1984/ytdlmusic/issues with the complete log"""


NOT_INSTALLED = "NOT INSTALLED"
NOT_FOUND = "NOT FOUND"

FULL_UPDATE_YN = """\
Update the ytdlmusic package and the dependencies [y/n] ? """

UPDATE_YN = "Update the ytdlmusic package [y/n] ? "

TRY_UPDATE = "Try to update $1 with $2"

DEBUG_HEADER = "[debug] stack trace :"
