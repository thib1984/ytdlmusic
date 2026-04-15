"""
string constants
"""


EXCEPTION = """\
[error] Unexpected error: Try to upgrade ytdlmusic with 'pipx reinstall ytdlmusic --force' and retry."""

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

DEBUG_HEADER = "[debug] stack trace :"

CHOICE_RESULT_QUESTION = "Which (1-$1, 0 to exit, 1 by default) ? "
