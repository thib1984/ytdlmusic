## Description

With ytdlmusic, you can download directly from YouTube music files in MP3/OGG format from your terminal, without using your browser. 
By default, it will match your request with a selection of 5 results with a brief summary to choose from or you can use auto mode to download automaticaly the first item.  

## Information

It may be illegal to download restricted content with this software, depending on the law in your country.

## Pipy

[Pipy link](https://pypi.org/project/ytdlmusic/)

## Prerequisites

- install Python 3 for your system
- install pip3 for your system or pip if pip3 does not exist
- optional : install ffmpeg for your system if you want to use MP3 format (OGG otherwise)

## Installation

``pip3 install ytdlmusic #or with pip if pip3 does not exist``

## Upgrade

`` ytdlmusic --update`` to upgrade ytdlmusic

`` ytdlmusic --full-update`` to upgrade ytdlmusic, youtube-dl and youtube-search-python

`` pip3 install --upgrade ytdlmusic #or with pip if pip3 does not exist`` to upgrade ytdlmusic directly with pip

`` pip3 install -ytdlmusic:x.x.x #to downgrade the app`` to downgrade ytdlmusic to a specified version with pip

`` pip3 install --upgrade youtube-dl`` to upgrade dependency youtube-dl

`` pip3 install --upgrade youtube-search-python`` to upgrade dependency youtube-search-python
## Use

``ytdlmusic "Rexlambo" "Stay With Me"``
will return a 5 items result list from which to chose which item to download, as a mp3/OGG file in the current directory

```
~$ ytdlmusic "the beattles" "Stay With Me"
artist : Rexlambo
song : Stay With Me
search "Rexlambo Stay With Me" with youtube-search-python
1
Rexlambo - stay with me
https://www.youtube.com/watch?v=LrED6SSFf-I
3:52 - 9,161 views
2
stay with me – Rexlambo (No Copyright Music)
https://www.youtube.com/watch?v=a0hkrjqpIOo
3:52 - 164,205 views
3
Rexlambo - stay with me
https://www.youtube.com/watch?v=TjATW8iAwa0
3:52 - 658 views
4
Rexlambo - stay with me
https://www.youtube.com/watch?v=0vnOMFmBUGk
3:52 - 831 views
5
Rexlambo - stay with me
https://www.youtube.com/watch?v=utrYsNKMcQc
3:52 - 549 views
Which (1-5, 0 to exit properly) ? 2
download https://www.youtube.com/watch?v=a0hkrjqpIOo with youtubedl
[youtube] a0hkrjqpIOo: Downloading webpage
[download] Destination: rexlambo_stay_with_me.webm
[download] 100% of 3.69MiB in 00:02
[ffmpeg] Destination: rexlambo_stay_with_me.mp3
Deleting original file rexlambo_stay_with_me.webm (pass -k to keep)
[ffmpeg] Adding metadata to 'rexlambo_stay_with_me.mp3'
rexlambo_stay_with_me.mp3 is ready
````

## use auto

``ytdlmusic --auto "Rexlambo" "Stay With Me"`` 
will dowmnload automaticaly the first item

```
~$ ytdlmusic --auto "the beattles" "Stay With Me"
artist : Rexlambo
song : Stay With Me
search "Rexlambo Stay With Me" with youtube-search-python
download https://www.youtube.com/watch?v=LrED6SSFf-I with youtubedl
[youtube] LrED6SSFf-I: Downloading webpage
[download] Destination: rexlambo_stay_with_me.webm
[download] 100% of 3.72MiB in 00:02
[ffmpeg] Destination: rexlambo_stay_with_me.mp3
Deleting original file rexlambo_stay_with_me.webm (pass -k to keep)
[ffmpeg] Adding metadata to 'rexlambo_stay_with_me.mp3'
rexlambo_stay_with_me.mp3 is ready
```

## Other commands

`` ytdlmusic`` to display help message, version, and license

`` ytdlmusic --help`` to display help message

`` ytdlmusic --update `` to upgrade ytdlmusic

`` ytdlmusic --full-update `` to upgrade ytdlmusic, youtube-dl and youtube-search-python

`` ytdlmusic --version `` to display version of ytdlmusic and dependencies
## Batch

You can use a script to loop in a csv file, and auto-download mp3 from it. ie: 

```

#!/bin/bash

file_csv="./test.csv"
colonne_artiste=2
colonne_titre=1
sep=';'

i=1
while true
do
    i=$((i+1))
    line=$(sed $i'!d' $file_csv)
    artiste=$(echo $line | cut -d $sep -f $colonne_artiste)
        titre=$(echo $line | cut -d $sep -f $colonne_titre)
    echo ""
    echo ""
    echo "********************"
    echo $line
    [ -z "$line" ] && echo "ligne vide : fin du script" && exit 0
    ytdlmusic --auto "$artiste" "$titre"
    echo "********************"
done 

```

## Local install to develop

```
git clone https://github.com/thib1984/ytdlmusic.git
cd ytdlmusic 
#work!
pip3 install . #to build
ytdlmusic "Rexlambo" "Stay With Me"  #to retest
``` 
 
## FAQ

### When i try to update youtube-dl with ``youtube-dl -U``, i obtain an error message in my debian/ubuntu

If you obtain the following message : 

```
It looks like you installed youtube-dl with a package manager, pip, setup.py or a tarball. Please use that to update.
```

instead of 

```
youtube-dl: error: youtube-dl's self-update mechanism is disabled on Debian.
Please update youtube-dl using apt(8).
See https://packages.debian.org/sid/youtube-dl for the latest packaged version.
```

, noo panic! You have just downloaded a newer version of youtube-dl which is not in apt. When a new version of youtube-dl will be released in apt, you will download it automatically with ``sudo apt upgrade``. If you want to retrieve the previous version, ``sudo apt remove youtube-dl && sudo apt install youtube-dl``

### I would like a MP3 format but I only get an OGG format, why?

The ``ffmpeg`` package is required for the MP3 conversion. Install it and retry to launch ytdlmusic

### The commands indicated in this README don't work for me! Why?

The  syntax of the commands can be change between versions, run ``ytdlmusic`` and read the help message. 

### I get an error about ``_requesthandler.py line 22`` when I try to use ytdlmusic

Sorry... You should update Python to 3.6 version or more. youtube-search-python doesn't seems to be compatible with Python 3.5 or less. Now, ytdlmusic package checks the Python version during the installation process.

### What are the compatibilities with Python, pip, youtube-dl and youtube-search-python?

When an new version is released, it is compatible with the last Python version ine the branches 3.6 to 3.9, on the release date. It's also compatible with the last versions of dependencies, on the release date.

### Have you tested your package?

Before a new version of ytdlmusic is published, it is checked in automatic job, with the last versions of pip, youtube-dl and youtube-search-python, all in the last versions of Python in the branches 3.6 to 3.9. 

Each night, another job checks the actual package with last versions of dependencies and Pythons 3.6 to 3.9 and 3.10. So if a regression appears, the author of ytdlmusic received  an automatic mail to warn it.

These tests are executed with GitHub Actions on an Ubuntu 18.04 image.
## Thanks

This package use two very important dependencies :
- [youtube_dl](https://pypi.org/project/youtube_dl/)
- [youtube-search-python](https://pypi.org/project/youtube-search-python/)

Thanks to contributors and dependencies authors :

- [albenquer](https://github.com/albenquer)
- [Hitesh Kumar Saini](https://github.com/alexmercerind)
- [youtube-dl](https://github.com/youtube-dl)

## License

MIT License

Copyright (c) 2021 [thib1984](https://github.com/thib1984)


