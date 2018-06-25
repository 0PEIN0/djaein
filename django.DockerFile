FROM python:3.6.5
ENV PYTHONUNBUFFERED 1
EXPOSE 9001
WORKDIR "/app"
COPY scripts/python/* /app/
COPY scripts/python/docker_local_settings.py /app/djaein/local_settings.py
COPY djaein/requirements.txt /app
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY djaein/ /app
CMD python manage.py migrate
CMD python manage.py collectstatic
CMD python manage.py shell < /app/initial_data_load.py
