# 🎵 ytdlmusic

`ytdlmusic` is a command-line program to search and download music files from YouTube without use browser.
This package is directly available from [pypi](https://pypi.org/project/ytdlmusic/)

# :warning: Disclaimer

It may be illegal to download restricted content with this software, depending on the law in your country.

This package use two very important dependencies :

- [yt_dlp](https://pypi.org/project/yt_dlp/), a fork from [youtube-dl](https://github.com/ytdl-org/youtube-dl)
- [youtube-search-python](https://pypi.org/project/youtube-search-python/)

# 💫 How use **ytdlmusic**

`ytdlmusic [KEY WORDS]`

![demo_1](https://user-images.githubusercontent.com/45128847/137580908-ce3f1b17-a2b3-4530-bc90-df00fbaf1cfc.gif)

# 💫 How use **ytdlmusic** in batch mode

You can use a command to loop in a csv file, and download all MP3 files from it.

`ytdlmusic --batch path_file had_header sep columns_to_concatenate`

![demo_2](https://user-images.githubusercontent.com/45128847/137581058-e0cca29b-9ad1-472e-bbb0-4fce94b984a0.gif)

with csv file (for the demo's example)

```
song_column;artist_column;unused column
limujii;above;no
nomyn;awake;use
eyazttyzaeyz;zhhezhahkzaj;inexistant
scandinavianz;avalon;information
```

# 🚀 Other commands and flags

` ytdlmusic` , ` ytdlmusic --help` or ``ytdlmusic -h`` display help message.

`ytdlmusic --update` or `ytdlmusic -u` upgrade ytdlmusic.

`ytdlmusic --fullupdate` or `ytdlmusic -U` upgrade ytdlmusic and the dependencies yt-dlp and youtube-search-python.

`ytdlmusic --version` or `ytdlmusic -v` display version of ytdlmusic and the dependencies.

You can also add these flags to your commands (except for help and version) :

`--auto` or `-y` : Use auto mode: choose the first item for classic use, auto-accept other commands.

`--choices X` or `-N X` : Set the number of choices (default=5, min=1, max=10).

`--k` or `--keep` : Keep the YouTube video title for the filename.

`--t` or `--tag` : Use tags of the downloaded file to rename it.

`--m4a` or `-f` : Use M4A format.

`--ogg` or `-o` : Use OGG format.

`--Q` or `--quality` : Set quality to 320kbs instead of 256kbs for MP3 format.

`--quiet` or `-q` : Give less output.

`--verbose` or `-d` : Give more output.

`--nocolor` or `-n` : Disable colors and emojis in sysout.

# ⚙️ Install

See [this page](INSTALL.md)

# :question: FAQ

See [this page](FAQ.md)

# :construction_worker: Contribution

## For contributors

Go to [CONTRIBUTING.md](CONTRIBUTING.md). You have to read and accept this [Code of conduct](./CODE_OF_CONDUCT.md).

## Tanks to contributors

Thanks to contributors and dependencies authors :

- [albenquer](https://github.com/albenquer), [dlicois](https://github.com/dlicois) and [Jean-Phi Baconnais](https://github.com/jeanphibaconnais) for contributions !
- [Hitesh Kumar Saini](https://github.com/alexmercerind) for [youtube-search-python](https://github.com/alexmercerind/youtube-search-python)
- [yt-dlp](https://github.com/yt-dlp) for [yt-dlp](https://github.com/yt-dlp/yt-dlp)
- [devsnd](https://github.com/devsnd) for [tinytag](https://github.com/devsnd/tinytag)
- [avian2](https://github.com/avian2) for [unidecode](https://github.com/avian2/unidecode)
- [tartley](https://github.com/tartley) for [colorama](https://github.com/tartley/colorama)
- [vaultboy](https://pypi.org/user/vaultboy) for [termcolor](https://pypi.org/project/termcolor/)
- [Federico Carboni](https://github.com/FedericoCarboni) for [setup-ffmpeg](https://github.com/FedericoCarboni/setup-ffmpeg)
- [pypa](https://github.com/pypa) for [gh-action-pypi-publish](https://github.com/pypa/gh-action-pypi-publish)
- [elgohrf](https://github.com/elgohr) for [Github-Release-Action](https://github.com/elgohr/Github-Release-Action)

# :package: Changelog

See [this page](CHANGELOG.md)
# License

MIT License

Copyright (c) 2021 [thib1984](https://github.com/thib1984)

See [this page](LICENSE.txt) for details
