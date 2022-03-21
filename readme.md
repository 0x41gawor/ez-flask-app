# Ez-Flask App
Just want to learn Docker, so I've chosen some easy&fast backend framework for fast development of smth that will just listen on some port and would be able to respond with basic html page or something. Want to deploy it as a Docker Image and then run it as a Docker Container on my PC, just to get hands-on practice with Docker.

## Dockerfile
I know later I will need to create a Dockerfile, and becasue of that i will note every step required for installation.

## Setting up Environment
Steps:
- Install Python 3.6+ and PIP
- Install virtualenv
- Create project directory
- Create virtual environment
- Install required packages

### Install Python 3.6+ and PIP
Open VS Code and type 
```sh
python3 --version
```
To check if Python is installed,
> My Docker Image will be based on Python Image, so I will have Python already installed.
Then check if the PIP is installed:
```sh
pip --version
```

### Install virtualenv
```sh
pip3 install virutalenv
```
### Create virtualenv
Linux:
```sh
sudo apt-get install python3-venv    # If needed
python3 -m venv .venv
```
Windows:
```
py -3 -m venv .venv
```
And the folder `.venv` is our virtualenv
### Activate virtualenv
Linux:
```sh
source .venv/bin/activate
```
Windows:
```sh
.venv\scripts\activate
```
> On Windows OS you might run upon a Script Restricition Error.
> Just google it and fix.
### Install required packages
```sh
pip install flask
```

## Run the app
Create `app.py` file:
```python
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run()
```
Now in the terminal type:
```sh
python app.py
```
Server should be ready to listen on requests.
