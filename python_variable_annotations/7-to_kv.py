#!/usr/bin/env python3
"""Module with a type-annotated to_kv function."""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Return a tuple with a string and the square of a number."""
    return (k, v ** 2)
