## Description

``ytdlmusic`` is a command-line program to search and download music files from YouTube without use browser. 

## Information

This package is directly available from [pypi](https://pypi.org/project/ytdlmusic/)

It may be illegal to download restricted content with this software, depending on the law in your country.

This package use two very important dependencies :
- [yt_dlp](https://pypi.org/project/yt_dlp/) a fork from [youtube-search-python](https://pypi.org/project/youtube-search-python/)
- [youtube-search-python](https://pypi.org/project/youtube-search-python/)

## Installation prerequisites

- Install Python 3 for your system
- Install pip3* for your system
- Install ffmpeg for your system if you want to use MP3/OGG format (M4A otherwise)

*_Install pip instead of pip3, if pip3 does not exist for your OS_
## Installation

``pip3 install ytdlmusic``*

*_Use pip instead of pip3, if pip3 does not exist_

## Use

``ytdlmusic [KEY WORDS]``

![demo_1](https://user-images.githubusercontent.com/45128847/137580908-ce3f1b17-a2b3-4530-bc90-df00fbaf1cfc.gif)

## Batch

You can use a command to loop in a csv file, and download all MP3 files from it. 

`` ytdlmusic --batch path_file had_header sep columns_to_concatenate ``*

![demo_2](https://user-images.githubusercontent.com/45128847/137581058-e0cca29b-9ad1-472e-bbb0-4fce94b984a0.gif)

with csv file 
```
song_column;artist_column;unused column
limujii;above;no
nomyn;awake;use
eyazttyzaeyz;zhhezhahkzaj;inexistant
scandinavianz;avalon;information
```
## Other commands

`` ytdlmusic`` , `` ytdlmusic --help`` or `` ytdlmusic -h ` display help message.

`` ytdlmusic --update `` or `` ytdlmusic -u `` upgrade ytdlmusic.

`` ytdlmusic --fullupdate `` or `` ytdlmusic -U `` upgrade ytdlmusic and the dependencies yt-dlp and youtube-search-python.

`` ytdlmusic --version `` or `` ytdlmusic -v `` display version of ytdlmusic and the dependencies.

## Other flags

You can also add these flags to your commands (except for help and version) :


`` --auto `` or `` -y `` : Use auto mode: choose the first item for classic use, auto-accept other commands.

`` --choices X `` or `` -n X `` : Set the number of choices (default=5, min=1, max=10).

`` --k `` or `` --keep `` : Keep the YouTube video title for the filename.

`` --t `` or `` --tag `` : Use tags of the downloaded file to rename it.

`` --m4a `` or `` -f `` : Use M4A format.

`` --ogg `` or `` -o `` : Use OGG format.

`` --Q `` or `` --quality `` : Set quality to 320kbs instead of 256kbs for MP3 format.

`` --quiet `` or `` -q `` : Give less output.

`` --verbose `` or `` -d `` : Give more output.
## Local install to develop

```
git clone https://github.com/thib1984/ytdlmusic.git
cd ytdlmusic 
#work!
pip3 install . #to build
ytdlmusic "Rexlambo Stay With Me"  #to retest
pip3 uninstall ytdlmusic #to properly uninstall the dev version
``` 
 
## FAQ

### The commands indicated in this README don't work for me! Why?

The  syntax of the commands can be changed between versions, run ``ytdlmusic`` and read the help message. 

### I would like an MP3 format but I only get an M4A format, why?

The ``ffmpeg`` package is required for the MP3 conversion. Install it and retry to launch ytdlmusic.


### With the ``--tag`` option, my filenames keep the YouTube title format. Why?

The ``ffmpeg`` package is required for the tag conversion. Install it and retry to launch ytdlmusic.
### What are the compatibilities with Python, pip, yt-dlp and youtube-search-python?

When an new version is released, it is compatible with the last Python version in the branches 3.6 to 3.10, on the release date. It's also compatible with the last versions of dependencies, on the release date.



### When I try to update yt-dlp with ``yt-dlp -U``, I obtain an error message in my debian/ubuntu!

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

### I get an error about ``_requesthandler.py line 22`` when I try to use ytdlmusic

Sorry... You should update Python to 3.6 version or more. youtube-search-python doesn't seem to be compatible with Python 3.5 or less. Now, ytdlmusic package checks the Python version during the installation process.

### Have you tested your package?

Before a new version of ytdlmusic is published, it is checked in an [automatic job](https://github.com/thib1984/ytdlmusic/actions/workflows/publish.yml), with the last versions of pip, yt-dlp and youtube-search-python, and also in the last versions of Python in the four branches 3.6 to 3.10.

Each night, [another automatic job](https://github.com/thib1984/ytdlmusic/actions/workflows/test_published_release.yml) checks the actual package with last versions of dependencies and Pythons 3.6 to 3.10. So if a regression appears, the author of ytdlmusic received  an automatic mail to warn it.*

*_These tests are executed with GitHub Actions on an Ubuntu 20.04 image. Tests are also run on macOS and Windows images (only very last Python version)._
## Thanks

Thanks to contributors and dependencies authors :

- [albenquer](https://github.com/albenquer) and [dlicois](https://github.com/dlicois) for contributions!
- [Hitesh Kumar Saini](https://github.com/alexmercerind) for [youtube-search-python](https://github.com/alexmercerind/youtube-search-python)
- [yt-dlp](https://github.com/yt-dlp) for [yt-dlp](https://github.com/yt-dlp/yt-dlp)
- [devsnd](https://github.com/devsnd) for [tinytag](https://github.com/devsnd/tinytag)
- [avian2](https://github.com/avian2) for [unidecode](https://github.com/avian2/unidecode)
- [tartley](https://github.com/tartley) for [colorama](https://github.com/tartley/colorama)
- [vaultboy](https://pypi.org/user/vaultboy) for [termcolor](https://pypi.org/project/termcolor/)
- [Federico Carboni](https://github.com/FedericoCarboni) for [setup-ffmpeg](https://github.com/FedericoCarboni/setup-ffmpeg)
- [pypa](https://github.com/pypa) for [gh-action-pypi-publish](https://github.com/pypa/gh-action-pypi-publish)
- [elgohrf](https://github.com/elgohr) for [Github-Release-Action](https://github.com/elgohr/Github-Release-Action)
## License

MIT License

Copyright (c) 2021 [thib1984](https://github.com/thib1984)


