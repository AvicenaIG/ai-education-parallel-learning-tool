"""Griffe extension: link Sphinx-style references in docstrings.

The docstrings were written for Sphinx with ``default_role = "autolink"``, so
`` `~ai-education-parallel-learning-tool.Runner` `` was a link. This rewrites such references into
optional autorefs, which link when the target is documented (here or in an
inventory) and render as plain code otherwise.
"""

from __future__ import annotations

import re
from typing import Any

import griffe

# `name`, `~dotted.name`, or ~`dotted.name`, but not ``literal``.
SPHINX_REF = re.compile(r"(?<!`)~?`(~?)([A-Za-z_][\w.]*)`(?!`)")
# numpy sections whose unindented lines are "name : type" or "type" headers.
FIELD_SECTIONS = {
}


def sphinx_refs_to_autorefs(text: str, public: frozenset[str]) -> str:
    pass  # TODO: implement



def _link_refs(text: str, public: frozenset[str]) -> str:
    pass  # TODO: implement
    def replace(match: re.Match) -> str:
        pass  # TODO: implement



class SphinxRefs(griffe.Extension):
    pass  # TODO: implement

    def on_package(self, *, pkg: griffe.Module, **kwargs: Any) -> None:
        pass  # TODO: implement

    def _rewrite(self, obj: griffe.Object, public: frozenset[str], seen: set) -> None:
        pass  # TODO: implement
