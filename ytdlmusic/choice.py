"""
choice user scripts
"""

import sys
from ytdlmusic.params import is_auto, is_batch


def choice(results_search):
    """
    user choice after return of youtube-search-python
    results : the json of youtube-search-pythons
    auto : True if no interactive choice, False otherwise
    """
    i = 0
    if len(results_search.result()["result"]) == 0:
        print("No result found, retry with other words.")
        if not is_batch():
            sys.exit(1)
        return 0
    answer = 1
    if not is_auto():
        for children in results_search.result()["result"]:
            i = i + 1
            print(i)
            print(children["title"])
            print(children["link"])
            print(
                children["duration"]
                + " - "
                + children["viewCount"]["text"]
            )

        answer = input(
            "Which (1-"
            + str(len(results_search.result()["result"]))
            + ", 0 to exit properly, 1 by default) ? "
        )
        if answer == "":
            answer = "1"
        if (
            (not answer.isnumeric())
            or int(answer) <= 0
            or int(answer) > len(results_search.result()["result"])
        ):
            print("Abort.")
            if not is_batch():
                sys.exit(1)
    return int(answer)
