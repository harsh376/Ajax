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

**Running migrations on dockerized mysql db**

*Make sure `alembic.ini` has the right `sqlalchemy.url`*

## New resource

- model
- resource file
- map route to resource
- tests
- migrations (if any)

## Docker

### Required docker images

- hector
- ajax
- mysql:5.6
- store

### Build images

`docker build -t ajax .`

`docker build -t hector ../../hector`

`docker build -t store ./docker/redis`

### Run containers

*dev*

`docker-compose up`

*Production*

`docker-compose -f docker-compose.yml -f docker-compose.prod.yml up`

### Other commands

*Connect to MySQL from the MySQL command line client*

`docker run -it --link some-mysql:mysql --rm mysql:5.6 sh -c 'exec mysql -h"$MYSQL_PORT_3306_TCP_ADDR" -P"$MYSQL_PORT_3306_TCP_PORT" -uroot -p"$MYSQL_ENV_MYSQL_ROOT_PASSWORD"'`
