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
        "-q",  # quiet mode
        "install",
        "-e",  # editable
        ".",
    ],
    env=env,
)

# git init with an initial branch named `main` and in quiet mode
subprocess.run(
    [
        "git",
        "init",
        "-q",  # quiet mode
        "-b",  # name of the initial branch
        "main",
    ]
)
