from fastapi import FastAPI, Cookie
from fastapi.responses import JSONResponse
app = FastAPI()
@app.post("/cookie/")
def create_cookie(key: str = "username", value: str = "admin"):
   content = {"message": "cookie set", "key": key, "value": value}
   response = JSONResponse(content=content)
   response.set_cookie(key=key, value=value)
   return response

@app.get("/readcookie/")
async def read_cookie(username: str = Cookie(None)):
   return {"username": username}