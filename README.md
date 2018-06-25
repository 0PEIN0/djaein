# Djaein

Boiler plate project for django/postgres.

### Stacks
Django `2.0.6`
DRF
Celery
RabbitMQ
Postgres
Docker


### Docker usage

1. To build the services, run the following commands in terminal. Make sure `docker-compose` is installed on your local machine.

```bash
docker-compose build
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
`DJAEIN` -> `NEW_DJANGO_PROJECT_NAME`
`djaein` -> `new_project_name`