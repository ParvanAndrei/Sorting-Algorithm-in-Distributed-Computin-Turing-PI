FROM python:3.7-slim-buster

WORKDIR /app

COPY . .

RUN ["pip","install","paho-mqtt"]
RUN ["apt-get","update"]
RUN ["apt-get","-y","install","nano"]

CMD ["python","subber.py"]
