#!/usr/bin/env python3
"""type-annotated function which finds the sum of an input_list"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Return sum of the floats in the list"""
    return float(sum(input_list))
