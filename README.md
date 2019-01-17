# nuxt-drf

> Django REST project

## Build Setup

``` bash
# (optional) Install python3.7
$ apt install python3.7 python3.7-venv
#
# Make virtual env
$ python3.7 -m venv venv
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
#
# Then you need to edit default django site (/admin/sites/site/1/change/).
# This is to ensure that in the account confirmation email was the correct path to your frontend.
# By default settings in "Domain name" field must be "localhost:3000".
# Note: if your site ID changes and is not equal to "1", do not forget to change the "SITE_ID" variable value in the environment variables file (.env).
```

Frontend (Nuxt.js) (https://github.com/rafizz/nuxt-drf-frontend).
