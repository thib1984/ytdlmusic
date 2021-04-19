"""
choice user scripts
"""

import sys
from ytdlmusic.params import is_auto, is_batch
from ytdlmusic.const import CHOICE_RESULT_QUESTION
from ytdlmusic.print import replace_all


def choice(results_search):
    """
    user choice after return of youtube-search-python
    results : the selected choice
    return 0 if automode and no result
    if 0 is choosen by the user, exit 1
    if illegal choice from user, print abort + exit 1
    1 for default choice
    auto : True if no interactive choice, False otherwise
    """
    numero_choix = 0
    tab_results = results_search.result()["result"]
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
            + result["title"]
            + "\n"
            + result["link"]
            + "\n"
            + result["duration"]
            + "-"
            + result["viewCount"]["text"]
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
