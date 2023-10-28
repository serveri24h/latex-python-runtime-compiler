FROM python:3.11-slim

RUN apt-get -y update && apt-get -y install \
  build-essential \
  texlive

RUN mkdir /app
COPY . /app

WORKDIR /app

CMD [ "sleep", "infinity" ]
#ENTRYPOINT ["python", "loop.py"]