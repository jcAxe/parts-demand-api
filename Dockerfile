FROM python:3.6.8
ENV PYTHONUNBUFFERED 1
ENV SECRET_KEY placeholder1
ENV DBUSER placeholder2
ENV DBPASSWORD placeholder3
ENV DBNAME placeholder4
ENV DBHOST placeholder5
ENV DBENGINE placeholder6
ENV DBPORT placeholder7

RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/