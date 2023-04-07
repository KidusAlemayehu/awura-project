FROM python:3.10-slim-buster


ENV PYTHONUNBUFFERED=1
RUN mkdir /awuraproject
WORKDIR /awuraproject

COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .

CMD sh -c "python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:54101"
