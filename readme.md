# nuxt-drf

> Django REST project

## Build Setup

``` bash
# Make virtual env
$ python3.5 -m venv venv
#
# Activate virtual env
$ source venv/bin/activate
#
# Upgrade pip
$ pip install pip --upgrade
#
# Install dependencies
$ pip install -r requirements.txt
#
# Then you need rename or copy .env(example) file to file with name .env
$ cp .env\(example\) .env
#
# Migrate
$ python3 manage.py migrate
#
# Create superuser
$ python manage.py createsuperuser
#
# Run server
$ python3 manage.py runserver
```

Frontend (Nuxt.js) (https://github.com/rafizz/nuxt-drf-frontend).
