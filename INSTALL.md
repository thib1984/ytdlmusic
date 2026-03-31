# Prerequisites

- Install Python 3 on your system
- Install pipx on your system
- Install git on your system

# Why use pipx?

`pipx` installs Python applications in isolated environments, which prevents dependency conflicts with your system or other projects.  
It also allows you to run CLI tools globally without polluting your Python installation.  
This makes it safer and cleaner than using `pip` or `pip3` for installing standalone tools.

# Clean old versions

If you have installed an old version with `pip` or `pip3` (depending on your system), use one of the following commands:

```
pip3 uninstall ytdlmusic
pip uninstall ytdlmusic
pip3 uninstall ytdlmusic --break-system-packages
pip uninstall ytdlmusic --break-system-packages
```

# Installation

```
pipx upgrade ytdlmusic
pipx reinstall ytdlmusic #to force update dependencies
```

# Upgrade

```
pipx upgrade ytdlmusic --include-deps
```

This command upgrades the application to the latest version and also updates all its dependencies.

# Uninstall

```
pipx uninstall ytdlmusic
```