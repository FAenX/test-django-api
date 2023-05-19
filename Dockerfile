FROM python:3.9

RUN apt-get update
RUN apt-get install postgresql postgresql-contrib -y
RUN apt-get install libpq-dev python3-dev -y

COPY ./poetry.lock ./pyproject.toml ./
RUN pip install poetry
RUN poetry config virtualenvs.in-project false
RUN poetry export -f requirements.txt --output requirements.txt --without-hashes
RUN pip install -r requirements.txt


WORKDIR /app