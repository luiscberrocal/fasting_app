# Fasting App

App to keep track of your fasting habits

[![Built with Cookiecutter Django](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter)](https://github.com/cookiecutter/cookiecutter-django/)
[![Black code style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

License: MIT

## Settings

Moved to [settings](http://cookiecutter-django.readthedocs.io/en/latest/settings.html).

## Basic Commands

### Setting Up Your Users

- To create a **normal user account**, just go to Sign Up and fill out the form. Once you submit it, you'll see a "Verify Your E-mail Address" page. Go to your console to see a simulated email verification message. Copy the link into your browser. Now the user's email should be verified and ready to go.

- To create a **superuser account**, use this command:

      $ python manage.py createsuperuser

For convenience, you can keep your normal user logged in on Chrome and your superuser logged in on Firefox (or similar), so that you can see how the site behaves for both kinds of users.

### Type checks

Running type checks with mypy:

    $ mypy fasting_app

### Test coverage

To run the tests, check your test coverage, and generate an HTML coverage report:

    $ coverage run -m pytest
    $ coverage html
    $ open htmlcov/index.html

#### Running tests with pytest

    $ pytest

### Live reloading and Sass CSS compilation

Moved to [Live reloading and SASS compilation](https://cookiecutter-django.readthedocs.io/en/latest/developing-locally.html#sass-compilation-live-reloading).

### Celery

This app comes with Celery.

To run a celery worker:

```bash
cd fasting_app
celery -A config.celery_app worker -l info
```

Please note: For Celery's import magic to work, it is important _where_ the celery commands are run. If you are in the same folder with _manage.py_, you should be right.

To run [periodic tasks](https://docs.celeryq.dev/en/stable/userguide/periodic-tasks.html), you'll need to start the celery beat scheduler service. You can start it as a standalone process:

```bash
cd fasting_app
celery -A config.celery_app beat
```

or you can embed the beat service inside a worker with the `-B` option (not recommended for production use):

```bash
cd fasting_app
celery -A config.celery_app worker -B -l info
```

## Deployment

The following details how to deploy this application.

# Short cuts

```shell
#Docker commands
export DOCKER_USER="$(id -u):$(id -g)"
alias d-build='docker stop $(docker ps -q -a) && docker-compose -f local.yml build'
alias d-arg-build='docker stop $(docker ps -q -a) && docker-compose -f local.yml build --build-arg PYPI_TOKEN=${PYPI_TOKEN}'
alias d-up='docker stop $(docker ps -q -a) && docker-compose -f local.yml up'
alias d-manage='docker stop $(docker ps -q -a) && docker-compose -f local.yml run django python manage.py'
alias d-django-exec="docker exec -it $(docker ps | grep local_django | awk '{print  $1 " bash"}' )"
alias d-superuser='docker stop $(docker ps -qa) && docker-compose -f local.yml run django python manage.py createsuperuser --username="luiscberrocal" --email="luis.berrocal@payjoy.com"'
alias gpt="git push --tag"
d-bash-django() { docker exec -it $(docker ps | grep django | awk '{print $1}') bash }
d-stop() { docker stop $(docker ps -a -q); }
 
# Python commands
alias pi='pip install'
alias bppa='bump2version patch'
alias bpmi='bump2version minor'
alias bpma='bump2version major'
alias relpa='bump2version patch --list --dry-run --allow-dirty | grep new_version | grep -E -o "[0-9]+.[0-9]+.[0-9]+$" | xargs git flow release start '
alias relmi='bump2version minor --list --dry-run --allow-dirty | grep new_version | grep -E -o "[0-9]+.[0-9]+.[0-9]+$" | xargs git flow release start '
alias relma='bump2version major --list --dry-run --allow-dirty | grep new_version | grep -E -o "[0-9]+.[0-9]+.[0-9]+$" | xargs git flow release start '
alias hotfix='bump2version patch --list --dry-run --allow-dirty | grep new_version | grep -E -o "[0-9]+.[0-9]+.[0-9]+$" | xargs git flow hotfix start '

```

### Docker

See detailed [cookiecutter-django Docker documentation](http://cookiecutter-django.readthedocs.io/en/latest/deployment-with-docker.html).
