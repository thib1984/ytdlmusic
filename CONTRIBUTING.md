# Local install to develop

```
git clone https://github.com/thib1984/ytdlmusic.git
cd ytdlmusic 
#work!
pip3 install . #to build
#test!
pip3 uninstall ytdlmusic #to properly uninstall the dev version
``` 
# Test

## Prerequisites

With [act](https://github.com/nektos/act), you can play Github Action locally.

To install it :
```
curl https://raw.githubusercontent.com/nektos/act/master/install.sh | sudo bash
```
or go to [this page](https://github.com/nektos/act#installation)

## Launch test

Just, go to the root of the project and play ``act -j full_test`` (test OS ubuntu 20.04/python 3.9) or ``act -j full_test_multi`` (multi OS/multi python ... slower).


The actions are available in ``.github`` folder


