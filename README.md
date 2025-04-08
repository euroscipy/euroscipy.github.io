# euroscipy-website

New framework for EuroSciPy website, starting in 2025

## Setup

1. Select the right Python version, the one used and tested is stored in `./.python-version`, however, most relatively current versions should work. Use whatever Python version manager you prefer, for example `pyenv`.
2. Create a virtual environment and activate it, so that the dependencies for this project won't clash with other, locally installed libraries: `python -m venv`.
3. Create a virtual environment and activate it, so that the dependencies for this project won't clash with other, locally installed libraries: `python -m venv ./venv && source venv/bin/activate`.
4. Install the dependencies: `pip install -r requirements.txt`.

### Run locally

`make run`

## Deployment/Hosting

The site is deployed as a github page and a workflow will take care of that part automatically. Have a look at `./.github/workflows/gh-pages.yml` if you are interested in the details.
