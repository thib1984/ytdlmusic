# Prerequisites

- Install Python 3 for your system
- Install pip3* for your system
- Install ffmpeg for your system if you want to use MP3/OGG format (M4A otherwise)

# Installation

Recommended method: Install using pipx

```
pip3 install pipx
pipx install ytdlmusic
```

Why pipx?
- Isolation: Creates an isolated virtual environment for the tool.
- Dependency Management: Avoids conflicts with system-wide Python packages.
- Easy Upgrades: Tools installed with pipx can be upgraded independently.

Alternative method: Install directly with pip3
```
pip3 install ytdlmusic
```

Note:
- Direct pip installation installs globally or in your active Python environment.
- May lead to dependency conflicts if other tools rely on different versions of the same packages.


# Upgrade


If installed via pipx

```
pipx upgrade ytdlmusic
```

If installed via pip3
```
pip3 install --upgrade ytdlmusic
pip3 install --upgrade yt_dlp
```

Explanation:
- The first command upgrades ytdlmusic to the latest version.
- The second command upgrades yt_dlp, a key dependency for downloading content.
- Keeping yt_dlp updated ensures compatibility with YouTube and other supported services