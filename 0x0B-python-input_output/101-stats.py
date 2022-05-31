#!/usr/bin/python3
"""[summary]
"""


def print_stats(size, status_codes):
    """
    The print_stats function prints the size of the file and
    a count of each status code returned by the web server.
    Args:
        size (int): The size of the file in bytes.
        status_codes (dict): A dictionary containing
        all HTTP response codes and their counts.
     Returns: None
    :param size: Print the size of the file
    :param status_codes: Store the status codes of the http requests
    :return: A dictionary with the file size and a dictionary of status codes
    :doc-author: Trelent
    """
    print(f"File size: {size}")
    for key in sorted(status_codes):
        print(f"{key}: {status_codes[key]}")

import contextlib
if __name__ == "__main__":
    import sys

    size = 0
    status_codes = {}
    valid_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
    count = 0

    try:
        for line in sys.stdin:
            if count == 10:
                print_stats(size, status_codes)
                count = 1
            else:
                count += 1

            line = line.split()

            with contextlib.suppress(IndexError, ValueError):
                size += int(line[-1])

            with contextlib.suppress(IndexError):
                if line[-2] in valid_codes:
                    if status_codes.get(line[-2], -1) == -1:
                        status_codes[line[-2]] = 1
                    else:
                        status_codes[line[-2]] += 1

        print_stats(size, status_codes)

    except KeyboardInterrupt:
        print_stats(size, status_codes)
        raise
