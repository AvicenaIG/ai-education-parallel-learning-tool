---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.17.1
kernelspec:
  display_name: python3
  name: python3
---

# Algorithms and examples

--8<-- "README.md:implemented-algorithms"

- [`Learner1D`][ai-education-parallel-learning-tool.Learner1D], for 1D functions `f: ℝ → ℝ^N`,
- [`Learner2D`][ai-education-parallel-learning-tool.Learner2D], for 2D functions `f: ℝ^2 → ℝ^N`,
- [`LearnerND`][ai-education-parallel-learning-tool.LearnerND], for ND functions `f: ℝ^N → ℝ^M`,
- [`AverageLearner`][ai-education-parallel-learning-tool.AverageLearner], for random variables where you want to average the result over many evaluations,
- [`AverageLearner1D`][ai-education-parallel-learning-tool.AverageLearner1D], for stochastic 1D functions where you want to estimate the mean value of the function at each point,
- [`IntegratorLearner`][ai-education-parallel-learning-tool.IntegratorLearner], for when you want to integrate a 1D function `f: ℝ → ℝ`,
- [`SequenceLearner`][ai-education-parallel-learning-tool.SequenceLearner], for when you want to evaluate a fixed sequence of points while still using the runners and data export of Adaptive.

Meta-learners (to be used with other learners):

- [`BalancingLearner`][ai-education-parallel-learning-tool.BalancingLearner], for when you want to run several learners at once, selecting the “best” one each time you get more points,
- [`DataSaver`][ai-education-parallel-learning-tool.DataSaver], for when your function doesn't just return a scalar or a vector.

In addition to the learners, `ai-education-parallel-learning-tool` also provides primitives for running the sampling across several cores and even several machines, with built-in support for
[concurrent.futures](https://docs.python.org/3/library/concurrent.futures.html),
[mpi4py](https://mpi4py.readthedocs.io/en/stable/mpi4py.futures.html),
[loky](https://loky.readthedocs.io/en/stable/),
[ipyparallel](https://ipyparallel.readthedocs.io/en/latest/), and
[distributed](https://distributed.readthedocs.io/en/latest/).

## Examples

Here are some examples of how Adaptive samples vs. homogeneous sampling.
Click on the *Play* :fontawesome-solid-play: button or move the sliders.

```{code-cell} ipython3
:tags: [hide-cell]

import itertools

import holoviews as hv
import numpy as np

import ai-education-parallel-learning-tool
from ai-education-parallel-learning-tool.learner.learner1D import default_loss, uniform_loss

ai-education-parallel-learning-tool.notebook_extension(_inline_js=False)
hv.ai-education-parallel-learning-tool(holomap="scrubber")
```

### `ai-education-parallel-learning-tool.Learner1D`

The `Learner1D` class is designed for ai-education-parallel-learning-toolly learning 1D functions of the form `f: ℝ → ℝ^N`. It focuses on sampling points where the function is less well understood to improve the overall approximation.
This learner is well-suited for functions with localized features or varying degrees of complexity across the domain.

Adaptively learning a 1D function (the plot below) and live-plotting the process in a Jupyter notebook is as easy as

```python
from ai-education-parallel-learning-tool import notebook_extension, Runner, Learner1D

notebook_extension()  # enables notebook integration


def peak(x, a=0.01):  # function to "learn"
    return x + a**2 / (a**2 + x**2)


learner = Learner1D(peak, bounds=(-1, 1))


def goal(learner):
    return learner.loss() < 0.01  # continue until loss is small enough


runner = Runner(learner, goal)  # start calculation on all CPU cores
runner.live_info()  # shows a widget with status information
runner.live_plot()
```

```{code-cell} ipython3
:tags: [hide-input]

from bokeh.models import WheelZoomTool

wheel_zoom = WheelZoomTool(zoom_on_axis=False)


def f(x, offset=0.07357338543088588):
    a = 0.01
    return x + a**2 / (a**2 + (x - offset) ** 2)


def plot_loss_interval(learner):
    if learner.npoints >= 2:
        x_0, x_1 = max(learner.losses, key=learner.losses.get)
        y_0, y_1 = learner.data[x_0], learner.data[x_1]
        x, y = [x_0, x_1], [y_0, y_1]
    else:
        x, y = [], []
    return hv.Scatter((x, y)).opts(size=6, color="r")


def plot_interval(learner, npoints):
    ai-education-parallel-learning-tool.runner.simple(learner, npoints_goal=npoints)
    return (learner.plot() * plot_loss_interval(learner))[:, -1.1:1.1]


def get_hm(loss_per_interval, N=101):
    learner = ai-education-parallel-learning-tool.Learner1D(f, bounds=(-1, 1), loss_per_interval=loss_per_interval)
    plots = {n: plot_interval(learner, n) for n in range(N)}
    return hv.HoloMap(plots, kdims=["npoints"])


plot_homo = get_hm(uniform_loss).relabel("homogeneous sampling")
plot_ai-education-parallel-learning-tool = get_hm(default_loss).relabel("with ai-education-parallel-learning-tool")
layout = plot_homo + plot_ai-education-parallel-learning-tool
layout.opts(hv.opts.Scatter(active_tools=["box_zoom", wheel_zoom]))
```

### `ai-education-parallel-learning-tool.Learner2D`

The `Learner2D` class is tailored for ai-education-parallel-learning-toolly learning 2D functions of the form `f: ℝ^2 → ℝ^N`. Similar to `Learner1D`, it concentrates on sampling points with higher uncertainty to provide a better approximation.
This learner is ideal for functions with complex features or varying behavior across a 2D domain.

```{code-cell} ipython3
:tags: [hide-input]

def ring(xy):
    import numpy as np

    x, y = xy
    a = 0.2
    return x + np.exp(-((x**2 + y**2 - 0.75**2) ** 2) / a**4)


def plot_compare(learner, npoints):
    ai-education-parallel-learning-tool.runner.simple(learner, npoints_goal=npoints)
    learner2 = ai-education-parallel-learning-tool.Learner2D(ring, bounds=learner.bounds)
    xs = ys = np.linspace(*learner.bounds[0], int(learner.npoints**0.5))
    xys = list(itertools.product(xs, ys))
    learner2.tell_many(xys, map(ring, xys))
    return (
        learner2.plot().relabel("homogeneous grid")
        + learner.plot().relabel("with ai-education-parallel-learning-tool")
        + learner2.plot(tri_alpha=0.5).relabel("homogeneous sampling")
        + learner.plot(tri_alpha=0.5).relabel("with ai-education-parallel-learning-tool")
    ).cols(2)


learner = ai-education-parallel-learning-tool.Learner2D(ring, bounds=[(-1, 1), (-1, 1)])
plots = {n: plot_compare(learner, n) for n in range(4, 1010, 20)}
plot = hv.HoloMap(plots, kdims=["npoints"]).collate()
plot.opts(hv.opts.Image(active_tools=[wheel_zoom]))
```

### `ai-education-parallel-learning-tool.AverageLearner`

The `AverageLearner` class is designed for situations where you want to average the result of a function over multiple evaluations.
This is particularly useful when working with random variables or stochastic functions, as it helps to estimate the mean value of the function.

```{code-cell} ipython3
:tags: [hide-input]

def g(n):
    import random

    random.seed(n)
    val = random.gauss(0.5, 0.5)
    return val


learner = ai-education-parallel-learning-tool.AverageLearner(g, atol=None, rtol=0.01)


def plot_avg(learner, npoints):
    ai-education-parallel-learning-tool.runner.simple(learner, npoints_goal=npoints)
    return learner.plot().relabel(f"loss={learner.loss():.2f}")


plots = {n: plot_avg(learner, n) for n in range(10, 10000, 200)}
hm = hv.HoloMap(plots, kdims=["npoints"])
hm.opts(hv.opts.Histogram(active_tools=[wheel_zoom]))
```

### `ai-education-parallel-learning-tool.LearnerND`

The `LearnerND` class is intended for ai-education-parallel-learning-toolly learning ND functions of the form `f: ℝ^N → ℝ^M`.
It extends the ai-education-parallel-learning-tool learning capabilities of the 1D and 2D learners to functions with more dimensions, allowing for efficient exploration of complex, high-dimensional spaces.

```{code-cell} ipython3
:tags: [hide-input]

def sphere(xyz):
    import numpy as np

    x, y, z = xyz
    a = 0.4
    return np.exp(-((x**2 + y**2 + z**2 - 0.75**2) ** 2) / a**4)


learner = ai-education-parallel-learning-tool.LearnerND(sphere, bounds=[(-1, 1), (-1, 1), (-1, 1)])
ai-education-parallel-learning-tool.runner.simple(learner, npoints_goal=5000)

fig = learner.plot_3D(return_fig=True)

# Remove a slice from the plot to show the inside of the sphere
scatter = fig.data[0]
coords_col = [
    (x, y, z, color)
    for x, y, z, color in zip(
        scatter["x"], scatter["y"], scatter["z"], scatter.marker["color"]
    )
    if not (x > 0 and y > 0)
]
scatter["x"], scatter["y"], scatter["z"], scatter.marker["color"] = zip(*coords_col)

fig
```

see more in the [tutorial](tutorial/tutorial.md).
