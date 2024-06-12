#!/usr/bin/env python3
"""Type-annotated function add"""


from typing import List
def sum_list(input_list: List[float]) -> float:
    """Takes two floats and returns their sum as float"""
    s: float = 0
    for i in input_list:
        s += i
    return s
