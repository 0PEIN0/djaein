#!/bin/bash

DJAEIN_PYTHON_VERSION="3"
DJAEIN_REPO_NAME="djaein"
DJAEIN_GIT_REPO="git@github.com:0PEIN0/$DJAEIN_REPO_NAME.git"
DJAEIN_PROJECT_NAME="djaein"
DJAEIN_CELERY_PROJECT_NAME="djaein"
DJAEIN_PROJECT_NAME_UNDERSCORE="djaein"
DJAEIN_PROJECT_NAME_CAMEL_CASE="djaein"
DJAEIN_LOCAL_PORT="9001"
DJAEIN_DJANGO_APP_NAMES="users personal"
DJAEIN_POSTGRES_USER="djaein"
DJAEIN_CELERY_FLOWER_HOST="127.0.0.1"
DJAEIN_CELERY_FLOWER_PORT="10001"

DJAEIN_DJANGO_OPERATIONS="makemigrations migrate"
DJAEIN_INIT_REQUIREMENTS_FILE_NAME='requirements.txt'
DJAEIN_PROJECT_ROOT_FOLDER="$SYSTEM_ROOT_GIT_REPO_FOLDER/$DJAEIN_REPO_NAME/$DJAEIN_PROJECT_NAME"
DJAEIN_VIRTUAL_ENVIRONMENT_NAME="${DJAEIN_PROJECT_NAME_CAMEL_CASE}Env"
DJAEIN_INIT_DB_FILE_NAME="${DJAEIN_PROJECT_NAME_UNDERSCORE}_reset_db.sql"
DJAEIN_POSTGRES_USER_PASSWORD_RESET_FILE_NAME="${DJAEIN_PROJECT_NAME_UNDERSCORE}_postgres_password_reset.sql"
DJAEIN_INIT_DATA_LOAD_PYTHON_FILE_NAME="initial_data_load.py"
DJAEIN_VIRTUAL_ENVIRONMENT_FOLDER="$SYSTEM_ROOT_VIRTUAL_PYTHON_ENVIRONMENT_FOLDER/$DJAEIN_VIRTUAL_ENVIRONMENT_NAME"
DJAEIN_INIT_POSTGRES_DB_FILE_PATH="$SYSTEM_ROOT_GIT_REPO_FOLDER/$DJAEIN_REPO_NAME/scripts/sql/$DJAEIN_INIT_DB_FILE_NAME"
DJAEIN_INIT_POSTGRES_DB_USER_PASSWORD_FILE_PATH="$SYSTEM_ROOT_GIT_REPO_FOLDER/$DJAEIN_REPO_NAME/scripts/sql/$DJAEIN_POSTGRES_USER_PASSWORD_RESET_FILE_NAME"
DJAEIN_INIT_DATA_LOAD_PYTHON_FILE_PATH="$SYSTEM_ROOT_GIT_REPO_FOLDER/$DJAEIN_REPO_NAME/scripts/python/$DJAEIN_INIT_DATA_LOAD_PYTHON_FILE_NAME"

alias ${DJAEIN_PROJECT_NAME_UNDERSCORE}_api_spec="${DJAEIN_PROJECT_NAME_UNDERSCORE}_ve && ./manage.py api_spec"
alias ${DJAEIN_PROJECT_NAME_UNDERSCORE}_bc="djangoBranchChange $DJAEIN_PROJECT_NAME_UNDERSCORE "
alias ${DJAEIN_PROJECT_NAME_UNDERSCORE}_bc_full_reset="djangoBranchChangeWithFullReset $DJAEIN_PROJECT_NAME_UNDERSCORE "
alias ${DJAEIN_PROJECT_NAME_UNDERSCORE}_bc_full_reset_and_run="djangoBranchChangeWithFullResetAndRun $DJAEIN_PROJECT_NAME_UNDERSCORE "
alias ${DJAEIN_PROJECT_NAME_UNDERSCORE}_bcd="${DJAEIN_PROJECT_NAME_UNDERSCORE}_bc develop"
alias ${DJAEIN_PROJECT_NAME_UNDERSCORE}_bcd_full_reset="${DJAEIN_PROJECT_NAME_UNDERSCORE}_bc_full_reset develop"
alias ${DJAEIN_PROJECT_NAME_UNDERSCORE}_bcd_full_reset_and_run="${DJAEIN_PROJECT_NAME_UNDERSCORE}_bc_full_reset_and_run develop"
alias ${DJAEIN_PROJECT_NAME_UNDERSCORE}_bcm="${DJAEIN_PROJECT_NAME_UNDERSCORE}_bc master"
alias ${DJAEIN_PROJECT_NAME_UNDERSCORE}_bcm_full_reset="${DJAEIN_PROJECT_NAME_UNDERSCORE}_bc_full_reset master"
alias ${DJAEIN_PROJECT_NAME_UNDERSCORE}_bcm_full_reset_and_run="${DJAEIN_PROJECT_NAME_UNDERSCORE}_bc_full_reset_and_run master"
alias ${DJAEIN_PROJECT_NAME_UNDERSCORE}_bcd_run="${DJAEIN_PROJECT_NAME_UNDERSCORE}_bcd && ${DJAEIN_PROJECT_NAME_UNDERSCORE}_run"
alias ${DJAEIN_PROJECT_NAME_UNDERSCORE}_bcr="djangoBranchChangeRun $DJAEIN_PROJECT_NAME_UNDERSCORE "
alias ${DJAEIN_PROJECT_NAME_UNDERSCORE}_db_shell="${DJAEIN_PROJECT_NAME_UNDERSCORE}_ve && ./manage.py shell"
alias ${DJAEIN_PROJECT_NAME_UNDERSCORE}_dir="goToDir \"$DJAEIN_PROJECT_ROOT_FOLDER\""
alias ${DJAEIN_PROJECT_NAME_UNDERSCORE}_frr="${DJAEIN_PROJECT_NAME_UNDERSCORE}_full_reset && ${DJAEIN_PROJECT_NAME_UNDERSCORE}_run"
alias ${DJAEIN_PROJECT_NAME_UNDERSCORE}_full_reset="djangoFullReset $DJAEIN_PROJECT_NAME_UNDERSCORE"
alias ${DJAEIN_PROJECT_NAME_UNDERSCORE}_gf="${DJAEIN_PROJECT_NAME_UNDERSCORE}_dir && git_f"
alias ${DJAEIN_PROJECT_NAME_UNDERSCORE}_git_setup="djangoGitSetup $DJAEIN_GIT_REPO"
alias ${DJAEIN_PROJECT_NAME_UNDERSCORE}_git_r="djangoGitRebaseWithDataLoad $DJAEIN_PROJECT_NAME_UNDERSCORE "
alias ${DJAEIN_PROJECT_NAME_UNDERSCORE}_git_rd="djangoGitRebaseWithDataLoad $DJAEIN_PROJECT_NAME_UNDERSCORE develop"
alias ${DJAEIN_PROJECT_NAME_UNDERSCORE}_git_rm="djangoGitRebaseWithDataLoad $DJAEIN_PROJECT_NAME_UNDERSCORE master"
alias ${DJAEIN_PROJECT_NAME_UNDERSCORE}_init_data_load="${DJAEIN_PROJECT_NAME_UNDERSCORE}_ve && ./manage.py migrate && ./manage.py shell < $DJAEIN_INIT_DATA_LOAD_PYTHON_FILE_PATH"
alias ${DJAEIN_PROJECT_NAME_UNDERSCORE}_installs="${DJAEIN_PROJECT_NAME_UNDERSCORE}_ve_init && cd \"$SYSTEM_ROOT_GIT_REPO_FOLDER\" && git clone ${DJAEIN_GIT_REPO} && ${DJAEIN_PROJECT_NAME_UNDERSCORE}_ve_installs && ${DJAEIN_PROJECT_NAME_UNDERSCORE}_dir"
alias ${DJAEIN_PROJECT_NAME_UNDERSCORE}_last_10_commit_hash="${DJAEIN_PROJECT_NAME_UNDERSCORE}_dir && git log -10 --pretty=format:\"%h\""
alias ${DJAEIN_PROJECT_NAME_UNDERSCORE}_loc="cloc \"$DJAEIN_PROJECT_ROOT_FOLDER\""
alias ${DJAEIN_PROJECT_NAME_UNDERSCORE}_reinitiate="djangoReinitiate \"$DJAEIN_PROJECT_ROOT_FOLDER\" \"$DJAEIN_DJANGO_APP_NAMES\" $DJAEIN_INIT_DATA_LOAD_PYTHON_FILE_PATH \"$DJAEIN_DJANGO_OPERATIONS\""
alias ${DJAEIN_PROJECT_NAME_UNDERSCORE}_reinitiate_clean="djangoReinitiateClean \"$DJAEIN_PROJECT_ROOT_FOLDER\" \"$DJAEIN_DJANGO_OPERATIONS\""
alias ${DJAEIN_PROJECT_NAME_UNDERSCORE}_reset_clean="djangoResetWithoutMigrationClean $DJAEIN_PROJECT_NAME_UNDERSCORE $DJAEIN_INIT_DATA_LOAD_PYTHON_FILE_PATH"
alias ${DJAEIN_PROJECT_NAME_UNDERSCORE}_postgres_shell="psql -U $DJAEIN_POSTGRES_USER"
alias ${DJAEIN_PROJECT_NAME_UNDERSCORE}_postgres_user_password_reset="postgresPasswordReset \"$DJAEIN_INIT_POSTGRES_DB_USER_PASSWORD_FILE_PATH\""
alias ${DJAEIN_PROJECT_NAME_UNDERSCORE}_process_id="lsof -i:${DJAEIN_LOCAL_PORT} | awk '{print $2}'"
alias ${DJAEIN_PROJECT_NAME_UNDERSCORE}_psql_reset="djangoPsqlReset $DJAEIN_POSTGRES_USER \"$DJAEIN_INIT_POSTGRES_DB_FILE_PATH\""
alias ${DJAEIN_PROJECT_NAME_UNDERSCORE}_reset="djangoReset $DJAEIN_PROJECT_NAME_UNDERSCORE"
alias ${DJAEIN_PROJECT_NAME_UNDERSCORE}_rr="${DJAEIN_PROJECT_NAME_UNDERSCORE}_reset && ${DJAEIN_PROJECT_NAME_UNDERSCORE}_run"
alias ${DJAEIN_PROJECT_NAME_UNDERSCORE}_rt="${DJAEIN_PROJECT_NAME_UNDERSCORE}_reset && ${DJAEIN_PROJECT_NAME_UNDERSCORE}_test"
alias ${DJAEIN_PROJECT_NAME_UNDERSCORE}_run="djangoRun $DJAEIN_PROJECT_NAME_UNDERSCORE $DJAEIN_PROJECT_NAME_UNDERSCORE $DJAEIN_LOCAL_PORT"
alias ${DJAEIN_PROJECT_NAME_UNDERSCORE}_run_production="djangoProductionRun $DJAEIN_PROJECT_NAME_UNDERSCORE $DJAEIN_PROJECT_NAME $DJAEIN_LOCAL_PORT"
alias ${DJAEIN_PROJECT_NAME_UNDERSCORE}_run_generic_deployment="djangoDeploymentOperations $DJAEIN_PROJECT_NAME_UNDERSCORE"
alias ${DJAEIN_PROJECT_NAME_UNDERSCORE}_start_celery="startCeleryWorkers $DJAEIN_CELERY_PROJECT_NAME $DJAEIN_CELERY_FLOWER_HOST $DJAEIN_CELERY_FLOWER_PORT"
alias ${DJAEIN_PROJECT_NAME_UNDERSCORE}_stop_processes="djangoStopProcesses $DJAEIN_LOCAL_PORT $DJAEIN_CELERY_PROJECT_NAME"
alias ${DJAEIN_PROJECT_NAME_UNDERSCORE}_test="djangoTest $DJAEIN_PROJECT_NAME_UNDERSCORE"
alias ${DJAEIN_PROJECT_NAME_UNDERSCORE}_ve="djangoUseVe \"$DJAEIN_VIRTUAL_ENVIRONMENT_FOLDER\" $DJAEIN_PROJECT_NAME_UNDERSCORE"
alias ${DJAEIN_PROJECT_NAME_UNDERSCORE}_ve_check="checkVirtualPythonEnvironmentFolder \"$DJAEIN_VIRTUAL_ENVIRONMENT_FOLDER\" \"$SYSTEM_ROOT_VIRTUAL_PYTHON_ENVIRONMENT_FOLDER\" $DJAEIN_VIRTUAL_ENVIRONMENT_NAME"
alias ${DJAEIN_PROJECT_NAME_UNDERSCORE}_ve_clear="djangoVeClear \"$SYSTEM_ROOT_VIRTUAL_PYTHON_ENVIRONMENT_FOLDER\" $DJAEIN_VIRTUAL_ENVIRONMENT_NAME"
alias ${DJAEIN_PROJECT_NAME_UNDERSCORE}_ve_init="pythonVeVersionDecider \"$DJAEIN_VIRTUAL_ENVIRONMENT_FOLDER\" \"$SYSTEM_ROOT_VIRTUAL_PYTHON_ENVIRONMENT_FOLDER\" $DJAEIN_VIRTUAL_ENVIRONMENT_NAME $DJAEIN_PROJECT_NAME \"$DJAEIN_PYTHON_VERSION\""
alias ${DJAEIN_PROJECT_NAME_UNDERSCORE}_ve_installs="djangoDefaultSetupWithDataLoad \"$DJAEIN_PROJECT_ROOT_FOLDER\" $DJAEIN_INIT_REQUIREMENTS_FILE_NAME $DJAEIN_PROJECT_NAME_UNDERSCORE"
