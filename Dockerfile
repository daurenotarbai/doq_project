FROM python:3.8

MAINTAINER Dauren

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/doq_project

COPY ./requirements.txt /usr/src/requirements.txt
RUN pip install -r /usr/src/requirements.txt

COPY . /usr/src/doq_project

FROM nginx

RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d

# 8000

# RUN python manage.py collectstatic --noinput
# CMD ["python","manage.py","migrate"]
# CMD ["python","manage.py","runserver","0.0.0.0:8000"]

#CMD exec gunicorn djangoapp.wsgi:application --bind 0.0.0.0:8000 --workers 3