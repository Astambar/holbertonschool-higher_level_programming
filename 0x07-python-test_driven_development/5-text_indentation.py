#!/usr/bin/python3
"""[summary]
"""


def text_indentation(text):
    """[summary]

    Args:
        text ([type]): [description]

    Raises:
        TypeError: [description]
    """
    if type(text) != str:
        raise TypeError("text must be a string")
    tablesep = ['.', '?', ':']

    idx = 0

    for i in text:
        if i in tablesep:
            if text[idx + 1] == " ":
                text = text[:idx + 1] + text[idx + 2:]
        else:
            idx += 1

    idx = 0
    for items in text:
        if items in tablesep:
            text = text[:idx + 1] + '\n\n' + text[idx + 1:]
            idx += 3
        else:
            idx += 1
    print(f"{text}", '')
