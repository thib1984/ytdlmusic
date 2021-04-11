## description

With ytdlmusic, you can download from youtube a mp3 music without use browser. 5 choices are available with small summary to facilitate the choice. You can also use auto mode to download the first item.  

## github

[Github link](https://github.com/thib1984/ytdlmusic/)

## pipy

[Pipy link](https://pypi.org/project/ytdlmusic/)

## prerequisites

- install pip or pip3 for your system
- install ffmpeg for your system

## installation

``pip install ytdlmusic`` or ``pip3 install ytdlmusic``

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

## local install to develop

```
git clone https://github.com/thib1984/ytdlmusic.git
cd ytdlmusic 
#work!
python3 ytdlmusic/__ytdlmusic__.py "the beatles" "let it be" #to test
pip3 install . #to build
ytdlmusic "the beatles" "let it be"  #to retest
``` 

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

## thanks

This package use two very important depedencies :
- [youtube_dl](https://pypi.org/project/youtube_dl/)
- [youtube-search-python](https://pypi.org/project/youtube-search-python/)