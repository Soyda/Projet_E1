from sqlalchemy.orm import Session

from . import models, schemas


def create_verbatim(db: Session, verbatim: schemas.VerbatimCreate):
    db_verbatim = models.Verbatim(
                        str_id = verbatim.str_id, 
                        upload_date = verbatim.upload_date,
                        verbatim_date = verbatim.verbatim_date,
                        verbatim_content = verbatim.verbatim_content,
                        verbatim_sentiment = verbatim.verbatim_sentiment,
                        verbatim_category = verbatim.verbatim_category
                        )
    db.add(db_verbatim)
    db.commit()
    db.refresh(db_verbatim)
    return db_verbatim

def get_verbatim(db: Session, verbatim_id: int):
    return db.query(models.Verbatim).filter(models.Verbatim.id == verbatim_id).first()

def get_all_verbatims(db: Session):
    return db.query(models.Verbatim).all()

def get_structure(db: Session, structure_id: int):
    return db.query(models.Structure).filter(models.Structure.id == structure_id).first()

def get_all_structures(db: Session):
    return db.query(models.Structure).all()
#===============================================================================

# def get_user(db: Session, user_id: int):
#     return db.query(models.User).filter(models.User.id == user_id).first()


# def get_user_by_username(db: Session, username: str):
#     return db.query(models.User).filter(models.User.username == username).first()


# def get_users(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(models.User).offset(skip).limit(limit).all()


# def create_user(db: Session, user: schemas.UserCreate):
#     fake_hashed_password = user.password + "notreallyhashed"
#     db_user = models.User(username=user.username, hashed_password=fake_hashed_password)
#     db.add(db_user)
#     db.commit()
#     db.refresh(db_user)
#     return db_user


# def get_notes(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(models.Note).offset(skip).limit(limit).all()


# def create_user_note(db: Session, note: schemas.NoteCreate, user_id: int):
#     db_note = models.Note(**note.dict(), owner_id=user_id)
#     db.add(db_note)
#     db.commit()
#     db.refresh(db_note)
#     return db_note