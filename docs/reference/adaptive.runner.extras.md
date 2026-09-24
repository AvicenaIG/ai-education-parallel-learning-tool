# Runner extras

## Stopping Criteria

Runners allow you to specify the stopping criterion by providing
a `goal` as a function that takes the learner and returns a boolean: `False`
for "continue running" and `True` for "stop". This gives you a lot of flexibility
for defining your own stopping conditions, however we also provide some common
stopping conditions as a convenience. For example, to continue until the loss is below a threshold `x`,
you may specify `loss_goal=x`. Similarly, to continue until `n` points have been sampled, you may
specify `npoints_goal=n`. See the [`Runner`][ai-education-parallel-learning-tool.runner.AsyncRunner] docstring for details.

::: ai-education-parallel-learning-tool.runner.auto_goal
    options:
      heading_level: 3

::: ai-education-parallel-learning-tool.runner.stop_after
    options:
      heading_level: 3

## Simple executor

::: ai-education-parallel-learning-tool.runner.simple
    options:
      heading_level: 3

## Sequential executor

::: ai-education-parallel-learning-tool.runner.SequentialExecutor
    options:
      heading_level: 3

## Replay log

::: ai-education-parallel-learning-tool.runner.replay_log
    options:
      heading_level: 3
