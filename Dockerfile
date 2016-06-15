FROM python:3.5.1-alpine

MAINTAINER Chris Fordham <chris@fordham-nagy.id.au>

ENV TOKEN=ineedatoken!

RUN mkdir -p /usr/local/echobot

WORKDIR /usr/local/echobot

COPY echobot.py /usr/local/echobot/
COPY requirements.txt /usr/local/echobot/

RUN pip install -r requirements.txt

CMD ["./echobot.py"]
