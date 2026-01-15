from fastapi import FastAPI, status
from pydantic import BaseModel
from pymongo import MongoClient
from typing import List

DB = "library"
BOOK_COLLECTION = "books"

class Book(BaseModel):
    bookID: int
    title: str
    author: str
    publisher: str

app = FastAPI()

@app.post("/add_new", status_code=status.HTTP_201_CREATED)
def add_book(book: Book):
    with MongoClient() as client:
        collection = client[DB][BOOK_COLLECTION]
        result = collection.insert_one(book.dict())
        return {"inserted": result.acknowledged}

@app.get("/get_all", response_model=List[Book])
def get_all_books():
    with MongoClient() as client:
        collection = client[DB][BOOK_COLLECTION]
        books = list(collection.find({}, {"_id": 0}))
        return books
    
@app.put("/update/{book_id}")
def update_book(book_id: int, book: Book):
    with MongoClient() as client:
        collection = client[DB][BOOK_COLLECTION]
        result = collection.update_one({"bookID": book_id}, {"$set": book.dict()})
        if result.matched_count:
            return {"updated": True}
        return {"updated": False}   

@app.delete("/delete/{book_id}")
def delete_book(book_id: int):
    with MongoClient() as client:
        collection = client[DB][BOOK_COLLECTION]
        result = collection.delete_one({"bookID": book_id})
        if result.deleted_count:
            return {"deleted": True}
        return {"deleted": False}