"""
version utils scripts
"""


import sys
from shutil import which
import pkg_resources
from ytdlmusic.const import NOT_INSTALLED


def python_version():
    """
    obtain python version
    """
    try:
        pythonversion = "".join(sys.version.splitlines())
    except Exception:
        pythonversion = NOT_INSTALLED
    return pythonversion


def binary_version(binary):
    """
    obtain binary version
    """
    if which(binary) is None:
        binary_version = NOT_INSTALLED
    else:
        binary_version = which(binary)
    return binary_version


def pip_package_version(package):
    """
    obtain package version
    """
    try:
        version = pkg_resources.get_distribution(package).version
    except Exception:
        version = NOT_INSTALLED
    return version


def pip_package_version_of_double(package1, package2):
    """
    obtain package version of package1 if exists, package in other case
    """
    try:
        version = pkg_resources.get_distribution(package1).version
    except Exception:
        try:
            version = pkg_resources.get_distribution(package2).version
        except Exception:
            version = NOT_INSTALLED

    return version
