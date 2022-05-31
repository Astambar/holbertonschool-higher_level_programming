#!/usr/bin/python3
""" This function have a from_json_string """

import json


def from_json_string(my_str):
    """
    The from_json_string function converts a JSON string to a Python object.

    Parameters:
        my_str (str): A JSON string.

        Returns: 
            The Python object represented by the JSON string.
        Examples: 
            &gt;&gt;&gt; from_json_string('[&quot;foo&quot;, {&quot;bar&quot;:[&quot;baz&quot;,

    :param my_str: Pass a string to the function
    :return: A list of dictionaries
    :doc-author: Trelent
    """

    return json.loads(my_str)
