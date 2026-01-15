# Import SQLModel tools:
# - SQLModel: base class for models (Pydantic + ORM)
# - Field: used to configure database columns
# - select: used to query the database
from sqlmodel import SQLModel, Field, select

# Typing helpers
from typing import Optional, List

# Used to manage application startup and shutdown
from contextlib import asynccontextmanager


# -------------------------------
# Database Model (Table + Schema)
# -------------------------------
class Item(SQLModel, table=True):
    # Primary key column
    # Optional because it is None before inserting into DB
    # default=None allows the database to auto-generate it
    id: Optional[int] = Field(default=None, primary_key=True)

    # Regular columns
    name: str
    price: float

    # Default value if not provided
    is_offer: bool = False


# -------------------------------
# Database Engine Setup
# -------------------------------
from sqlmodel import create_engine, Session

# SQLite database file name
sqlite_file_name = "database.db"

# SQLite connection URL
sqlite_url = f"sqlite:///{sqlite_file_name}"

# Create the database engine
# echo=True prints SQL queries to the console (useful for learning/debugging)
engine = create_engine(sqlite_url, echo=True)


# -------------------------------
# Create Tables Function
# -------------------------------
def create_db_and_tables():
    # Creates all tables defined with table=True
    # Safe to run multiple times
    SQLModel.metadata.create_all(engine)


# -------------------------------
# FastAPI App Setup
# -------------------------------
from fastapi import FastAPI, Depends


# Application lifespan (startup & shutdown)
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Runs ONCE when the app starts
    create_db_and_tables()

    # Application runs while paused here
    yield

    # Runs when the app shuts down (nothing here for now)


# Create FastAPI app and attach lifespan
app = FastAPI(lifespan=lifespan)


# -------------------------------
# CREATE (POST)
# -------------------------------
@app.post("/items/")
def create_item(item: Item):
    # Open a database session
    with Session(engine) as session:
        # Add item to session (not saved yet)
        session.add(item)

        # Commit transaction (save to DB)
        session.commit()

        # Refresh to get auto-generated fields like ID
        session.refresh(item)

        # Return the saved item
        return item


# -------------------------------
# READ ALL (GET)
# -------------------------------
@app.get("/items/", response_model=List[Item])
def read_items():
    with Session(engine) as session:
        # Execute SELECT * FROM item
        items = session.exec(select(Item)).all()

        # Return all items
        return items


# -------------------------------
# UPDATE FULL (PUT)
# -------------------------------
@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, item: Item):
    with Session(engine) as session:
        # Fetch item by primary key
        db_item = session.get(Item, item_id)

        # If item exists, replace all fields
        if db_item:
            db_item.name = item.name
            db_item.price = item.price
            db_item.is_offer = item.is_offer

            # Save changes
            session.add(db_item)
            session.commit()
            session.refresh(db_item)

        # Return updated item (or None if not found)
        return db_item


# -------------------------------
# DELETE (DELETE)
# -------------------------------
@app.delete("/items/{item_id}", response_model=Item)
def delete_item(item_id: int):
    with Session(engine) as session:
        # Fetch item
        item = session.get(Item, item_id)

        # If found, delete it
        if item:
            session.delete(item)
            session.commit()

        # Return deleted item (or None)
        return item


# -------------------------------
# PARTIAL UPDATE (PATCH)
# -------------------------------
@app.patch("/items/{item_id}", response_model=Item)
def patch_item(item_id: int, item: Item):
    with Session(engine) as session:
        # Fetch item from DB
        db_item = session.get(Item, item_id)

        # Update only fields that are provided
        if db_item:
            if item.name is not None:
                db_item.name = item.name

            if item.price is not None:
                db_item.price = item.price

            if item.is_offer is not None:
                db_item.is_offer = item.is_offer

            # Save changes
            session.add(db_item)
            session.commit()
            session.refresh(db_item)

        # Return updated item
        return db_item
