"""
print utils scripts
"""

import traceback

from ytdlmusic.version import (
    binary_path,
    python_version,
    pip_package_version,
    pip_package_version_of_double,
    platform_version,
)
from ytdlmusic.const import (
    HELP_TXT,
    LICENCE_TXT,
    BAD_LAUNCH_TXT,
    EXCEPTION,
    BUG_MESSSAGE,
    EXCEPTION_UPDATE,
    EXCEPTION_BATCH,
    VERSION_YTDLMUSIC,
    VERSION_DEPENDENCIES,
    TRY_UPDATE,
    PLATFORM_OS,
    DEBUG_HEADER,
)
from ytdlmusic.params import is_verbose


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


def print_no_param():
    """
    if no params, display help + short_version + licence
    """
    print_help()
    print_version_ytdlmusic()
    print_version_dependencies()
    print_licence()


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
                "$1": pip_package_version("youtube-search-python"),
                "$2": pip_package_version("youtube-dl"),
                "$3": pip_package_version_of_double("pip3", "pip"),
                "$4": python_version(),
                "$5": binary_path("ffmpeg"),
            },
        )
    )
    print(replace_all(PLATFORM_OS, {"$1": platform_version()}))


def print_help():
    """
    print the help message
    """
    print(replace_all(HELP_TXT, {}))


def print_bad_launch():
    """
    print the bad launch message
    """
    print(replace_all(BAD_LAUNCH_TXT, {}))


def print_error(err):
    """
    print the error message with additional informations
    """
    if is_verbose():
        print(DEBUG_HEADER)
        traceback.print_exc()
    print(replace_all(EXCEPTION, {"$1": str(err)}))
    print_version_ytdlmusic()
    print_version_dependencies()
    print(BUG_MESSSAGE)


def print_error_update(err):
    """
    print the error message with additional informations
    """
    if is_verbose():
        print(DEBUG_HEADER)
        traceback.print_exc()
    print(replace_all(EXCEPTION_UPDATE, {"$1": str(err)}))
    print_version_ytdlmusic()
    print_version_dependencies()
    print(BUG_MESSSAGE)


def print_error_batch(err):
    """
    print the error message with additional informations
    """
    if is_verbose():
        print(DEBUG_HEADER)
        traceback.print_exc()
    print(replace_all(EXCEPTION_BATCH, {"$1": str(err)}))
    print_version_ytdlmusic()
    print_version_dependencies()
    print(BUG_MESSSAGE)


def print_try_update(package, prog):
    """
    print try update message
    """
    print(replace_all(TRY_UPDATE, {"$1": package, "$2": prog}))
