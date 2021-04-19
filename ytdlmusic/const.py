"""
string constants
"""


HELP_TXT = """\

    NAME
        ytdlmusic

    SYNOPSIS
        ytdlmusic is a command-line program to search and download music files from YouTube without use browser. 
    
    USAGE : ytdlmusic [OPTION]... [ARTIST] [SONG]

        By default, ytdlmusic searches Youtube for "[ARTIST] [SONG]" and displays the top five result and their 
        description. The selected result is downloaded in your current directory. The format used is MP3 if 
        ffmpeg is installed, OGG otherwise. The filename is [ARTIST]_[SONG].mp3/ogg to lowercase, and special 
        characters replaced by '_'. 

        Options are played in this order:
        -h, --help          : print this help text and exit
        -u, --update        : upgrade this program to latest version and exit
        -U, --full-update   : upgrade this program and the dependencies to latest version and exit
        -v, --version       : print program version and exit                     
        -y, --auto          : use automatic default choices 
        -f, --ogg           : use ogg extension even if ffmpeg is installed
        -d, --verbose       : give more output
        --batch=<path>%<bool_h>%<s>%<art_col>%<song_col>  
                            : batch mode, loop on a <path> csv file with an header <bool_h>, with separator 
                            <sep>, artist on colum number <art_col>, song aon column number <song_col>

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
If you reproduce the error : add the flag '--verbose' flag and open an issue at 
https://github.com/thib1984/ytdlmusic/issues with the complete log"""


NOT_INSTALLED = "NOT INSTALLED"
NOT_FOUND = "NOT FOUND"

FULL_UPDATE_YN = """\
Update the ytdlmusic package and the dependencies [Y/n] ? """

UPDATE_YN = "Update the ytdlmusic package [Y/n] ? "

TRY_UPDATE = "Try to update $1 with $2"

DEBUG_HEADER = "[debug] stack trace :"

CHOICE_RESULT_QUESTION = "Which (1-$1, 0 to exit, 1 by default) ? "

FLAG_HELP_LONG = "--help"
FLAG_VERSION_LONG = "--version"
FLAG_UPDATE_LONG = "--update"
FLAG_FULL_UPDATE_LONG = "--full-update"
FLAG_AUTO_LONG = "--auto"
FLAG_VERSBOSE_LONG = "--verbose"
FLAG_UPDATE_OGG = "--ogg"
FLAG_HELP_SHORT = "^-.*h.*"
FLAG_VERSION_SHORT = "^-.*v.*"
FLAG_UPDATE_SHORT = "^-.*u.*"
FLAG_FULL_UPDATE_SHORT = "^-.*U.*"
FLAG_AUTO_SHORT = "^-.*y.*"
FLAG_VERBOSE_SHORT = "^-.*d.*"
FLAG_OGG_SHORT = "^-.*f.*"
FLAG_BATCH_LONG = "--batch="
