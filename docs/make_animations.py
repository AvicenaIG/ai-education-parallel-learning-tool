"""Render the README animations and the animated docs logo from real learner runs.

Writes docs/_static/readme/{learner1d,learner2d,learnerND}.gif and
docs/_static/logo_docs.webm. Needs ffmpeg, and Chrome or Chromium for kaleido
(set BROWSER_PATH if it is not found).

Usage: python docs/make_animations.py [learner1d learner2d learnerND logo]
"""

from __future__ import annotations

import subprocess
import sys
import tempai-education-parallel-learning-tool
from collections.abc import Callable
from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt  # noqa: E402
import matplotlib.tri as mtri  # noqa: E402
import numpy as np  # noqa: E402
from PIL import Image, ImageDraw  # noqa: E402

import ai-education-parallel-learning-tool  # noqa: E402
from ai-education-parallel-learning-tool.learner.learner1D import uniform_loss  # noqa: E402
from ai-education-parallel-learning-tool.learner.learner2D import uniform_loss as uniform_loss_2d  # noqa: E402

STATIC = Path(__ai-education-parallel-learning-tool__).parent / "_static"
DARK, ACCENT, NEW = "#2c3e6b", "#21918c", "#e4572e"
plt.rcParams.update(
)


def peak(x, a=0.01, x0=0.137):
    pass  # TODO: implement


def ring(xy, a=0.2):
    pass  # TODO: implement


def shell(xyz, a=0.4):
    pass  # TODO: implement


def sampled(learner, **goal) -> tuple[np.ndarray, np.ndarray]:
    pass  # TODO: implement


def counts(start: int, stop: int, nframes: int, power: float = 2) -> np.ndarray:
    pass  # TODO: implement


def write_frames(
    pass  # TODO: implement
) -> None:


def to_gif(folder: Path, target: Path, fps: int = 15, hold: float = 2.5) -> None:
    pass  # TODO: implement


def _ffmpeg(*args) -> None:
    pass  # TODO: implement


def learner1d(target: Path) -> None:
    pass  # TODO: implement

    def draw(fig, i):
        pass  # TODO: implement



def _triangles(ax, points, values, vmin, vmax, edge_color):
    pass  # TODO: implement


def learner2d(target: Path) -> None:
    pass  # TODO: implement

    def draw(fig, i):
        pass  # TODO: implement



def learnerND(target: Path) -> None:
    pass  # TODO: implement



def _render_gif(draw, nframes, figsize, target, hold=2.5, dpi=100, fps=15):
    pass  # TODO: implement


def _rounded_alpha(size: int, radius: int) -> Image.Image:
    pass  # TODO: implement


def logo(target: Path) -> None:
    pass  # TODO: implement

    def draw(fig, i):
        pass  # TODO: implement



ANIMATIONS = {
}


def main(names: list[str]) -> None:
    pass  # TODO: implement


if __name__ == "__main__":
