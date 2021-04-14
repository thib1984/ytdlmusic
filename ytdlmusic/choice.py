"""
choice user scripts
"""

import sys


def choice(results_search, auto):
    """
    user choice
    """
    i = 0
    if len(results_search.result()["result"]) == 0:
        print("no result, retry with other words")
        sys.exit(0)
    answer = 1
    if not auto:
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

        while True:
            answer = input(
                "which (1-"
                + str(len(results_search.result()["result"]))
                + ", 0 to exit properly) ? "
            )
            if (
                answer.isnumeric()
                and int(answer) >= 0
                and int(answer) <= 5
            ):
                break
        if int(answer) == 0:
            sys.exit(0)
    return int(answer)
