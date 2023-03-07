# sotinyurl

Tiny your URL 

[![Built with Cookiecutter Django](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter)](https://github.com/cookiecutter/cookiecutter-django/)
[![Black code style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

## Settings

Moved to [settings](http://cookiecutter-django.readthedocs.io/en/latest/settings.html).

## Basic Commands

Use below command with **sudo** if needed

- **make dev** create local dev server up and running at http://127.0.0.1:8000
- **make build** build/rebuild docker images/containers
- **make migrations** create Django migration files
- **make migrate** execute migration files on database
- **make seed** build local environment + create base data admin user (admin@admin) + 10000 random tiny urls
- **make superuser** create superuser with access to admin panel at http://127.0.0.1:8000/admin/
- **make shell** run django container with shell (python manage.py shell)
- **make cleardocker** Removes installed images/containers/volumes
- **make test** run pytests

## Prefered way to start local enironment

1. clone repo
2. run `make seed` or `sudo make seed` if needed
3. run `make dev` or `sudo make dev`


## Main Urls
- http://127.0.0.1:8000/api/docs/ - swagger API schema
- / - base url will redirect or display error msg. See **sotinyurl.tinyurls.views.catch_tiny_url_view


[App Changelog](/CHANGELOG.md)

---

### Setting Up Your Users

-   To create a **normal user account**, just go to Sign Up and fill out the form. Once you submit it, you'll see a "Verify Your E-mail Address" page. Go to your console to see a simulated email verification message. Copy the link into your browser. Now the user's email should be verified and ready to go.

-   To create a **superuser account**, use this command:

        $ python manage.py createsuperuser

For convenience, you can keep your normal user logged in on Chrome and your superuser logged in on Firefox (or similar), so that you can see how the site behaves for both kinds of users.

### Type checks

Running type checks with mypy:

    $ mypy sotinyurl

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

``` bash
cd sotinyurl
celery -A config.celery_app worker -l info
```

Please note: For Celery's import magic to work, it is important *where* the celery commands are run. If you are in the same folder with *manage.py*, you should be right.

To run [periodic tasks](https://docs.celeryq.dev/en/stable/userguide/periodic-tasks.html), you'll need to start the celery beat scheduler service. You can start it as a standalone process:

``` bash
cd sotinyurl
celery -A config.celery_app beat
```

or you can embed the beat service inside a worker with the `-B` option (not recommended for production use):

``` bash
cd sotinyurl
celery -A config.celery_app worker -B -l info
```

## Deployment

The following details how to deploy this application.

### Docker

See detailed [cookiecutter-django Docker documentation](http://cookiecutter-django.readthedocs.io/en/latest/deployment-with-docker.html).
