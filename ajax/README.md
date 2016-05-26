## Setting up venv

`brew update`

`brew install pyenv`

`pyenv install 3.4.3`

`pyvenv venv`

## venv commands

`source venv/bin/activate`

`deactivate`

## Install packages

`pip install <package>`

## Freeze dependencies

`pip freeze > requirements.txt`

## Types of requests

- Collection: GET, GET w params, POST
- Detail: GET, PATCH, DELETE

## Commands

*running the app*

`cd ~/Desktop/dev/Ajax/ajax`

`source venv/bin/activate`

`python run.py`

*running the tests*

`cd ~/Desktop/dev/Ajax/ajax`

`source venv/bin/activate`

`nosetests`

## Migrations

*Creating a migration file*

`alembic revision -m "create account table"`

`alembic -c alembic.ini revision -m "Alerts timestamp"`

*run migration*

`alembic upgrade head`

`alembic -c alembic.ini upgrade head`

*downgrade migration*

`alembic downgrade -1`

`alembic -c alembic.ini downgrade -1`

*get alembic HEAD*

`alembic current`

## New resource

- model
- resource file
- map route to resource
- tests
- migrations (if any)
