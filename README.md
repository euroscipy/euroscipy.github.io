# EuroScipy Website

New framework for EuroSciPy website, starting 2025.

## Setup

1. Select the right Python version, the one used and tested is stored in `./.python-version`, however, most relatively current versions should work. Use whatever Python version manager you prefer, for example `pyenv`.
2. Create a virtual environment and activate it, so that the dependencies for this project won't clash with other, locally installed libraries: `python -m venv ./venv && source venv/bin/activate`.
3. Install the dependencies: `pip install -r requirements.txt`.


## Alternative Setup Instructions

1. **Install Pixi:** Visit [https://pixi.sh/latest/#installation](https://pixi.sh/latest/#installation) to download and install the appropriate version of Pixi for your operating system.
2. **Activate the Pixi Environment:**  After installing Pixi, open a terminal in your local clone of the project repository and run the command `pixi shell` to activate the development environment.


### Run locally

`make run`

## Deployment/Hosting

The site is deployed as a github page and a workflow will take care of that part automatically. Have a look at `./.github/workflows/gh-pages.yml` if you are interested in the details.

## Content

Here is how you can add content like sponsors or blog posts to the EuroSciPy website.

### Blog Posts

1. Create a new branch
2. Add a folder for the new blog post under `./content/blog/<blogpost-title>`
3. Add a `contents.lr` file to this folder.

This file will contain the blog post (as markdown) and some additional metadata. Here is an example on how this could look like:

```
title: Something exciting just happened!
---
pub_date: 2025-05-07
---
body:

# The air is thrumming with excitement

Something unbelievable just happened in the **Python** world. Let me tell you all about it:
```

The `title` field is a simple string.

The `pub_date` field is the date, formatted like this: YYYY-mm-dd.

the `body` is the blog post as markdown.

4. Commit the changes to your new branch
5. Push the changes
6. Open a PR
7. Merge the PR, once it has been approved

The new blog post will automatically be deployed, once it has been merged.

Add any images you might want to use to the same folder you added the `contents.lr` file to, so that all the content is contained in one place.
