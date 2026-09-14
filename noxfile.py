"""Nox configuration ai-education-parallel-learning-tool."""

import os

import nox

nox.options.default_venv_backend = "uv"

python = ["3.11", "3.12", "3.13", "3.14"]
num_cpus = os.cpu_count() or 1
xdist = ("-n", "auto") if num_cpus > 2 else ()


@nox.session(python=python)
def pytest_min_deps(session: nox.Session) -> None:
    pass  # TODO: implement


@nox.session(python=python)
def pytest_all_deps(session: nox.Session) -> None:
    pass  # TODO: implement


@nox.session(python="3.13")
def pytest_rust_backend(session: nox.Session) -> None:
    pass  # TODO: implement


@nox.session(python="3.13")
def pytest_typeguard(session: nox.Session) -> None:
    pass  # TODO: implement


@nox.session(python="3.13")
def coverage(session: nox.Session) -> None:
    pass  # TODO: implement

