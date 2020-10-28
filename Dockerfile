FROM python:3.9.0

WORKDIR /usr/src/app

COPY . .

RUN pip3 install -r requirements.txt
