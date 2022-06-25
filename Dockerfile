FROM python:3.8

MAINTAINER Dauren

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /doq_project

COPY ./requirements.txt /requirements.txt
COPY ./scripts /scripts
RUN pip install -r /requirements.txt

COPY . /doq_project

RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    apt-get update -y && \
    apt-get install postgresql-client -y && \
    apt-get install .tmp-deps -y \
        musl-dev && \
    /py/bin/pip install -r /requirements.txt && \
    apt-get del .tmp-deps -y && \
    adduser --disabled-password --no-create-home dauren && \
    mkdir -p /vol/web/static && \
    mkdir -p /vol/web/media && \
    chown -R dauren:doq_project /vol && \
    chmod -R 755 /vol && \
    chmod -R +x /scripts

ENV PATH="/scripts:/py/bin:$PATH"

USER dauren

CMD ["run.sh"]