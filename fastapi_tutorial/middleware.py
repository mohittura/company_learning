from fastapi import FastAPI, Request    

app = FastAPI()

@app.middleware("http")
async def addmiddleware(request: Request, call_next):
    print("Middleware works here mwehehehe")
    response = await call_next(request)
    return response

@app.get("/")
async def main():
    return {"message": "hello world"}

@app.get("/{name}")
async def getname(name: str):
    return {"message": f"Hello {name}"}