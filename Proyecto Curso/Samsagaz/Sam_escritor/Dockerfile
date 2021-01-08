FROM python:3.6.3

ENV SLACK_TOKEN="xoxb-1449368106935-1449466769239-xzV9EsIa9z8UajAghqZbsdyz"

COPY ./requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

WORKDIR /Sam_escritor

COPY ./sam_escribe.py /sam_escribe.py
COPY ./sam_escribe.py /sam_escribe.py

CMD [ "python", "/sam_escribe.py" ]
