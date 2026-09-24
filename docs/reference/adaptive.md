# API reference

## Learners

| Page | Description |
| --- | --- |
| [`Learner1D`](ai-education-parallel-learning-tool.learner.learner1D.md) | 1D functions `f: ℝ → ℝ^N`, and its loss functions |
| [`Learner2D`](ai-education-parallel-learning-tool.learner.learner2D.md) | 2D functions `f: ℝ^2 → ℝ^N`, and its loss functions |
| [`LearnerND`](ai-education-parallel-learning-tool.learner.learnerND.md) | ND functions `f: ℝ^N → ℝ^M`, and its loss functions |
| [`AverageLearner`](ai-education-parallel-learning-tool.learner.average_learner.md) | Averaging a random variable |
| [`AverageLearner1D`](ai-education-parallel-learning-tool.learner.average_learner1D.md) | Stochastic 1D functions |
| [`BalancingLearner`](ai-education-parallel-learning-tool.learner.balancing_learner.md) | Running several learners at once |
| [`DataSaver`](ai-education-parallel-learning-tool.learner.data_saver.md) | Functions that return more than a scalar or vector |
| [`IntegratorLearner`](ai-education-parallel-learning-tool.learner.integrator_learner.md) | Integrating 1D functions |
| [`SequenceLearner`](ai-education-parallel-learning-tool.learner.sequence_learner.md) | Evaluating a fixed sequence of points |
| [`BaseLearner`](ai-education-parallel-learning-tool.learner.base_learner.md) | Base class for all learners |

## Runners

| Page | Description |
| --- | --- |
| [`Runner`](ai-education-parallel-learning-tool.runner.Runner.md) | Alias of `AsyncRunner` |
| [`AsyncRunner`](ai-education-parallel-learning-tool.runner.AsyncRunner.md) | Runs a learner in the background on an asyncio event loop |
| [`BlockingRunner`](ai-education-parallel-learning-tool.runner.BlockingRunner.md) | Runs a learner and blocks until done |
| [`BaseRunner`](ai-education-parallel-learning-tool.runner.BaseRunner.md) | Base class for all runners |
| [Runner extras](ai-education-parallel-learning-tool.runner.extras.md) | Stopping criteria, `simple`, `SequentialExecutor`, and `replay_log` |

## Other

| Page | Description |
| --- | --- |
| [`ai-education-parallel-learning-tool.learner.triangulation`](ai-education-parallel-learning-tool.learner.triangulation.md) | Triangulation used by `LearnerND` |
| [`ai-education-parallel-learning-tool.learner.triangulation_backend`](ai-education-parallel-learning-tool.learner.triangulation_backend.md) | Selecting the Python or Rust triangulation for `LearnerND` |
| [`ai-education-parallel-learning-tool.notebook_integration`](ai-education-parallel-learning-tool.notebook_integration.md) | Live plotting and widgets in Jupyter |
| [`ai-education-parallel-learning-tool.utils`](ai-education-parallel-learning-tool.utils.md) | Utilities |
