FROM python:3.10.3-alpine3.15

RUN mkdir -p /home/ez-flask-app &&\
    cd /home/ez-flask-app &&\
    pip3 install virtualenv &&\
    python3 -m venv .venv &&\
    source .venv/bin/activate &&\
    pip install flask

COPY . /home/ez-flask-app

CMD [ "python", "app.py" ]
