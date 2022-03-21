# Creating Docker Image
## 1 Pull python image
### Check used python version
```sh
python --version
```
### Pull proper image
Go to the https://hub.docker.com/_/python website and look up in Tags for your python version.
> The tags are `x.x.x-<base image>. I will personally select Python Image based on Alpine 3.15

```sh
docker pull python:3.10.3-alpine3.15
```

### Check if the image is pulled
```sh
docker images
```

## 2 Create Dockerfile

Dockerfile should look like this:

```dockerfile
FROM python:3.10.3-alpine3.15

WORKDIR /home/ez-flask-app

RUN pip install flask

COPY . .

ENTRYPOINT [ "python" ]

CMD ["app.py" ]

```

1. First we are basing it on `python:3.10.3-alpine3.15` image.
2. Later we run commands on the Image Linux Terminal to set up our Environment
3. Then we are copying contents of repository from host into Image File System
4. Last step is to define the command that should run during the creation of a container from our image.

## 3 Build image from Dockerfile

On the terminal run:

```sh
docker build -t ez-flask-app:1.0.0 .
```

If no errors were found check if the image was created 

## 4 Debug the container

### 4.1 Not running

It may happen that something does not work with your container. And when you type

```sh
docker run ez-flask-app:1.0.0
```

it may not even start.

In that case you need to remove image and rebuild it (but to remove image, you need to remove the container). The fastest way to do it is:

```
docker ps -a
docker rm <container_id>
docker rmi <image_id>
```

And now you can run it again after some changes.

### 4.2 Running

When the container starts, but it does not run as you wanted it to.

You can open the terminal of container by:

```sh
docker exec -it <container_id> /bin/sh
```

## 5 Work with the container

After you successfully builded the image, you can run a container from it!

```sh
docker images
docker run -p5000:5000 --name ez-flask-app ez-flask-app:1.0.0
```

I don't know why but on my PC the container logs:

```sh
* Serving Flask app 'app' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on all addresses.
   WARNING: This is a development server. Do not use it in a production deployment.
 * Running on http://172.17.0.2:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 384-425-739
```

Suggesting that it listens on http://172.17.0.2:5000/ which is not true. It works on localhost so to get the response from the app use this link:

http://127.0.0.1:5000/

