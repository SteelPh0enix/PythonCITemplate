# Python 3 project template

This repository contains a simple template for Python 3 project with Github Actions for automatic test execution and coverage report/documentation deploy to Github Pages.

## How does it work?

If you are familiar with Github Actions, take a peek into [workflows directory](.github/workflows/). If not, here's long description:

This project is managed by Poetry. Poetry is a tool for managing Python projects and virtual environments, it allows for easy creation of virtualenvs and dependency management. Everything that's related to project management - installing/removing packages, preparing virtual environment and running the code - is done via Poetry.

For development, you can simply go into Poetry shell using `poetry shell` command, and then work in virtualenv. For this repo's CI, we use `poetry run` to execute commands inside it.

Poetry also generates a `pyproject.toml` file, which contains the metadata of project - including the list of packages this project's using. By looking into this file, Poetry sees what packages it needs to install in order to prepare the environment for our code, and we can use it in our CI for quick setup.

Poetry is not a mandatory manager for this type of projects, you can use anything that either has it's own metadata format - like `pipenv` - or just generate `requirements.txt` file. The point is - CI needs to know what packages to install in order to run the tests and generate documentation.

For testing, this project uses [`PyTest`](https://docs.pytest.org/) framework. It's invoked via `poetry run pytest`.
There's also a code formatter ([`black`](https://github.com/psf/black)) and linter ([`flake8`](https://flake8.pycqa.org/en/latest/)) integrated into the CI. You can configure them to automatically check if the code sticks to your project's standard. `black` is currently not configured in CI, so it has to be run manually (`pipenv run black example_app/* tests/*`).

For coverage report generation, [`coverage.py`](https://coverage.readthedocs.io/en/latest/) is used, and for docs - [`sphinx`](https://www.sphinx-doc.org/en/master/).

This project uses Github Actions for automatic testing and docs deployment. Testing workflow is in [`python-app.yml`](.github/workflows/python-app.yml), and pages deployment in [`pages-deploy.yml`](.github/workflows/pages-deploy.yml).

You can check the state of recent workflows [here](https://github.com/SteelPh0enix/PythonCITemplate/actions).

Testing workflow prepares Python environment and installs Poetry, then Poetry installs the project dependencies required for testing, checks the code with `flake8` and runs the tests. It does not install dependencies used only for docs generation, as `docs` group is defined as optional in [`pyproject.toml`](pyproject.toml) file.

Page deployment workflow starts similarly to test workflow, however it does install `docs` group packages with Poetry. Then, it generates docs, coverage report, creates an artifact for Github Pages deployment and uploads it. That's it, that's the magic.
