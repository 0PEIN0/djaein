FROM python:3.6.5
ENV PYTHONUNBUFFERED 1
EXPOSE 9001

COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . /app/
RUN python manage.py runserver 9001
