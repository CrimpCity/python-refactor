## Overview
This project refactors this web scraping code example [here](https://towardsdatascience.com/web-scraping-html-tables-with-python-c9baba21059) by Syed Sadat Nazrul.

The goals of the refactor are:
1. Completeness
2. Reproducibility
3. Maintainability
4. Modularity

I achieve these goals by using pipenv to setup a virtual env, and install the necessary dependencies.
Additionally, the project structure is clean and rational with the test directory matching the source directory file
structure. I've also added a command line interface using click to easily run commands from the terminal.

After the refactor I compare my approach with Conor Hoekstra's [here](https://youtu.be/W-lZttZhsUY).
The main updates I make from Conor's code is I replace an enumeration with list slicing and I remove
unnecessary tuple unpacking in favor of explicitly defining the data and data column names separately.

His last point about using pandas web scraping is interesting but I learned more without that magical function.

## Development installation
To install pyenv automatically follow [this link](https://github.com/pyenv/pyenv-installer#install)
with install instructions. If you run into issues with the installer or would like to install
automatically, try following the manual instructions [here](https://github.com/pyenv/pyenv#installation)

You can verify that pyenv installed properly by running the following commands:

```commandline
# Should run and show commands usable with pyenv
pyenv --help

# Should show /Users/{user}/.pyenv/shims:/ in $PATH before any other python installations
echo $PATH
```

#### Clone the Project repository

1. Clone this repo using ssh:

```commandline
git clone git@github.com:{project-home}/{repo-name}.git
```

2. In a command prompt or terminal, navigate to the head of the directory:

```commandline
cd {repo-name}
```

NOTE: if you were previously running in an older version of Python and are using the
same path, the virtual environment in `pipenv` is sticky. You will need to run the
following commands first:

3. Run the following commands to install the version of python needed by the project,
   setup a virtual env using pipenv, and install the necessary dependencies into the
   pipenv.

```commandline
# Installs the version of python specified in the .python_version file.
pyenv install

# Installs pipenv for the version of python installed by pyenv
pip install pipenv

# Removes any pipenv environments that might be associated
pipenv --rm

# Installs core project production dependencies and dev dependencies into a virtual environment
pipenv install --dev

# Activates pipenv in current terminal
pipenv shell
```

NOTE: never use `pipenv install --dev --ignore-pipfile` during development. This will
cause Pipenv to ignore changes to the Pipfile and prevent it from adding the
current environment to Pipfile.lock. Essentially, new dependencies a developer added will
not be considered.

4. Optionally, you can install new packages at any time and have them available
   in your `Pipfile`. Make sure you `git add` both `Pipfile` and `Pipfile.lock`
   when you create your PR.

```
pipenv install your-favorite-package
```


## Local Development
After the development dependencies are installed via
```
pipenv install --dev
```
Activate the virtual environment through:
```
pipenv shell
```

You may begin local code development.

NOTE:
1. Upon every new virtual environment activation command i.e. `pipenv shell` you will need to also run `pre-commit install` to run pre-commit locally. You can check that pre-commit hooks are working locally by running `pre-commit run --all-files`.
2. In order for `pre-commit` to work the project must be in a properly set up github repository.
3. If your work requires you to add any new packages to the Pipfile this will require you to rebuild your entire virtual environment in order to get the new packages. Optionally you may install packages into the current virtual environment though this will not be persistent using `pipenv install your-favorite-package`
4. If you need to modify any dot files like `.pre-commit.yml` then for these changes to take effect you will need to rebuild your virtual environment.


## Running Tests
Unit tests are located under tests/unit.

#### Testing with your local python (via Pipenv) environment

Use `pytest` to run all of the unit tests. It can be as simple as:

```pytest```

To run a specific set of tests, specify the directory.


## Deployment Process
#### To DEV Environment
The main branch of the repo is the dev environment and is configured with all other dev environments.

#### To STG Environment
1. Draft a release
2. Tag it with today's date using the YEAR-MONTH-DAY format
3. Target the main branch
4. Click the pre-release checkbox making sure that it is checked
5. You do not need to provide a description since one will be automatically generated from the commit history
6. Click publish release

#### To PRD Environment
1. Select the release in the STG environment you wish to release to production
2. Uncheck the pre-release checkbox
3. Click publish release
4. You do not need to provide a description since one will be automatically generated from the commit history
