#!/usr/bin/python3
""" This function have a append_file"""


def append_write(filename="", text=""):
    """
    The append_write function appends text to the end of a file.

    Args:
        filename (str): The name of the file to be appended.
        Defaults to &quot;&quot;.

        text (str): The new content that will be written
        at the end of the file. Defaults to &quot;&quot;.



    :param filename=&quot;&quot;: Specify the name of the file to be opened
    :param text=&quot;&quot;: Specify the text that is to be written
    to the file
    :return: The number of characters written to the file
    :doc-author: Trelent
    """

    with open(filename, mode="a", encoding="utf-8") as append_write:
        return append_write.write(text)
