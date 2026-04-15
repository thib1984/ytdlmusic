"""
print utils scripts
"""

import traceback
from ytdlmusic.const import (
    EXCEPTION,
    BUG_MESSSAGE,
    EXCEPTION_BATCH,
    DEBUG_HEADER,
    BUG_MESSSAGE_DEBUG,
)
from ytdlmusic.file import binary_path
from ytdlmusic.params import is_verbose, my_colored


def replace_all(text, dic):
    """
    replace in param text with dict paramaters
    example : dic = { "cat": "dog", "bird": "rabbit"}
    text = "This is my cat and this is my bird."
    -> "This is my dog and this is my rabbit."
    """
    for i, j in dic.items():
        text = text.replace(i, j)
    return text



def print_error():
    """
    print the error message with additional informations
    """
    if is_verbose():
        print(my_colored(DEBUG_HEADER, "yellow"))
        print(my_colored(traceback.format_exc(), "yellow"))
    print(my_colored(EXCEPTION, "red"))
    print_addtional_informations()

def print_error_batch():
    """
    print the error message with additional informations
    """
    if is_verbose():
        print(my_colored(DEBUG_HEADER, "yellow"))
        print(my_colored(traceback.format_exc(), "yellow"))
    print(my_colored(EXCEPTION_BATCH, "red"))
    print_addtional_informations()


def print_addtional_informations():
    """
    print footer informations
    """
    if is_verbose():
        print(my_colored(BUG_MESSSAGE_DEBUG, "yellow"))
    else:
        print(my_colored(BUG_MESSSAGE, "yellow"))


    


