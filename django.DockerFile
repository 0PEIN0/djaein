FROM python:3.6.5
ENV PYTHONUNBUFFERED 1
ENV DOCKER_CONTAINER=1
EXPOSE 9001
WORKDIR "/app"
COPY scripts/python/initial_data_load.py /scripts/initial_data_load.py
COPY djaein/requirements.txt /app/djaein/requirements.txt
RUN pip install --upgrade pip
RUN pip install -r /app/djaein/requirements.txt
COPY djaein/* /app/
CMD python /app/djaein/manage.py migrate
CMD python /app/djaein/manage.py collectstatic
CMD python /app/djaein/manage.py shell < /scripts/initial_data_load.py
