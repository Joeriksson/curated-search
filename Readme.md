# Curated Search

![django test workflow](https://github.com/Joeriksson/curated-search/actions/workflows/django.yml/badge.svg)

## Quick start

1. Clone this repository

` https://github.com/Joeriksson/curated-search`

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


