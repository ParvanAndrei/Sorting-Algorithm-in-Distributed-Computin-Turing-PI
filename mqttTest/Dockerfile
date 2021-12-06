FROM python:3.7-slim-buster

WORKDIR /app

COPY . .
RUN ["apt-get","update"]
RUN ["apt-get","install","-y","software-properties-common"]
RUN ["apt","install","-y","gpg-agent"]
RUN ["apt-add-repository","ppa:mosquitto-dev/mosquitto-ppa"]
RUN ["apt-get","install","-y","mosquitto"]
RUN ["apt-get","install","-y","mosquitto-clients"]
RUN ["apt-get","install","-y","build-essential","python3-dev","python3-setuptools"]
RUN ["apt-get","install","-y","python3-numpy","python3-scipy"]
RUN ["apt-get","install","-y","libatlas-dev","libatlas3gf-base"]

RUN ["pip","install","-r","requirements.txt"]

#CMD ["mosquitto","-v","&"]
