from fastapi import FastAPI
from pydantic import BaseModel
from typing import Tuple

app = FastAPI()
class supplier(BaseModel):
   name: str
   address: str
   city: str
   country: str

class product(BaseModel):
   name: str
   description: str
   price: float
   supp: supplier   

class customer(BaseModel):
   custID: int
   custname: str
   prod : Tuple[product]


@app.post("/invoice/",)
async def getInvoice(c1:customer):
   return c1