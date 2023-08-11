import uvicorn
from datetime import date

from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from sqldb import crud, models, schemas, database
from sqldb.database import SessionLocal, engine

from init_bdd import fill_db

# Drop all tables in the database
models.Base.metadata.drop_all(bind=engine)
# Create all tables in the database
models.Base.metadata.create_all(bind=engine)
# Fill the database with some data
fill_db()

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
async def root():
    today = date.today()
    d1 = today.strftime("%d/%m/%Y")
    return {"message": f"Hello World, today is {d1}"}

@app.post("/add_item/", response_model=schemas.Verbatim)
def create_verbatim(verbatim: schemas.VerbatimCreate, db: Session = Depends(get_db)):
    print(verbatim)
    return crud.create_verbatim(db=db, verbatim=verbatim)

@app.get("/verbatim/{verbatim_id}", response_model=schemas.Verbatim)
def read_verbatim(verbatim_id:int, db: Session = Depends(get_db)):
    verbatim = crud.get_verbatim(db,verbatim_id)
    return verbatim

@app.get("/verbatims/", response_model=List[schemas.Verbatim])
def read_verbatims(db: Session = Depends(get_db)):
    verbatims = crud.get_all_verbatims(db)
    return verbatims

@app.get("/structure/{structure_id}", response_model=schemas.Structure)
def read_structure(structure_id:int, db: Session = Depends(get_db)):
    structure = crud.get_structure(db,structure_id)
    return structure

@app.get("/structures/", response_model=List[schemas.Structure])
def read_structures(db: Session = Depends(get_db)):
    structures = crud.get_all_structures(db)
    return structures
#===============================================================================
# @app.post("/users/", response_model=schemas.User)
# def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
#     db_user = crud.get_user_by_username(db, username=user.username)
#     if db_user:
#         raise HTTPException(status_code=400, detail="Username already registered")
#     return crud.create_user(db=db, user=user)


# @app.get("/users/", response_model=List[schemas.User])
# def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     users = crud.get_users(db, skip=skip, limit=limit)
#     return users


# @app.get("/users/{user_id}", response_model=schemas.User)
# def read_user(user_id: int, db: Session = Depends(get_db)):
#     db_user = crud.get_user(db, user_id=user_id)
#     if db_user is None:
#         raise HTTPException(status_code=404, detail="User not found")
#     return db_user


# @app.post("/users/{user_id}/notes/", response_model=schemas.Note)
# def create_note_for_user(
#     user_id: int, note: schemas.NoteCreate, db: Session = Depends(get_db)
# ):
#     return crud.create_user_note(db=db, note=note, user_id=user_id)


# @app.get("/notes/", response_model=List[schemas.Note])
# def read_notes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     notes = crud.get_notes(db, skip=skip, limit=limit)
#     return notes

if __name__ == "__main__":
    uvicorn.run("main:app")