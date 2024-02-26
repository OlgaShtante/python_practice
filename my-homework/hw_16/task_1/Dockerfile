FROM python:3.11

ENV PYTHONUNBUFFERED 1

WORKDIR /app

RUN curl -sSL https://install.python-poetry.org | python -
COPY poetry.lock pyproject.toml /app/

ENV PATH="${PATH}:/root/.local/bin" \
    POETRY_VIRTUALENVS_CREATE=False \
    PYTHONPATH="${PYTHONPATH}:/opt:/opt/src"

RUN poetry install

RUN apt-get update && apt-get install -y htop vim

COPY . .

CMD ["python", "app/manage.py", "runserver", "0.0.0.0:8000"]
