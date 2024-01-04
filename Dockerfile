FROM python:3.11.6-alpine

WORKDIR /flaskeleton

COPY flaskeleton ./flaskeleton
COPY migrations ./migrations
COPY requirements.txt .
COPY settings.toml .

RUN pip install --upgrade pip
# RUN pip install poetry
# RUN poetry export --format=requirements.txt --output=requirements.txt
RUN pip install -r requirements.txt

RUN flask --app flaskeleton db upgrade

EXPOSE 80