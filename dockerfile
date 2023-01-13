FROM python:3.10-slim-buster


ENV PYTHONUNBUFFERED=1
RUN mkdir /awuraproject
WORKDIR /awuraproject

COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
