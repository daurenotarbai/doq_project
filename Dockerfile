FROM python:3.8

MAINTAINER Dauren

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /doq_project
EXPOSE 8000

COPY ./requirements.txt /requirements.txt
COPY ./scripts /scripts
RUN pip install -r /requirements.txt

COPY . /doq_project

RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    apt-get update -y && \
    apt-get install postgresql-client -y && \
    apt-get install musl-dev -y && \
    /py/bin/pip install -r /requirements.txt && \
    adduser --disabled-password --no-create-home doq_project && \
    mkdir -p /vol/web/static && \
    mkdir -p /vol/web/media && \
    chown -R doq_project:doq_project /vol && \
    chmod -R 755 /vol && \
    chmod -R +x /scripts

ENV PATH="/scripts:/py/bin:$PATH"

USER doq_project

CMD ["run.sh"]