from fastapi import FastAPI, Request, UploadFile, File
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import shutil

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/upload/", response_class=HTMLResponse)
async def upload(request: Request):
    return templates.TemplateResponse("uploadfile.html", {"request": request})
    
    
@app.post("/uploader/")
async def create_upload_file(file: UploadFile = File(...)):
    with open(file.filename, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {"filename": file.filename}
