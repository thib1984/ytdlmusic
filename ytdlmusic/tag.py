from tinytag import TinyTag

def obtain_tags(filename):
    tag = TinyTag.get(filename)
    title = translateNoneOrBlankToEmpty(tag.title)
    artist = translateNoneOrBlankToEmpty(tag.artist)
    album = translateNoneOrBlankToEmpty(tag.album)
    return title, artist, album

def translateNoneOrBlankToEmpty(my_string):
    if my_string and my_string.strip():
        return my_string.strip()
    return ""
