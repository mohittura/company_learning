from flask import Flask

flaskapp = Flask(__name__)
@flaskapp.route("/")
def home():
    return "Hello, Flask!"

from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def read_root():
    return "Hello from fastapi"

from fastapi.middleware.wsgi import WSGIMiddleware
app.mount("/flask", WSGIMiddleware(flaskapp))

