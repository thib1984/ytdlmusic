"""
choice user scripts
"""

import sys
from ytdlmusic.params import is_auto, is_batch, my_colored_emoji
from ytdlmusic.const import CHOICE_RESULT_QUESTION
from ytdlmusic.print import replace_all


def choice(results_search):
    """
    user choice after return of yt-dlp
    results : the selected choice
    return 0 if automode and no result
    if 0 is choosen by the user, exit 1
    if illegal choice from user, print abort + exit 1
    1 for default choice
    auto : True if no interactive choice, False otherwise
    """

    numero_choix = 0
    tab_results = results_search['entries']
    nb_choix = len(tab_results)

    if nb_choix == 0:
        print("No result found, retry with other words.")
        if is_batch():
            return 0
        sys.exit(1)

    if is_auto():
        return 1

    for result in tab_results:
        numero_choix += 1
        print(
            str(numero_choix)
            + "\n"
            +  my_colored_emoji(
            "\U0001f3b6", result.get('title'),
            "yellow")
            + "\n"
            +  my_colored_emoji(
            "\U0001f4bb", result.get('url')
            + " - "
            + str(format_duration(result.get('duration')))
            + " - "
            + str(f"{result.get('view_count'):,}") + " views",
            "yellow")
        )

    answer = input(
        replace_all(CHOICE_RESULT_QUESTION, {"$1": str(nb_choix)})
    )

    # default choice
    if answer == "":
        return 1
    # no valid choice or 0
    if answer.isnumeric() and 1 <= int(answer) <= nb_choix:
        return int(answer)
    print("Abort.")
    if is_batch():
        return 0
    sys.exit(1)

# Fonction pour formater la durée en minutes et secondes
def format_duration(seconds):
    minutes, sec = divmod(int(float(seconds)), 60)
    return f"{minutes}:{sec}"    
