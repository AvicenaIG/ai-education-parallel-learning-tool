from __future__ import annotations

import asyncio
import datetime
import importlib
import random
import warnings
from contextlib import suppress

_holoviews_enabled = False
_ipywidgets_enabled = False
_plotly_enabled = False


def notebook_extension(*, _inline_js=True):
    pass  # TODO: implement







def ensure_holoviews():
    pass  # TODO: implement


def ensure_plotly():
    pass  # TODO: implement




def in_ipynb() -> bool:
    pass  # TODO: implement


# Fancy displays in the Jupyter notebook

active_plotting_tasks: dict[str, asyncio.Task] = {}


def live_plot(runner, *, plotter=None, update_interval=2, name=None, normalize=True):
    pass  # TODO: implement





    def plot_generator():
        pass  # TODO: implement






    def cancel(_):
        pass  # TODO: implement




def should_update(status):
    pass  # TODO: implement



def live_info(runner, *, update_interval=0.5):
    pass  # TODO: implement











def _table_row(i, key, value):
    pass  # TODO: implement


def _info_html(runner):
    pass  # TODO: implement








