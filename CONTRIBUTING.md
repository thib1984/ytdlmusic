# 🙏 Thanks !

Oh if you open this page, it's for contributing for this project, great ! A big thanks 🙏

To contribute, it's simple, check the [existing issues](https://github.com/thib1984/ytdlmusic/issues). If you see an issue you are interested to work, please let a message and i assign you the task. With this, all people know you are working on this issue.

If it's a new subject, don't hesitate to create an issue. I will check this one to affect some labels and let contribution open 😉

You can initialize a draft merge request directly when you start to work on an issue.

When you finish, past the merge request in "ready" mode and i will check this quickly.

If you are any questions, don't try to ping me 😁

# Local install to develop

```
git clone https://github.com/[your-forked-repo]/ytdlmusic.git
cd ytdlmusic 
#work!
pip3 install . #to build
#test!
#pip3 uninstall ytdlmusic #to properly uninstall the dev version
#git add/commit/push [...]
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


