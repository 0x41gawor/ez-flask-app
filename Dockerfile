FROM python:3.10.3-alpine3.15

WORKDIR /home/ez-flask-app

RUN pip install flask

COPY . .

ENTRYPOINT [ "python" ]

CMD ["app.py" ]
