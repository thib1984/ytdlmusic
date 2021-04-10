from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="ytdlmusic",
    version="0.1.0",
    description="ytdlmusic",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/thib1984/ytdlmusic",
    author="thib1984",
    author_email="thibault.garcon@gmail.com",
    license="mit",
    packages=["ytdlmusic"],
    install_requires=["setuptools", "youtube-search-python", "youtube_dl"],
    zip_safe=False,
    entry_points={
        "console_scripts": ["ytdlmusic=ytdlmusic.__ytdlmusic__:ytdlmusic"],
    },
)
