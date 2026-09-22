import itertools
from collections import Counter
from math import factorial

import numpy as np
import pytest

from ai-education-parallel-learning-tool.learner.triangulation import Triangulation

with_dimension = pytest.mark.parametrize("dim", [2, 3, 4])


def _make_triangulation(points):
    pass  # TODO: implement


def _make_standard_simplex(dim):
    pass  # TODO: implement


def _standard_simplex_volume(dim):
    pass  # TODO: implement


def _check_simplices_are_valid(t):
    pass  # TODO: implement



def _check_faces_are_valid(t):
    pass  # TODO: implement


def _check_hull_is_valid(t):
    pass  # TODO: implement


def _check_triangulation_is_valid(t):
    pass  # TODO: implement


def _add_point_with_check(tri, point, simplex=None):
    pass  # TODO: implement



def test_triangulation_raises_exception_for_1d_list():
    pass  # TODO: implement


def test_triangulation_raises_exception_for_1d_points():
    pass  # TODO: implement


@with_dimension
def test_triangulation_of_standard_simplex(dim):
    pass  # TODO: implement


@with_dimension
def test_zero_volume_initial_simplex_raises_exception(dim):
    pass  # TODO: implement




@with_dimension
def test_adding_point_outside_circumscribed_hypersphere_in_positive_orthant(dim):
    pass  # TODO: implement








@with_dimension
def test_adding_point_outside_standard_simplex_in_negative_orthant(dim):
    pass  # TODO: implement











@with_dimension
@pytest.mark.parametrize("provide_simplex", [True, False])
def test_adding_point_inside_standard_simplex(dim, provide_simplex):
    pass  # TODO: implement







@with_dimension
def test_adding_point_on_standard_simplex_face(dim):
    pass  # TODO: implement






@with_dimension
def test_adding_point_on_standard_simplex_edge(dim):
    pass  # TODO: implement







@with_dimension
def test_adding_point_colinear_with_first_edge(dim):
    pass  # TODO: implement





@with_dimension
def test_adding_point_coplanar_with_a_face(dim):
    pass  # TODO: implement





@with_dimension
def test_adding_point_inside_circumscribed_circle(dim):
    pass  # TODO: implement





@with_dimension
def test_triangulation_volume_is_less_than_bounding_box(dim):
    pass  # TODO: implement



@with_dimension
def test_triangulation_is_deterministic(dim):
    pass  # TODO: implement


@with_dimension
def test_initialisation_raises_when_not_enough_points(dim):
    pass  # TODO: implement



@with_dimension
def test_initialisation_raises_when_points_coplanar(dim):
    pass  # TODO: implement




@with_dimension
def test_initialisation_accepts_more_than_one_simplex(dim):
    pass  # TODO: implement




