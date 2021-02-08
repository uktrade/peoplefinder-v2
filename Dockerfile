FROM python:3.9.1-buster

ENV PYTHONUNBUFFERED=1

RUN mkdir /code
WORKDIR /code

COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

ENTRYPOINT [ "./entrypoint.sh" ]
