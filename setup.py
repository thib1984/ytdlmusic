from setuptools import setup


setup(
    name="ytdlmusic",
    version="1.0.0",
    description="With ytdlmusic, you can download from youtube a MP3/OGG music without use browser. 5 choices are available with a small summary to facilitate the choice. You can also use auto mode to download the first item.",
    long_description="The complete description/installation/use/FAQ is available at : https://github.com/thib1984/ytdlmusic#readme",
    long_description_content_type="text/markdown",
    url="https://github.com/thib1984/ytdlmusic",
    author="thib1984",
    author_email="thibault.garcon@gmail.com",
    license="mit",
    packages=["ytdlmusic"],
    install_requires=[
        "setuptools",
        "youtube-search-python",
        "youtube_dl",
    ],
    zip_safe=False,
    entry_points={
        "console_scripts": ["ytdlmusic=ytdlmusic.__init__:ytdlmusic"],
    },
    python_requires=">=3.6",
)
