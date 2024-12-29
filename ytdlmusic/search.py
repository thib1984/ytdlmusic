"""
search utils scripts
"""
from ytdlmusic.log import print_debug
from ytdlmusic.params import param_number, my_colored_emoji, is_verbose, is_quiet

try:
    import yt_dlp
except ImportError:
    print_debug("yt_dlp import problem")


def search(keywords):
    """
    search the items with yt-dlp
    return a json with 5 entries of YouTube results
    param : the artist and the song
    """

    print_debug("search : " + keywords)
    print(
        my_colored_emoji(
            "\U0001F50E", "search " + keywords + '" with yt-dlp',
            "green",
        )
    )
    my_limit = int(param_number())


    ydl_opts = {
        'quiet': True,
        'extract_flat': True,  # Permet d'extraire plus de détails sur chaque vidéo
        'simulate': True,       # Empêche le téléchargement
        'force_generic_extractor': True
    }
    
    if is_verbose():
        ydl_opts["verbose"] = "True"
        print_debug("debug yt-dlp is activated")
    if not is_quiet():
        print("start yt-dlp operation")
    elif is_quiet():
        ydl_opts["quiet"] = True
        ydl_opts["no_warnings"] = True

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        result = ydl.extract_info("ytsearch"+str(my_limit)+":"+keywords, download=False)

    return result
