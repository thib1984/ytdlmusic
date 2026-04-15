from setuptools import setup


setup(
    name="ytdlmusic",
    version="5.0.0",
    description="ytdlmusic is a command-line program to search and download music files from YouTube without use browser.",
    long_description="The complete description/installation/use/FAQ is available at : https://github.com/thib1984/ytdlmusic#readme",
    long_description_content_type="text/markdown",
    url="https://github.com/thib1984/ytdlmusic",
    author="thib1984",
    author_email="thibault.garcon@gmail.com",
    license="MIT",
    license_files="LICENSE.txt",
    packages=["ytdlmusic"],
    install_requires=[
        "yt_dlp",
        "yt-dlp-ejs",
        "tinytag",
        "unidecode",
        "termcolor",
        "colorama",
        "validators",
        "deno"
    ],
    zip_safe=False,
    entry_points={
        "console_scripts": ["ytdlmusic=ytdlmusic.__init__:ytdlmusic"],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.10",
)
