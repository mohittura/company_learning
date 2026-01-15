from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import FastAPI, Request, Form
from fastapi.staticfiles import StaticFiles

app = FastAPI()
templates = Jinja2Templates(directory="templates") # will look for templates in the "templates" folder

# app.mount("/static", StaticFiles(directory="static"), name="static") # serve static files from the "static" folder
@app.get("/login", response_class=HTMLResponse)
async def login(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

# @app.post("/submit") # this is the non pydantic way of receiving form data
# async def submit(name: str = Form(...), password:str = Form(...)):
#     return {"name": name, "password": password}

from pydantic import BaseModel
class User(BaseModel):
   username:str
   password:str
@app.post("/submit/", response_model=User)
async def submit(nm: str = Form(...), pwd: str = Form(...)):
   return User(username=nm, password=pwd)