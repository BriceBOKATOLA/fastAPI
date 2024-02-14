from sqlalchemy import Column, Integer, String
from database import Base

# Define To Do class inheriting from Base
class ToDo(Base):
    __tablename__ = 'articles'
    id = Column(Integer, primary_key=True)
    titre = Column(String)
    contenu = Column(String)
    date_publication = Column(String)
