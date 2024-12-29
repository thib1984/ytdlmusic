"""
print utils scripts
"""

import traceback


from ytdlmusic.version import (
    python_version,
    pip_package_version,
    pip_package_version_of_double,
    platform_version,
)
from ytdlmusic.const import (
    LICENCE_TXT,
    EXCEPTION,
    BUG_MESSSAGE,
    EXCEPTION_BATCH,
    VERSION_YTDLMUSIC,
    VERSION_DEPENDENCIES,
    PLATFORM_OS,
    DEBUG_HEADER,
    BUG_MESSSAGE_DEBUG,
)
from ytdlmusic.file import binary_path
from ytdlmusic.params import is_verbose, my_colored


def replace_all(text, dic):
    """
    replace in param text with dict paramaters
    example : dic = { "cat": "dog", "bird": "rabbit"}
    text = "This is my cat and this is my bird."
    -> "This is my dog and this is my rabbit."
    """
    for i, j in dic.items():
        text = text.replace(i, j)
    return text


def print_licence():
    """
    print MIT Licence + Copyright + No WARRANTY + author
    """
    print(LICENCE_TXT)


def print_version_ytdlmusic():
    """
    print version of ytdlmusic
    """
    print(
        replace_all(
            VERSION_YTDLMUSIC,
            {"$1": pip_package_version("ytdlmusic")},
        )
    )


def print_version_dependencies():
    """
    print version of dependencies
    """
    print(
        replace_all(
            VERSION_DEPENDENCIES,
            {
                "$1": pip_package_version("yt-dlp"),
                "$2": binary_path("ffmpeg"),
            },
        )
    )
    print(replace_all(PLATFORM_OS, {"$1": platform_version()}))


def print_error():
    """
    print the error message with additional informations
    """
    if is_verbose():
        print(my_colored(DEBUG_HEADER, "yellow"))
        print(my_colored(traceback.format_exc(), "yellow"))
    print(my_colored(EXCEPTION, "red"))
    print_addtional_informations()

def print_error_batch():
    """
    print the error message with additional informations
    """
    if is_verbose():
        print(my_colored(DEBUG_HEADER, "yellow"))
        print(my_colored(traceback.format_exc(), "yellow"))
    print(my_colored(EXCEPTION_BATCH, "red"))
    print_addtional_informations()


def print_addtional_informations():
    """
    print footer informations
    """
    if is_verbose():
        print_version_ytdlmusic()
        print_version_dependencies()
        print(my_colored(BUG_MESSSAGE_DEBUG, "yellow"))
    else:
        print(my_colored(BUG_MESSSAGE, "yellow"))


    


