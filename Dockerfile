FROM python:3.5.1-onbuild

MAINTAINER Chris Fordham <chris@fordham-nagy.id.au>

ENV TOKEN=ineedatoken!

CMD ["python", "echobot.py"]
