from setuptools import setup


setup(
    name="ytdlmusic",
    version="1.4.0",
    description="With ytdlmusic, you can download directly from YouTube music files in MP3/OGG format from your terminal, without using your browser. By default, it will match your request with a selection of 5 results with a brief summary to choose from or you can use auto mode to download automaticaly the first item.",
    long_description="The complete description/installation/use/FAQ is available at : https://github.com/thib1984/ytdlmusic#readme",
    long_description_content_type="text/markdown",
    url="https://github.com/thib1984/ytdlmusic",
    author="thib1984",
    author_email="thibault.garcon@gmail.com",
    license="MIT",
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
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
