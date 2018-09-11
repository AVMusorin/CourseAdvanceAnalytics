FROM jupyter/base-notebook
MAINTAINER Aleksandr Musorin <smusorin@mail.ru>
USER root
WORKDIR /home/jovyan
RUN apt update && apt install tor -y
RUN wget -q https://chromedriver.storage.googleapis.com/2.41/chromedriver_linux64.zip
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

