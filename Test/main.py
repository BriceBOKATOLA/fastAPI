from typing import List
from uuid import uuid4
from fastapi import FastAPI
from models import Article
# sup 
from uuid import UUID
from fastapi HTTPException

app = FastAPI()
db: List[Article] = [
 Article(
 id=uuid4(),
 titre="La vie",
 contenu="blablabla......",
 date_publication="12h",
 ),
 Article(
 id=uuid4(),
 titre="L'enfant",
 contenu="blablabla......",
 date_publication="12h",

 ),
 Article(
 id=uuid4(),
 titre="Les dieux",
 contenu="blablabla......",
 date_publication="12h"
 ),
 Article(
 id=uuid4(),
 titre="Le tartar",
 contenu="blablabla......",
 date_publication="12h",

 ),
]


# test pour voir le bon fonctionement 
@app.get("/")
async def root():
 return {"Hello": "World",}
@app.get("/api/v1/rodson")
async def get_users():
 return db

# creation d'un  nouvel article 

@app.post("/api/v1/rodson") #lancement de l'api http://localhost:8000/api/v1/rodson
async def create_Article(Article: Article):
 db.append(Article)
 return {"id": Article.id} 



@app.delete("/api/v1/rodson/{id}")
async def delete_user(id: UUID):
for article in db:
 if article.id == id:
  db.remove(article)
 return
#  Si le id correspond à un utilisateur, 
# l’utilisateur sera supprimé ; sinon, un HTTPException avec un code d’état de 404 sera levé.

raise HTTPException(
 status_code=404, detail=f"Delete article failed, id {id} not found."
 )
