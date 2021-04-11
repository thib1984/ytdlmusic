## description

With ytdlmusic, you can download from youtube a mp3 music without use browser. 5 choices are available with small summary to facilitate the choice. You can also use auto mode to download the first item.  

## github

[Github link](https://github.com/thib1984/ytdlmusic/)

## pipy

[Pipy link](https://pypi.org/project/ytdlmusic/)

## prerequisites

install ffmpeg for your system

## installation

``pip install ytdlmusic`` or ``pip3 install ytdlmusic``

## use

``ytdlmusic "the beatles" "let it be"``
will download, after choice, the mp3 in the current directory

```
~$ ytdlmusic "the beatles" "let it be"

1
Let It Be (Remastered 2009)
4:04
None - 75,848,559 views
************************************

2
Let It Be (Remastered 2015)
3:51
None - 13,390,170 views
************************************

3
The Beatles - Let it be
4:15
8 years ago - 29,173,724 views
************************************

4
Beatles   Let It Be 1970
3:55
2 years ago - 326,613 views
************************************

5
The Beatles - Let It be lyrics
2:17
3 years ago - 7,239,282 views
************************************

which? 5
[youtube] 6d5ST3tbPIU: Downloading webpage
[download] Destination: the beatles let it be.m4a
[download] 100% of 2.11MiB in 00:00
[ffmpeg] Correcting container in "the beatles let it be.m4a"
[ffmpeg] Destination: the beatles let it be.mp3
Deleting original file the beatles let it be.m4a (pass -k to keep)
[ffmpeg] Adding metadata to 'the beatles let it be.mp3'
````

## use auto

``ytdlmusic "the beatles" "let it be" auto`` will dowmnload the first item 

## local install to develop

```
git clone https://github.com/thib1984/ytdlmusic.git
cd ytdlmusic 
#work!
pip3 install .
#launch ytdlmusic
``` 

## batch

you can use script for loop in a csv file for example 

```

#!/bin/bash

file_csv="./test.csv"
colonne_artiste=2
colonne_titre=1
sep=','

i=1
while true
do
	i=$((i+1))
	line=$(sed $i'!d' $file_csv)
	artiste=$(echo $line | cut -d $sep -f $colonne_artiste)     # get the first name
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

