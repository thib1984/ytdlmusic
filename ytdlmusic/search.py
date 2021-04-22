"""
search utils scripts
"""
from ytdlmusic.log import print_debug
from ytdlmusic.params import is_number, param_number

try:
    from youtubesearchpython import VideosSearch
except ImportError:
    print_debug("youtubesearchpython import problem")


def search(artist, song):
    """
    search the items with youtube-search-python
    return a json with 5 entries of YouTube results
    param : the artist and the song
    """

    print_debug("artist : " + artist)
    print_debug("song : " + song)
    search_pattern = artist + " " + song
    print(
        'search "' + search_pattern + '" with youtube-search-python'
    )
    my_limit = 5
    if is_number():
        my_limit = int(param_number())
    return VideosSearch(search_pattern, limit=my_limit)
