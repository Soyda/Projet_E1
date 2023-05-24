from typing import List, Optional
from pydantic import BaseModel
import datetime


class VerbatimBase(BaseModel):
    verbatim_content: str


class VerbatimCreate(VerbatimBase):
    str_id: int
    upload_date: Optional[datetime.date]
    verbatim_date: datetime.date
    verbatim_content: str
    verbatim_sentiment: Optional[str] = "N/A"
    verbatim_category: Optional[str] = "N/A"


class Verbatim(VerbatimBase):
    id: int
    str_id: int
    # structures : List["Structure"] = []
    upload_date: datetime.date
    verbatim_date: datetime.date
    verbatim_content: str
    verbatim_sentiment: str
    verbatim_category: str

    class Config:
        orm_mode = True


class StructureBase(BaseModel):
    id: int
    lib_str : str
    verbatims : List[Verbatim] = []


class StructureCreate(StructureBase):
    pass

class Structure(StructureBase):
    lib_str : str
    verbatims: List[Verbatim] = []

    class Config:
        orm_mode = True

Verbatim.update_forward_refs()  # To solve the circular dependency between Verbatim and Structure