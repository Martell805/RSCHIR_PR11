# syntax=docker/dockerfile:1

FROM python:3.10

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .
RUN python manage.py migrate

CMD ["python3", "main.py"]
