:warning: ytdlmusic is not compatible with python2 (deprecated), use python3!


## description

With ytdlmusic, you can download from youtube a mp3 music without use browser. 5 choices are available with small summary to facilitate the choice. You can also use auto mode to download the first item.  

## github

[Github link](https://github.com/thib1984/ytdlmusic/)

## pipy

[Pipy link](https://pypi.org/project/ytdlmusic/)

## prerequisites

- install python3 for your system #no python2!
- install pip3 for your system #or pip if pip3 does not exist
- optional : install ffmpeg for your system if you want use mp3 format (ogg if not)

## installation

``pip3 install ytdlmusic #or with pip if pip3 does not exist``

## upgrade

``pip3 install --upgrade ytdlmusic #or with pip if pip3 does not exist``

## use

``ytdlmusic "the beatles" "let it be"``
will download, after choice, the mp3 in the current directory

```
~$ ytdlmusic "the beattles" "let it be"
artist : the beatles
song : let it be
search the beatles let it be mp3 with youtubesearchpython

1
Let It Be (Remastered 2009)
https://www.youtube.com/watch?v=QDYfEBY9NM4
4:04 - 75,940,717 views


2
Let It Be (Remastered 2015)
https://www.youtube.com/watch?v=HzvDofigTKQ
3:51 - 13,390,170 views


3
The Beatles - Let it be
https://www.youtube.com/watch?v=7P6X3IWLECY
4:15 - 29,202,773 views


4
Beatles   Let It Be 1970
https://www.youtube.com/watch?v=nt9uBlRuBPw
3:55 - 326,823 views


5
Let It Be (Remastered 2009)
https://www.youtube.com/watch?v=hR-3ajVftG4
3:53 - 1,684,647 views


which (1-5, 0 to exit properly) ? 2
future filename is : the_beatles_let_it_be.mp3
download https://www.youtube.com/watch?v=HzvDofigTKQ with youtubedl
[youtube] HzvDofigTKQ: Downloading webpage
[download] Destination: the_beatles_let_it_be.webm
[download] 100% of 3.73MiB in 00:00
[ffmpeg] Destination: the_beatles_let_it_be.mp3
Deleting original file the_beatles_let_it_be.webm (pass -k to keep)
[ffmpeg] Adding metadata to 'the_beatles_let_it_be.mp3'
the_beatles_let_it_be.mp3 is ready
````

## use auto

``ytdlmusic "the beatles" "let it be" auto`` 
will dowmnload the first item 

```
~$ ytdlmusic "the beattles" "let it be" auto
artist : the beatles
song : let it be
search the beatles let it be mp3 with youtubesearchpython
future filename is : the_beatles_let_it_be.mp3
download https://www.youtube.com/watch?v=QDYfEBY9NM4 with youtubedl
[youtube] QDYfEBY9NM4: Downloading webpage
[download] Destination: the_beatles_let_it_be.webm
[download] 100% of 3.75MiB in 00:00
[ffmpeg] Destination: the_beatles_let_it_be.mp3
Deleting original file the_beatles_let_it_be.webm (pass -k to keep)
[ffmpeg] Adding metadata to 'the_beatles_let_it_be.mp3'
the_beatles_let_it_be.mp3 is ready
```

## other commands

`` ytdlmusic help`` to display help message

`` ytdlmusic update `` to upgrade ytdlmusic, youtube-dl and youtube-search-python

`` ytdlmusic version `` to display version of ytdlmusic and dependencies
## batch

you can use script for loop in a csv file for example 

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
	ytdlmusic "$artiste" "$titre" auto
	echo "********************"
done 

```

## local install to develop

```
git clone https://github.com/thib1984/ytdlmusic.git
cd ytdlmusic 
#work!
python3 ytdlmusic/__ytdlmusic__.py "the beatles" "let it be" #to test
pip3 install . #to build
ytdlmusic "the beatles" "let it be"  #to retest
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

No panic : you have just downloaded a newer version of youtube-dl who is not in apt. When a new version of youtube-dl will be released in apt, you will download it automatically with ``sudo apt upgrade``. If you want retrieve the previous version, ``sudo apt remove youtube-dl && sudo apt install youtube-dl``

## thanks

This package use two very important depedencies :
- [youtube_dl](https://pypi.org/project/youtube_dl/)
- [youtube-search-python](https://pypi.org/project/youtube-search-python/)
