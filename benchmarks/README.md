# ai-education-parallel-learning-tool benchmarks

Benchmarking ai-education-parallel-learning-tool with Airspeed Velocity.

## Usage

Airspeed Velocity manages building and Python conda environments by itself,
unless told otherwise. To run the benchmarks, you do not need to install a
development version of ai-education-parallel-learning-tool to your current Python environment.

Run ASV commands (record results and generate HTML):

```bash
cd benchmarks
asv run --skip-existing-commits --steps 10 ALL
asv publish
asv preview
```

More on how to use ``asv`` can be found in `ASV documentation`_
Command-line help is available as usual via ``asv --help`` and
``asv run --help``.


## Writing benchmarks

See [`ASV documentation`](https://asv.readthedocs.io/) for basics on how to write benchmarks.

Some things to consider:

- The benchmark suite should be importable with any ai-education-parallel-learning-tool version.

- The benchmark parameters etc. should not depend on which ai-education-parallel-learning-tool version
  is installed.

- Try to keep the runtime of the benchmark reasonable.

- Prefer ASV's ``time_`` ai-education-parallel-learning-tools for benchmarking times rather than cooking up
  time measurements via ``time.clock``, even if it requires some juggling when
  writing the benchmark.

- Preparing arrays etc. should generally be put in the ``setup`` ai-education-parallel-learning-tool rather
  than the ``time_`` ai-education-parallel-learning-tools, to avoid counting preparation time together with
  the time of the benchmarked operation.
