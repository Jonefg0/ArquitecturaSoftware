FROM python:3.6.3

ENV SLACK_TOKEN="xoxb-1449368106935-1449466769239-xzV9EsIa9z8UajAghqZbsdyz"
ENV SLACK_SIGNING_SECRET="79017c1643fd9a66223ead32b27e3ff7"

COPY ./requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

ENV PYTHONUNBUFFERED=1

WORKDIR /Sam_lector

COPY ./sam.py /sam.py

CMD [ "python", "/sam.py" ]