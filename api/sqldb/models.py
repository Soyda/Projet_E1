from sqlalchemy import Integer, ForeignKey, String, Column, Boolean, DateTime
from .database import Base
from sqlalchemy.orm import relationship
from datetime import datetime



class Verbatim(Base):
    __tablename__ = 'verbatims'
    id = Column(Integer, primary_key=True, index=True)
    str_id = Column(Integer, ForeignKey('structures.id'))
    upload_date = Column(DateTime) 
    verbatim_date = Column(DateTime)
    verbatim_content = Column(String(length=500))
    verbatim_sentiment = Column(String)
    verbatim_category = Column(String)

    structure = relationship("Structure", back_populates="verbatims")

class Structure(Base):
    __tablename__ = 'structures'
    id = Column(Integer, primary_key=True, index=True)
    lib_str = Column(String)

    verbatims = relationship("Verbatim", back_populates="structure")


