# from fastapi import FastAPI, Path
# app = FastAPI()
# @app.get("/hello/{name}/{age}")
# async def hello(*, name: str=Path(...,min_length=3 , max_length=10), age: int = Path(..., ge=1, le=100)):
#    return {"name": name, "age":age}

# import uvicorn
# from fastapi import FastAPI
# from typing import List
# from pydantic import BaseModel, Field
# app = FastAPI()
# class Student(BaseModel):
#    id: int
#    name :str = Field(None, title="name of student", max_length=10)
#    subjects: List[str] = []
# @app.post("/students/")
# async def student_data(s1: Student):
#    return s1


# import uvicorn
# from fastapi import FastAPI, Body
# app = FastAPI()
# @app.post("/students")
# async def student_data(name:str=Body(...), marks:int=Body(...)): # ... this thing means mandatory field
#    return {"name":name,"marks": marks}

# @app.post("/students/{college}")
# async def student_data(college:str, age:int, student:Student):
#    retval={"college":college, "age":age, **student.dict()} ## ** means dictionary unpacking
#    return retval

from fastapi import FastAPI
from fastapi.responses import HTMLResponse  
app = FastAPI()
@app.get("/hello/")
async def hello():
    html_content="""
    <html>
        <head>
            <title>Sample HTML Page</title>
        </head>
        <body>
            <h1 style="color:blue;">Welcome to FastAPI!</h1>
            <p>This is a sample HTML response.</p>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content)