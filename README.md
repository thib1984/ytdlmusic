:warning: ytdlmusic is not compatible with Python < 3.5 (deprecated), use Python >= 3.6 !


## description

With ytdlmusic, you can download directly from YouTube music files in MP3/OGG format from your terminal, without using your browser. 
By default, it will match your request with a selection of 5 results with a breif summary to choose from or you can use auto mode to download automaticaly the first item.  

## github

[Github link](https://github.com/thib1984/ytdlmusic/)

## pipy

[Pipy link](https://pypi.org/project/ytdlmusic/)

## prerequisites

- install Python 3 for your system
- install pip3 for your system #or pip if pip3 does not exist
- optional : install ffmpeg for your system if you want to use MP3 format (OGG otherwise)

## installation

``pip3 install ytdlmusic #or with pip if pip3 does not exist``

## upgrade

`` ytdlmusic --update`` to upgrade ytdlmusic

`` ytdlmusic --full-update`` to upgrade ytdlmusic, youtube-dl and youtube-search-python since 0.5 version

``pip3 install --upgrade ytdlmusic #or with pip if pip3 does not exist`` to upgrade ytdlmusic with pip

``pip3 install -ytdlmusic:x.x.x #to downgrade the app`` to downgrade ytdlmusic to a specified version with pip
## use

``ytdlmusic "Rexlambo" "Stay With Me"``
will return a 5 items result list from which to chose which item to download, as a mp3/OGG file in the current directory

```
~$ ytdlmusic "the beattles" "Stay With Me"
artist : Rexlambo
song : Stay With Me,
search Rexlambo Stay With Me MP3/OGG with youtubesearchpython

1
Stay With Me (Remastered 2009)
https://www.youtube.com/watch?v=QDYfEBY9NM4
4:04 - 75,940,717 views


2
Stay With Me (Remastered 2015)
https://www.youtube.com/watch?v=HzvDofigTKQ
3:51 - 13,390,170 views


3
Rexlambo - Stay With Me
https://www.youtube.com/watch?v=7P6X3IWLECY
4:15 - 29,202,773 views


4
Beatles   Stay With Me 1970
https://www.youtube.com/watch?v=nt9uBlRuBPw
3:55 - 326,823 views


5
Stay With Me (Remastered 2009)
https://www.youtube.com/watch?v=hR-3ajVftG4
3:53 - 1,684,647 views


which (1-5, 0 to exit properly) ? 2
future filename is : rexlambo_stay_with_me.mp3
download https://www.youtube.com/watch?v=HzvDofigTKQ with youtubedl
[youtube] HzvDofigTKQ: Downloading webpage
[download] Destination: rexlambo_stay_with_me.webm
[download] 100% of 3.73MiB in 00:00
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
search Rexlambo Stay With Me mp3 with youtubesearchpython
download https://www.youtube.com/watch?v=QDYfEBY9NM4 with youtubedl
[youtube] QDYfEBY9NM4: Downloading webpage
[download] Destination: rexlambo_stay_with_me.webm
[download] 100% of 3.75MiB in 00:00
[ffmpeg] Destination: rexlambo_stay_with_me.mp3
Deleting original file rexlambo_stay_with_me.webm (pass -k to keep)
[ffmpeg] Adding metadata to 'rexlambo_stay_with_me.mp3'
rexlambo_stay_with_me.mp3 is ready
```

## other commands

`` ytdlmusic --help`` to display help message

`` ytdlmusic --update `` to upgrade ytdlmusic

`` ytdlmusic --full-update `` to upgrade ytdlmusic, youtube-dl and youtube-search-python

`` ytdlmusic --version `` to display version of ytdlmusic and dependencies
## batch

You can use a script to loop in a csv file. ie: 

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

## local install to develop

```
git clone https://github.com/thib1984/ytdlmusic.git
cd ytdlmusic 
#work!
pip3 install . #to build
ytdlmusic "Rexlambo" "Stay With Me"  #to retest
``` 
 
## FAQ

- When i try to update youtube-dl with ``youtube-dl -U``, i obtain the following message in my debian/ubuntu

```
It looks like you installed youtube-dl with a package manager, pip, setup.py or a tarball. Please use that to update.
```

instead of 

```
youtube-dl: error: youtube-dl's self-update mechanism is disabled on Debian.
Please update youtube-dl using apt(8).
See https://packages.debian.org/sid/youtube-dl for the latest packaged version.
```

No panic : you have just downloaded a newer version of youtube-dl which is not in apt. When a new version of youtube-dl will be released in apt, you will download it automatically with ``sudo apt upgrade``. If you want to retrieve the previous version, ``sudo apt remove youtube-dl && sudo apt install youtube-dl``

- I would like a MP3 format but I only get an OGG format, why?

The ``ffmpeg`` package is required for the MP3 conversion. Install it and retry to launch ytdlmusic

- The commands indicated in this README don't work! Why?

The  syntax of the commands can be change between versions, run ``ytdlmusic`` and read the help message. 

- I get an error about ``_requesthandler.py line 22`` when I try to use ytdlmusic

Sorry... You should update python to 3.6 version or more. youtube-search-python doesn't seems to be compatible with python 3.5 or less. from version 0.6.1, the ytdlmusic package checks the python version during the installation process.

- What are the compatibilities with Python, pip, youtube-dl and youtube-search-python?

When a new version of ytdlmusic is published, it is tested with the last versions of pip, youtube-dl and youtube-search-python. For Python, the last versions are  tested in the branches 3.6 to 3.9. Each night, a job retest the actual package with last versions of dependencies and Pythons 3.6 to 3.9 and 3.10. These tests are executed with GitHub Actions on an Ubuntu 18.04 image.
## thanks

This package use two very important dependencies :
- [youtube_dl](https://pypi.org/project/youtube_dl/)
- [youtube-search-python](https://pypi.org/project/youtube-search-python/)

Thanks to contributors :

- https://github.com/albenquer
