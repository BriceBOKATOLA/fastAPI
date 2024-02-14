from pydantic import BaseModel

# Create ToDo Schema (Pydantic Model)
class CreateArticle(BaseModel):
    id: int
    titre: str
    contenu: str
    date_publication: str

# Complete ToDo Schema (Pydantic Model)
class ToDo(BaseModel):
    id: int
    titre: str
    contenu: str
    date_publication: str

    class Config:
        orm_mode = True