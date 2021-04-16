"""
print utils scripts
"""

from ytdlmusic.version import (
    binary_version,
    python_version,
    pip_package_version,
    pip_package_version_of_double,
)
from ytdlmusic.const import (
    HELP_TXT,
    LICENCE_TXT,
    BAD_LAUNCH_TXT,
    EXCEPTION,
    BUG_MESSSAGE,
    EXCEPTION_UPDATE,
    BUG_UPDATE_MESSSAGE,
    VERSION_YTDLMUSIC,
    VERSION_DEPENDENCIES,
    TRY_UPDATE,
)


def replace_all(text, dic):
    """
    replace in text with dic paramaters
    """
    for i, j in dic.items():
        text = text.replace(i, j)
    return text


def print_no_param():
    """
    print if no param
    """
    print_help()
    print("")
    print_licence()


def print_licence():
    """
    print licence
    """
    print_version_ytdlmusic()
    print(replace_all(LICENCE_TXT, {}))


def print_version_ytdlmusic():
    """
    print licence
    """
    print(
        replace_all(
            VERSION_YTDLMUSIC,
            {"$1": pip_package_version("ytdlmusic")},
        )
    )


def print_version_dependencies():
    """
    print licence
    """
    print(
        replace_all(
            VERSION_DEPENDENCIES,
            {
                "$1": pip_package_version("youtube-search-python"),
                "$2": pip_package_version("youtube-dl"),
                "$3": pip_package_version_of_double("pip3", "pip"),
                "$4": python_version(),
                "$5": binary_version("ffmpeg"),
            },
        )
    )


def print_help():
    """
    print help
    """
    print(replace_all(HELP_TXT, {}))


def print_bad_launch():
    """
    print bad launch
    """
    print(replace_all(BAD_LAUNCH_TXT, {}))


def print_error(err):
    """
    print generic error
    """
    print(replace_all(EXCEPTION, {"$1": str(err)}))
    print(replace_all(BUG_MESSSAGE, {}))


def print_error_update(err):
    """
    print generic error
    """
    print(replace_all(EXCEPTION_UPDATE, {"$1": str(err)}))
    print_version_ytdlmusic()
    print_version_dependencies()
    print(replace_all(BUG_UPDATE_MESSSAGE, {}))


def print_try_update(package, prog):
    """
    print try update
    """
    print(replace_all(TRY_UPDATE, {"$1": package, "$2": prog}))
