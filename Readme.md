# Curated Search

Built on top of one of my templates. Includes:

- pages app
- users app
- custom user model (email instead of username)
- e-mail verification
- django debug toolbar (only in development)
- docker files for spinning up containers (python and postgresql)
- basic tests for pages and users
- different settings files for development and production

Also there is the following containerized features:
- Celery
- Redis

> Note: The Celery and Redis features are currently just implemented in docker-compose-dev.yml. There would probably be other settings for these in a production scenario than covered in this template.

This template is based on my previous [Django Template](https://github.com/Joeriksson/django-template), but also adds Celery and Redis for doing e.g. scheduled tasks, async tasks. It also uses [Tailwind CSS](https://tailwindcss.com) instead of Bootstrap.

## Production and development settings

The setting file are split up in production and a development settings files. Also the project have one docker-compose.yml for production and one for development. Within the docker-compose files you can find the parameter for which settings file to use on the runserver command. To make it easier and less to type for each command, there is a Makefile with different common operations.

## Quick start

1. Clone this repository

` https://github.com/Joeriksson/django-template-2`

2. Install [Docker Desktop](https://www.docker.com/products/docker-desktop) to be able to use the docker environment.

3. Create an .env file in the root folder with the the following parameters:

    ```ENVIRONMENT='development'
    SENDGRID_PASSWORD=<you sendgrid password>
    SENDGRID_USERNAME=<your sendgrid username>
    SECRET_KEY=<your secret key>
    DEBUG=True
    ```

4. In the directory where you cloned the repository, run the following command:

    `make dev_build`

5. Run a migration to build the databases

    `make dev_web_exec cmd='python manage.py migrate'`
    
    Then check in you browser that you see a start web page at `http://127.0.0.1:8000`

6. Create a Django super user to log in to the admin

    `make dev_web_exec cmd='python manage.py createsuperuser'`

7. Goto `http://127.0.0.1:8000/admin` and login with the super user account you just created.

8. Go on and build you app.

If you want to stop the container run:

  `make dev_down`


