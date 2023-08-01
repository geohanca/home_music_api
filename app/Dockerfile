FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
#created to allow makemigrations command to run properly
RUN mkdir songapi/migrations
RUN touch songapi/migrations/__init__.py