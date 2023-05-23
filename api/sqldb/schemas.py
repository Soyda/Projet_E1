from typing import List, Optional
from pydantic import BaseModel


class NoteBase(BaseModel):
    note_content: str
    # note_sentiment: Optional[str] = None CHECKER SI BESOIN DE LE METTRE


class NoteCreate(NoteBase):
    pass


class Note(NoteBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    username : str



class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_admin: bool
    notes: List[Note] = []

    class Config:
        orm_mode = True