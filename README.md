# Djaein

Boiler plate project for django/postgres.

### Stacks
1. Django `2.0.6`
2. DRF
3. Celery
4. Redis
5. Postgres `9.6`
6. Docker

### Docker usage

1. To build the services, run the following commands in terminal. Make sure `docker-compose` is installed on your local machine.

```bash
COMPOSE_HTTP_TIMEOUT=2000 docker-compose build
```

2. To run the services, run the following commands in terminal.

```bash
docker-compose up
```

### Using as boiler plate
1. Copy the source from this repository.
2. Move to the place where the source is copied.
3. Delete `djaein/djaein` folder.
4. Delete `djaein/manage.py` file.
5. Create new django project.
6. Copy the contents from `djaein` folder inside the newly created django project.
7. Replace the following strings in the parent directory.

`admin@djaein.net` -> `new_project_django_admin_panel_user_email`

`djaein-204-login` -> `new_project_django_admin_panel_super_user_password`

`DJAEIN` -> `NEW_DJANGO_PROJECT_NAME`

`djaein` -> `new_project_name`

`9001` -> `new_django_project_running_port`

`10001` -> `new_project_celery_running_port`
