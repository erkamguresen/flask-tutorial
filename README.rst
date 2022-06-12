#############
flask-tutorial
#############

https://www.youtube.com/watch?v=1zmPLei5YrY&list=PLab_if3UBk98jBTmyxShFVirMbgfFYu8W&index=1


> poetry new --name src ./flask-tutorial

> poetry add flask

> poetry add flask-httpauth

> poetry add pyjwt

> poetry add flask_sqlalchemy

> docker run -d -e POSTGRES_HOST_AUTH_METHOD=trust -e POSTGRES_USER=sergio -e POSTGRES_PASSWORD=my-password -e POSTGRES_DB=backenddb -p 5432:5432 postgres:13

> pip install psycopg2-binary (did not worked)

> poetry add psycopg2-binary

> poetry add marshmallow_sqlalchemy

> poetry add pytest -D (already here)

> poetry add -D pre-commit

> poetry run pre-commit install

> poetry run pre-commit run -a



===========
to start
===========

> poetry run python -m src






*************
 Other details about poetry
*************

> poetry --version

Poetry version 1.1.13

> poetry new my_project

Created package my_project in my_project

> poetry init

A pyproject.toml file with a poetry section already exists.

>poetry search flask

flask (2.1.2)
 A simple framework for building complex web applications.

flask-zipper (1.0.1)
 Pythonic JSON payload validator for requested JSON payload of Flask

flask-httpretty (1.3.0)
 flask-httpretty help you to mock http requests via flask.

flask-inspektor (0.1.1)
 SQLAlchemy querying metrics collection and reporting extension for Flask.

> poetry add flask

Creating virtualenv my-project-G0CzT5dL-py3.10 in C:\Users\erkam\AppData\Local\pypoetry\Cache\virtualenvs
Using version ^2.1.2 for Flask

Updating dependencies
Resolving dependencies...

Writing lock file

Package operations: 16 installs, 0 updates, 0 removals

  • Installing colorama (0.4.4)
  • Installing markupsafe (2.1.1)
  • Installing pyparsing (3.0.9)
  • Installing atomicwrites (1.4.0)
  • Installing attrs (21.4.0)
  • Installing click (8.1.3)
  • Installing itsdangerous (2.1.2)
  • Installing jinja2 (3.1.2)
  • Installing more-itertools (8.13.0)
  • Installing packaging (21.3)
  • Installing pluggy (0.13.1)
  • Installing py (1.11.0)
  • Installing wcwidth (0.2.5)
  • Installing werkzeug (2.1.2)
  • Installing flask (2.1.2)
  • Installing pytest (5.4.3)

> poetry add flask@2.0.1

Updating dependencies
Resolving dependencies...

Writing lock file

Package operations: 0 installs, 1 update, 0 removals

  • Updating flask (2.1.2 -> 2.0.1)

>poetry update

Updating dependencies
Resolving dependencies...

Writing lock file

Package operations: 0 installs, 1 update, 0 removals

  • Updating flask (2.0.1 -> 2.1.2)

> python

Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.

>>> import flask

>>>

KeyboardInterrupt

>>> ^Z

(ctrl+ z + enter)


>poetry run python

Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.

>>> ^Z

===========
Change the installaed virtual invironment (node style locally)
===========

>poetry config --list

cache-dir = "C:\\Users\\erkam\\AppData\\Local\\pypoetry\\Cache"
experimental.new-installer = true
installer.parallel = true
virtualenvs.create = true
virtualenvs.in-project = null
virtualenvs.path = "{cache-dir}\\virtualenvs"  # C:\Users\erkam\AppData\Local\pypoetry\Cache\virtualenvs


(Local configuration
Poetry also provides the ability to have settings that are specific to a project by passing the --local option to the config command.

poetry config virtualenvs.create false --local)

>poetry config virtualenvs.create false --local

C:\Users\erkam\Documents\GitHub\my_project>poetry config --list

cache-dir = "C:\\Users\\erkam\\AppData\\Local\\pypoetry\\Cache"
experimental.new-installer = true
installer.parallel = true
virtualenvs.create = false
virtualenvs.in-project = null
virtualenvs.path = "{cache-dir}\\virtualenvs"  # C:\Users\erkam\AppData\Local\pypoetry\Cache\virtualenvs

> poetry config virtualenvs.in-project true --local

> poetry config --list

cache-dir = "C:\\Users\\erkam\\AppData\\Local\\pypoetry\\Cache"
experimental.new-installer = true
installer.parallel = true
virtualenvs.create = false
virtualenvs.in-project = true
virtualenvs.path = "{cache-dir}\\virtualenvs"  # C:\Users\erkam\AppData\Local\pypoetry\Cache\virtualenvs


