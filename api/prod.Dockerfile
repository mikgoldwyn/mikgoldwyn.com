FROM python:3.6

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        postgresql-client \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app/api
COPY prod.requirements.txt /app/api
COPY requirements.txt /app/api
RUN pip install --upgrade pip
RUN pip install -r prod.requirements.txt
