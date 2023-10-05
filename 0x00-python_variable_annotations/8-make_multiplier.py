#!/usr/bin/env python3
"""type-annotated function"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """returns a function that multiplies a float by multiplier"""
    def multiplier_func(number: float) -> float:
        return multiplier * number
    return multiplier_func
