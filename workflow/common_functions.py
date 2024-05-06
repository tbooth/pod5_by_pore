"""Utility functions for use by the workflow
"""
import os, re
from functools import partial

def n_sorted():
    key_regex = re.compile(r"(?<=[._])\d+(?=[._])")
    def key_func(filename):
        return re.sub(key_regex, lambda d: d.group().rjust(8,'0'), filename)
    return partial(sorted, key=key_func)
n_sorted = n_sorted()

def get_common_prefix(list_of_filenames, extn=r"\..+", base_only=True):
    """Used by the Snakefiles. Chop extn (which is a regex) off every file
       in the list and see if that leaves a common prefix. If so, return it.
       If not, return None.
    """
    extn_regex = re.compile(extn + "$")
    if not list_of_filenames:
        return None

    if base_only:
        list_of_filenames = (os.path.basename(f) for f in list_of_filenames)
    else:
        list_of_filenames = iter(list_of_filenames)

    common_prefix = re.sub(extn_regex, '', next(list_of_filenames))

    for f in list_of_filenames:
        p = re.sub(extn_regex, '', f)
        if p != common_prefix:
            return None

    return common_prefix

