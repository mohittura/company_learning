
MYSQL_URL = "mysql+pymysql://sql12813646:vfVMuIUMrG@sql12.freesqldatabase.com:3306/sql12813646"
from sqlmodel import SQLModel, Field, create_engine, Session, select
from fastapi import FastAPI
from typing import Optional, List
from contextlib import asynccontextmanager

engine = create_engine(MYSQL_URL,  echo=True)

class Item(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    price: float
    is_offer: bool = False

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield

app = FastAPI(lifespan=lifespan)

@app.post("/items/", response_model=Item)
def create_item(item: Item):
    with Session(engine) as session:
        session.add(item)
        session.commit()
        session.refresh(item)
        return item
    
@app.get("/items/", response_model=List[Item])
def read_items():
    with Session(engine) as session:
        items = session.exec(select(Item)).all()
        return items