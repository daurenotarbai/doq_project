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
    apk add --update --no-cache postgresql-client && \
    apk add --update --no-cache --virtual .tmp-deps \
        build-base postgresql-dev musl-dev linux-headers && \
    /py/bin/pip install -r /requirements.txt && \
    apk del .tmp-deps && \
    adduser --disabled-password --no-create-home dauren && \
    mkdir -p /vol/web/static && \
    mkdir -p /vol/web/media && \
    chown -R dauren:doq_project /vol && \
    chmod -R 755 /vol && \
    chmod -R +x /scripts

ENV PATH="/scripts:/py/bin:$PATH"

USER dauren

CMD ["run.sh"]