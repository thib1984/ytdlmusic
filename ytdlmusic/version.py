"""
version utils scripts
"""


import os
import sys
import platform
import pkg_resources
from ytdlmusic.const import NOT_INSTALLED, NOT_FOUND


def python_version():
    """
    obtain the Python version
    """
    try:
        pythonversion = "".join(sys.version.splitlines())
    except Exception:
        pythonversion = NOT_FOUND
    return pythonversion


def platform_version():
    """
    obtain platform version
    """
    try:
        platformversion = platform.system() + " " + platform.release()
    except Exception:
        platformversion = NOT_FOUND
    return platformversion


def pip_package_version(package):
    """
    Obtain pip 'package' version.
    Returns:
        - Version if the package is installed.
        - 'NOT_INSTALLED' if the package is not found.
        - Environment source (venv/pipx or system pip).
    """
    NOT_INSTALLED = 'NOT_INSTALLED'
    try:
        version = pkg_resources.get_distribution(package).version
        # Détecter si on est dans un environnement virtuel
        if hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix:
            source = 'venv/pipx'
        elif 'PIPX_HOME' in os.environ or 'PIPX_BIN_DIR' in os.environ:
            source = 'venv/pipx'
        else:
            source = 'pip'
    except Exception:
        version = NOT_INSTALLED
        source = 'unknown'
    
    return version+" ("+source+")"

def pip_package_version_of_double(package1, package2):
    """
    obtain package version of package1 if exists, package2 otherwise
    NOT_INSTALLED in no packages found
    """
    try:
        version = pkg_resources.get_distribution(package1).version
    except Exception:
        try:
            version = pkg_resources.get_distribution(package2).version
        except Exception:
            version = NOT_INSTALLED

    return version
