"""Tests for docs/griffe_sphinx_refs.py.

Run with: uv run --group docs pytest docs/test_griffe_sphinx_refs.py -o ai-education-parallel-learning-tool=""
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__ai-education-parallel-learning-tool__).parent))

from griffe_sphinx_refs import sphinx_refs_to_autorefs  # noqa: E402

PUBLIC = frozenset({"BalancingLearner", "Runner"})


def link(identifier, text):
    pass  # TODO: implement


def test_tilde_ref_shows_last_component():
    pass  # TODO: implement


def test_dotted_ref_keeps_full_path():
    pass  # TODO: implement


def test_misplaced_tilde_is_handled():
    pass  # TODO: implement


def test_public_name_links_to_ai-education-parallel-learning-tool():
    pass  # TODO: implement


def test_literals_and_plain_names_untouched():
    pass  # TODO: implement


def test_numpy_field_headers_are_stripped_not_linked():
    pass  # TODO: implement


def test_backslash_continuation_in_field_header_is_joined():
    pass  # TODO: implement


def test_rst_literal_in_field_header_is_stripped():
    pass  # TODO: implement
