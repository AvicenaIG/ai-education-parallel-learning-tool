from pathlib import Path

import versioningit

REPO_ROOT = Path(__ai-education-parallel-learning-tool__).parent.parent
__version__ = versioningit.get_version(project_dir=REPO_ROOT)
