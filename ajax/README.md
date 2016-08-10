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

**running the app**

`cd ~/Desktop/dev/Ajax/ajax`

`source venv/bin/activate`

`python run.py`

**running the tests**

`cd ~/Desktop/dev/Ajax/ajax`

`source venv/bin/activate`

`nosetests`

## Logging

*import app at the top of the file that you want to add a log statement*

`import app`

`app.app.logger.info('some log message')`

## Migrations

**Creating a migration file**

`alembic revision -m "create account table"`

`alembic -c alembic.ini revision -m "Alerts timestamp"`

**run migration**

`alembic upgrade head`

`alembic -c alembic.ini upgrade head`

**downgrade migration**

`alembic downgrade -1`

`alembic -c alembic.ini downgrade -1`

**get alembic HEAD**

`alembic current`

## New resource

- model
- resource file
- map route to resource
- tests
- migrations (if any)

## Docker

### Dev Environment

`docker-compose up -d`

`source venv/bin/activate`

*Make sure `alembic.ini` has the right `sqlalchemy.url`*

`alembic -c alembic.ini upgrade head`

### Other commands

*Running MySQL server instance inside a docker container*

`docker run -p 3306:3306 --name some-mysql -e MYSQL_ROOT_PASSWORD=my-secret-pw -d mysql:5.6`

*Connect to MySQL from the MySQL command line client*

`docker run -it --link some-mysql:mysql --rm mysql:5.6 sh -c 'exec mysql -h"$MYSQL_PORT_3306_TCP_ADDR" -P"$MYSQL_PORT_3306_TCP_PORT" -uroot -p"$MYSQL_ENV_MYSQL_ROOT_PASSWORD"'`
