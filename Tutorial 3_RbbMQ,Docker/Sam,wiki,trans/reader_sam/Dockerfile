FROM python:3.6.3

COPY ./requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

ENV PYTHONUNBUFFERED=1

WORKDIR /reader_sam

COPY ./reader_sam.py /reader_sam.py

CMD [ "python", "/reader_sam.py" ]
