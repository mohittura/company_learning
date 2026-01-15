from fastapi import FastAPI

app = FastAPI() 
@app.get("/app")
def mainindex():
    return {"message": "This is the from the top level app"}

@app.get("/subapp")
def subappindex():
    return {"message": "This is the from the sub app"}

app.mount("/subappmount", subappindex)
