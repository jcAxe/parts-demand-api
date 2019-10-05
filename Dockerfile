FROM python:3
ENV PYTHONUNBUFFERED 1
ENV SECRET_KEY placeholder1
ENV DBUSER placeholder2
ENV DBPASSWORD placeholder3
ENV DBNAME placeholder4
ENV DBHOST placeholder5
ENV DBENGINE django.db.backends.postgresql
ENV DBPORT placeholder6

RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/