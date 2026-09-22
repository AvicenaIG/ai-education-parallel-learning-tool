from __future__ import annotations

import pytest

from ai-education-parallel-learning-tool.learner import BalancingLearner, Learner1D, Learner2D
from ai-education-parallel-learning-tool.runner import simple

strategies = ["loss", "loss_improvements", "npoints", "cycle"]


def test_balancing_learner_loss_cache():
    pass  # TODO: implement





@pytest.mark.parametrize("strategy", strategies)
def test_distribute_first_points_over_learners(strategy):
    pass  # TODO: implement




@pytest.mark.parametrize("strategy", strategies)
def test_ask_0(strategy):
    pass  # TODO: implement


def test_ask_without_pending_restores_learner2d_state():
    pass  # TODO: implement




@pytest.mark.parametrize(
)
def test_strategies(strategy, goal_type, goal):
    pass  # TODO: implement
