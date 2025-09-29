FROM ubuntu:18.04
RUN apt-get update -y && \
    apt-get install -y python-pip python-dev build-essential && \
    rm -rf /var/lib/apt/lists/*
WORKDIR /app
COPY ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
COPY . /app
CMD [ "python","./app.py" ]