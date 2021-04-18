"""
search utils scripts
"""
from ytdlmusic.params import is_verbose


def search(artist, song):
    """
    search the items with youtube-search-python
    return a json with 5 entries of YouTube results
    param : the artist and the song
    """
    from youtubesearchpython import VideosSearch

    if is_verbose():
        print("artist : " + artist)
        print("song : " + song)
    search_pattern = artist + " " + song
    print(
        'search "' + search_pattern + '" with youtube-search-python'
    )
    results_search = VideosSearch(search_pattern, limit=5)

    return results_search
