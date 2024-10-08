FROM python:3.10-alpine

WORKDIR /app

COPY app/requirements.txt .

RUN apk update && \
    apk add --no-cache pkgconfig mariadb-dev build-base mariadb-connector-c bash
RUN pip install --upgrade pip setuptools wheel
RUN pip install -r requirements.txt
RUN apk del mariadb-dev

COPY ./app .

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
