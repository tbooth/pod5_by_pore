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

def pore_to_batch(pore_num, batch_size):
    """Given a pore number, return the batch where it should be batched.
       I'll use inclusive ranges starting at 1, which is not Pythonic but
       generally more intuitive. So for batch_size of 50 we'll have "1-50",
       "51-100", "101-150" etc.
    """
    pore_num = int(pore_num)
    assert pore_num >= 1

    batch_size = int(batch_size)
    if batch_size == 1:
        # Special case
        return str(pore_num)
    assert batch_size >= 2

    # OK, here we go

    batch_start = ( ((pore_num - 1) // batch_size) * batch_size ) + 1
    batch_end = batch_start + ( batch_size - 1 )

    return f"{batch_start}-{batch_end}"

# Quick test
assert pore_to_batch(23, 1) == "23"
assert pore_to_batch(1, 50)  == "1-50"
assert pore_to_batch(50, 50) == "1-50"
assert pore_to_batch(51, 50) == "51-100"
assert pore_to_batch(99, 27) == "82-108"

