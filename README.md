# Djaein

Boiler plate project for django/postgres.

### Stacks
1. Django `2.0.6`
2. DRF
3. Celery
4. Redis
5. Postgres `9.6`
6. Docker

#### Setup instructions for local development environment
1. Clone the repository.
2. Copy contents `scripts/python/sample_local_settings.py` file to `djaein/djaein/local_settings.py` file. Replace postgres user and password with relevant values. Run the following command from the project repository root directory: `cp scripts/python/sample_local_settings.py djaein/djaein/local_settings.py`
3. Activate virtual environment.
4. Go to the project root directory.
5. Run `cd djaein && pip install -r requirements.txt`
6. Run: `./manage.py migrate` to migrate migrations from repository.
7. Go to the project root directory. Load the initial data for the project by running this command: `./manage.py shell < scripts/python/initial_data_load.py`. Initial superuser authentication can also be found on this data loader python file. Default admin user authentication credential is noted below as well.
8. Run the backend project with this command: `./manage.py runserver 9001`. The django admin is available at [localhost:9001](http://localhost:9001/admin).

#### Alternate setup instructions for those who are using [`bash-helpers`](https://github.com/0PEIN0/bash-helpers) repository.
1. Run `cd $SYSTEM_ROOT_GIT_REPO_FOLDER` command and clone the repository there.

>Git url: `git@github.com:0PEIN0/djaein.git`

2. In `personal.sh` file import the project shell file like this.
```bash
if [ -f $SYSTEM_ROOT_GIT_REPO_FOLDER/djaein/scripts/shell/project-shell.sh ]; then
    . $SYSTEM_ROOT_GIT_REPO_FOLDER/djaein/scripts/shell/project-shell.sh
fi;
```
Then run `bash_refresh` in command line.

3. Copy contents `scripts/python/sample_local_settings.py` file to `djaein/djaein/local_settings.py` file. Replace postgres user and password with relevant data. Run the following command from the project repository root directory: `cp scripts/python/sample_local_settings.py djaein/djaein/local_settings.py`

4. `djaein_ve_init` command is for creating new virtual environment.

5. Open a new tab in the terminal by pressing `Ctrl + Shift + T`. Enter into sudo mode by pressing command `admin`. In sudo mode, open postgres shell by running command `postgres_shell_sudo` or `sudo -u postgres psql`. Then paste the following sql code:
```sql
CREATE USER djaein WITH PASSWORD 'djaein' ;
CREATE ROLE djaein LOGIN PASSWORD 'djaein';
```
Ignore any error that may show up here.

6. Switch back to the terminal tab where the project setup operations were being executed. Run `djaein_postgres_user_password_reset` command is for resetting postgres user password and creating project related database user.
7. `djaein_psql_reset` command is for cleaning the database.
8. `djaein_ve_init && djaein_ve && djaein_ve_installs` command is for installing django project requirement packages.
9. Run: `./manage.py migrate` to migrate migrations from repository.
10. `djaein_init_data_load` command is for migrating existing migrations in the repository and loading initial data. This command will insert a superuser as well and you can find the authorization credentials on this file: `scripts/python/initial_data_load.py`.
11. Run `djaein_run` command is to run back-end project.


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
