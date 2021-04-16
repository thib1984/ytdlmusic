"""
search utils scripts
"""


def search(artist, song):
    """
    search the items with youtube-search-python
    return a json with 5 entries of YouTube results
    param : the artist and the song
    """
    from youtubesearchpython import VideosSearch

    print("artist : " + artist)
    print("song : " + song)
    print(
        "search "
        + artist
        + " "
        + song
        + " mp3 with youtubesearchpython"
    )
    results_search = VideosSearch(
        artist + " " + song + " mp3", limit=5
    )

    return results_search
