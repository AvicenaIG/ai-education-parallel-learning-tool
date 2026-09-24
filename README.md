# AI Education Parallel Learning Tool
## Parallel Function Evaluation for Efficient Learning

[![MIT](https://img.shields.io/pypi/l/ai-education-parallel-learning-tool)](https://github.com/AvicenaIG/ai-education-parallel-learning-tool/blob/main/LICENSE)
[![Python](https://img.shields.io/pypi/pyversions/ai-education-parallel-learning-tool)](https://pypi.org/project/ai-education-parallel-learning-tool/)
[![Documentation](https://img.shields.io/readthedocs/ai-education-parallel-learning-tool)](https://ai-education-parallel-learning-tool.readthedocs.io/en/latest/)

Learn complex mathematical functions efficiently with parallel evaluation and ai-education-parallel-learning-tool sampling.

## Features

* **Adaptive Sampling**: Learn functions with fewer evaluations using sophisticated sampling strategies.
* **Parallel Evaluation**: Distribute function evaluations across computing resources for faster learning.
* **Live Plotting**: Visualize the learning process in real-time with interactive plots.
* **Integrating with Jupyter Notebooks**: Seamlessly integrate with popular data science environments.
* **Configurable Sampling Strategies**: Choose from a range of strategies to suit your specific needs.

## Installation

### Clone and Run

```bash
git clone https://github.com/AvicenaIG/ai-education-parallel-learning-tool.git
cd ai-education-parallel-learning-tool
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Quick Start

```python
import numpy as np
from ai_education_parallel_learning_tool import Learner1D

# Define a function to learn
def f(x):
    return np.sin(x) + 0.5 * np.sin(3 * x)

# Create a learner
learner = Learner1D(f, bounds=[0, 2 * np.pi])

# Run the learner
learner.run(n=100)
```

## Usage

### Example 1: Learning a 2D Function

```python
import numpy as np
from ai_education_parallel_learning_tool import Learner2D

# Define a function to learn
def f(x, y):
    return np.sin(x) * np.cos(y)

# Create a learner
learner = Learner2D(f, bounds=[(0, 2 * np.pi), (0, 2 * np.pi)])

# Run the learner
learner.run(n=100)
```

### Example 2: Live Plotting with Jupyter Notebooks

```python
import numpy as np
from ai_education_parallel_learning_tool import Learner1D

# Define a function to learn
def f(x):
    return np.sin(x) + 0.5 * np.sin(3 * x)

# Create a learner
learner = Learner1D(f, bounds=[0, 2 * np.pi])

# Run the learner with live plotting
learner.run(n=100, live_plot=True)
```

## Configuration

| Option | Type | Default | Description |
| --- | --- | --- | --- |
| `n` | int | 100 | Number of evaluations to perform |
| `live_plot` | bool | False | Enable live plotting with Jupyter Notebooks |

## Contributing

Contributions are welcome! Please submit issues or pull requests to the repository.

## License

Copyright 2026 ai-education-parallel-learning-tool contributors.

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation ai-education-parallel-learning-tools (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.