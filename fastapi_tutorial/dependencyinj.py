from fastapi import FastAPI, Depends
app = FastAPI()


class dependency: # can be made as a function also
   def __init__(self, id: str, name: str, age: int):
       self.id = id
       self.name = name
       self.age = age

@app.get("/user/")
async def user(dep: dependency = Depends(dependency)): # instead of passing individual parameters we can pass the whole dependency as a parameter
   return dep
@app.get("/admin/")
async def admin(dep: dependency = Depends(dependency)):
   return dep 
