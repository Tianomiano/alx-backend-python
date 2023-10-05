#!/usr/bin/env python3
"""type-annotated function that adds a mixed list of integers and floats"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """returns the sum as a float."""
    return sum(mxd_lst)
