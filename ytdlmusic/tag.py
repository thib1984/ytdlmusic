"""
tag utils scripts
"""
from tinytag import TinyTag


def obtain_tags(filename):
    """
    obtain tags from file
    """
    tag = TinyTag.get(filename)
    title = translate_none_or_blank_to_empty(tag.title)
    artist = translate_none_or_blank_to_empty(tag.artist)
    album = translate_none_or_blank_to_empty(tag.album)
    return title, artist, album


def translate_none_or_blank_to_empty(my_string):
    """
    return "" if blank or empty or None, string otherwise
    """
    if my_string and my_string.strip():
        return my_string.strip()
    return ""
