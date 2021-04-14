"""
search utils scripts
"""


def search(artist, song):
    """
    search the items
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
