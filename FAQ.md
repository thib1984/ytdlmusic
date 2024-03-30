

# The commands indicated in this README don't work for me! Why?

The  syntax of the commands can be changed between versions, run ``ytdlmusic`` and read the help message. 

# I would like an MP3 format but I only get an M4A format, why?

The ``ffmpeg`` package is required for the MP3 conversion. Install it and retry to launch ytdlmusic.


# With the ``--tag`` option, my filenames keep the YouTube title format. Why?

The ``ffmpeg`` package is required for the tag conversion. Install it and retry to launch ytdlmusic.
# What are the compatibilities with Python, pip, yt-dlp and youtube-search-python?

When an new version is released, it is compatible with the last Python version in the branches 3.6 to 3.10, on the release date. It's also compatible with the last versions of dependencies, on the release date.



# When I try to update yt-dlp with ``yt-dlp -U``, I obtain an error message in my debian/ubuntu!

If you obtain the following message: 

```
It looks like you installed yt-dlp with a package manager, pip, setup.py or a tarball. Please use that to update.
```

instead of 

```
yt-dlp: error: yt-dlp's self-update mechanism is disabled on Debian.
Please update yt-dlp using apt(8).
See https://packages.debian.org/sid/yt-dlp for the latest packaged version.
```

No panic! You have just downloaded a newer version of yt-dlp which is not in apt. When a new version of yt-dlp will be released in apt, you will download it automatically with ``sudo apt upgrade``. If you want to retrieve the previous version, ``sudo apt remove yt-dlp && sudo apt install yt-dlp``

# I get an error about ``_requesthandler.py line 22`` when I try to use ytdlmusic

Sorry... You should update Python to 3.6 version or more. youtube-search-python doesn't seem to be compatible with Python 3.5 or less. Now, ytdlmusic package checks the Python version during the installation process.

# Have you tested your package?

Before a new version of ytdlmusic is published, it is checked in an [automatic job](https://github.com/thib1984/ytdlmusic/actions/workflows/publish.yml), with the last versions of pip, yt-dlp and youtube-search-python, and also in the last versions of Python in the four branches 3.6 to 3.10.

Each night, [another automatic job](https://github.com/thib1984/ytdlmusic/actions/workflows/test_published_release.yml) checks the actual package with last versions of dependencies and Pythons 3.6 to 3.10. So if a regression appears, the author of ytdlmusic received  an automatic mail to warn it.*

*_These tests are executed with GitHub Actions on an Ubuntu 20.04 image. Tests are also run on macOS._
