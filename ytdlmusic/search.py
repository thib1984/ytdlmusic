"""
search utils scripts
"""
from ytdlmusic.log import print_debug
from ytdlmusic.params import param_number

try:
    from youtubesearchpython import VideosSearch
except ImportError:
    print_debug("youtubesearchpython import problem")


def search(search):
    """
    search the items with youtube-search-python
    return a json with 5 entries of YouTube results
    param : the artist and the song
    """

    print_debug("search : " + search)
    search_pattern = search
    print(
        'search "' + search_pattern + '" with youtube-search-python'
    )
    my_limit = int(param_number())
    return VideosSearch(search_pattern, limit=my_limit)
