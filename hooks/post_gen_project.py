import os
import subprocess

env = os.environ.copy()

# Choose Python version
env["PYENV_VERSION"] = "{{ cookiecutter.python_dev_version }}"

# Create virtual environment
subprocess.run(
    [
        "python",
        "-m",
        "venv",
        ".venv",
        "--prompt",
        "{{ cookiecutter.package_distribution_name }}",
    ],
    env=env,
)

# Install the package in editable mode
subprocess.run(
    [
        ".venv/bin/pip",
        "install",
        "-e",
        ".",
    ],
    env=env,
)

# git init
subprocess.run(["git", "init", "-b", "main"])
