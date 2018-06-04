FROM django:onbuild

EXPOSE 8001

RUN pip install --upgrade pip
COPY . /app
RUN pip install
RUN python manage.py runserver 8001
