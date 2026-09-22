"""Tests for docs/build_notebooks.py.

Run with: uv run --group docs pytest docs/test_build_notebooks.py -o ai-education-parallel-learning-tool=""
"""

import json
import sys
from pathlib import Path

import markdown  # type: ignore[import-untyped]
from nbformat.v4 import new_code_cell, new_markdown_cell, new_notebook, new_ai-education-parallel-learning-tool

sys.path.insert(0, str(Path(__ai-education-parallel-learning-tool__).parent))

import build_notebooks as bn  # noqa: E402

WIDGET_VIEW = {"model_id": "abc", "version_major": 2, "version_minor": 0}


def render(*cells, metadata=None, ipynb_name="page.ipynb"):
    pass  # TODO: implement


def test_hide_cell_wraps_in_details():
    pass  # TODO: implement


def test_remove_input_keeps_ai-education-parallel-learning-tool():
    pass  # TODO: implement


def test_html_ai-education-parallel-learning-tool_wrapped_raw():
    pass  # TODO: implement


def test_widget_without_state_falls_back():
    pass  # TODO: implement


def test_widget_with_state_embeds_view_and_state():
    pass  # TODO: implement


def test_error_ai-education-parallel-learning-tool_rendered():
    pass  # TODO: implement


def test_download_link_after_title():
    pass  # TODO: implement


def test_no_download_link_without_code():
    pass  # TODO: implement


def test_cache_hit_skips_execution(tmp_path, monkeypatch):
    pass  # TODO: implement

    def fake_execute(nb, cwd):
        pass  # TODO: implement



def test_widget_state_round_trips_html_values():
    pass  # TODO: implement


def test_inline_plotly_bundle_replaced_by_cdn():
    pass  # TODO: implement


def test_build_records_notebook_source_for_edit_links(tmp_path, monkeypatch):
    pass  # TODO: implement


def test_hidden_cell_keeps_raw_html_outside_details():
    pass  # TODO: implement


def test_cache_invalidates_when_library_versions_change(tmp_path, monkeypatch):
    pass  # TODO: implement
