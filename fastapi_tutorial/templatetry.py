from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles

app = FastAPI()
templates = Jinja2Templates(directory="templates") # will look for templates in the "templates" folder

# app.mount("/static", StaticFiles(directory="static"), name="static") # serve static files from the "static" folder

# @app.get("/hello/{name}", response_class=HTMLResponse) # tells FastAPI to expect an HTML response
# async def hello(request: Request, name: str): # Request → gives access to the incoming HTTP request (required for templates) 
#    # request: Request Jinja2 templates require the request object for url generation middleware templates
#    return templates.TemplateResponse("hello.html", {"request": request, "name": name}) # render the "hello.html" template with the request context

@app.get("/login", response_class=HTMLResponse)
async def login(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})
