"""Make ``flaky`` reruns work with ``pytest-randomly``."""

import functools as ft
import random
from collections import Counter

import numpy as np

_attempts: Counter = Counter()


def fresh_seed_each_run(func):
    pass  # TODO: implement



    def wrapper(*args, **kwargs):
        pass  # TODO: implement

