# opencv-pixelator

Project to practice using pipenv and refresh image processing skills

## Setup

1. If it is not already installed, run `pip install --user pipenv` to install pipenv on your system. This assumes that you already have python on your system.
2. Run `pipenv install` to install the dependencies associated with this project.
3. To activate a shell with the pipenv enviromment set up run `pipenv shell`. Otherwise to just launch the python program, run `pipenv run python3 -m main.py`

## Takeaway from this project

I feel like having a `requirements.txt` file is just much easier than using `pipenv`. `pipenv` feels out of place and after-the-fact in Python, so just using a requirements file with a virtual environment to share code feels much more straightforward.

In a brief search `pipreqs` is something that can generate a `requirements.txt` file for you. Otherwise, `pip freeze > requirements.txt` pulls all installed pip packages into a file. Use this carefully and probably with `pipenv` or you will pull system-wide pip installs into dependencies.
