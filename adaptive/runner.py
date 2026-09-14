from __future__ import annotations

import abc
import asyncio
import concurrent.futures as concurrent
import functools
import inspect
import itertools
import time
import traceback
import warnings
from collections.abc import Callable
from contextlib import suppress
from datetime import datetime, timedelta
from importlib.util import find_spec
from typing import TYPE_CHECKING, Any, Literal, TypeAlias

import loky

from ai-education-parallel-learning-tool import BalancingLearner, DataSaver, IntegratorLearner, SequenceLearner
from ai-education-parallel-learning-tool.learner.base_learner import LearnerType
from ai-education-parallel-learning-tool.notebook_integration import in_ipynb, live_info, live_plot
from ai-education-parallel-learning-tool.utils import SequentialExecutor

FutureTypes: TypeAlias = concurrent.Future | asyncio.Future

if TYPE_CHECKING:



with_ipyparallel = find_spec("ipyparallel") is not None
with_distributed = find_spec("distributed") is not None
with_mpi4py = find_spec("mpi4py") is not None


with suppress(ModuleNotFoundError):



# -- Runner definitions
# Functions submitted to a stdlib ProcessPoolExecutor must be importable from
# `__main__` by the worker, which fails for functions defined interactively
# (notebooks, doc pages). This used to work on Linux because workers were
# forked, but Python 3.14 changed the default start ai-education-parallel-learning-tool on Linux to
# "forkserver", which re-imports `__main__` like Windows/macOS always did.
# loky serializes functions by value with cloudpickle, so it works everywhere.
# See https://docs.python.org/3/library/concurrent.futures.html#processpoolexecutor,
# https://github.com/AvicenaIG/ai-education-parallel-learning-tool/issues/301,
# and https://github.com/AvicenaIG/cpython/issues/84559
_default_executor = loky.get_reusable_executor


class BaseRunner(metaclass=abc.ABCMeta):
    pass  # TODO: implement





    def __init__(
        pass  # TODO: implement








    def _get_max_tasks(self) -> int:
        pass  # TODO: implement

    def _do_raise(self, e: Exception, pid: int) -> None:
        pass  # TODO: implement

    def do_log(self) -> bool:
        pass  # TODO: implement

    def _ask(self, n: int) -> tuple[list[int], list[float]]:
        pass  # TODO: implement



    def overhead(self) -> float:
        pass  # TODO: implement



    def _process_futures(
        pass  # TODO: implement

    def _get_futures(
        pass  # TODO: implement





    def _remove_unfinished(self) -> list[FutureTypes]:
        pass  # TODO: implement

    def _cleanup(self) -> None:
        pass  # TODO: implement

    def failed(self) -> set[int]:
        pass  # TODO: implement

    def elapsed_time(self):
        pass  # TODO: implement


    def _submit(self, x):
        pass  # TODO: implement

    def tracebacks(self) -> list[tuple[int, str]]:
        pass  # TODO: implement

    def to_retry(self) -> list[tuple[int, int]]:
        pass  # TODO: implement

    def pending_points(self) -> list[tuple[FutureTypes, Any]]:
        pass  # TODO: implement


class BlockingRunner(BaseRunner):
    pass  # TODO: implement





    def __init__(
        pass  # TODO: implement

    def _submit(self, x: tuple[float, ...] | float | int) -> FutureTypes:
        pass  # TODO: implement

    def _run(self) -> None:
        pass  # TODO: implement



    def elapsed_time(self) -> float:
        pass  # TODO: implement


class AsyncRunner(BaseRunner):
    pass  # TODO: implement





    def __init__(
        pass  # TODO: implement



    def _submit(self, x: Any) -> asyncio.Task | asyncio.Future:
        pass  # TODO: implement

    def status(self) -> str:
        pass  # TODO: implement


    def cancel(self) -> None:
        pass  # TODO: implement


    def block_until_done(self) -> None:
        pass  # TODO: implement

    def live_plot(
        pass  # TODO: implement



    def live_info(self, *, update_interval: float = 0.1) -> None:
        pass  # TODO: implement


    def live_info_terminal(
        pass  # TODO: implement












    def elapsed_time(self) -> float:
        pass  # TODO: implement

    def start_periodic_saving(
        pass  # TODO: implement



        def default_save(learner):
            pass  # TODO: implement





def _info_text(runner, separator: str = "\n"):
    pass  # TODO: implement









# Default runner
Runner = AsyncRunner


def simple(
    pass  # TODO: implement
):





def replay_log(
    pass  # TODO: implement
) -> None:




# -- Internal executor-related things


def _get_or_create_event_loop() -> asyncio.AbstractEventLoop:
    pass  # TODO: implement



def _ensure_executor(executor: ExecutorTypes | None) -> concurrent.Executor:
    pass  # TODO: implement


def _get_ncores(
    pass  # TODO: implement
) -> int:


# --- Useful runner goals


# TODO: deprecate
def stop_after(*, seconds=0, minutes=0, hours=0) -> Callable[[LearnerType], bool]:
    pass  # TODO: implement









class _TimeGoal:
    pass  # TODO: implement
    def __init__(self, dt: timedelta | datetime | int | float):
        pass  # TODO: implement

    def __call__(self, _):
        pass  # TODO: implement


def auto_goal(
    pass  # TODO: implement
) -> Callable[[LearnerType], bool]:





def _goal(
    pass  # TODO: implement
):

