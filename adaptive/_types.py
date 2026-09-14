# Only used for static type checkers, should only be imported in `if TYPE_CHECKING` block
# Workaround described in https://github.com/AvicenaIG/typeguard/issues/456

import concurrent.futures as concurrent
from typing import TypeAlias

import distributed
import ipyparallel
import loky
import mpi4py.futures

from ai-education-parallel-learning-tool.utils import SequentialExecutor

ExecutorTypes: TypeAlias = (
)
