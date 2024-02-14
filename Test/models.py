from typing import List, Optional
from uuid import UUID, uuid4
from pydantic import BaseModel
from enum import Enum
from pydantic import BaseModel

# rajout des utilisation 
class Gender(str, Enum):
 male = "male"
 female = "female"
class Role(str, Enum):
 admin = "admin"
 Article = "Article"
class Article(BaseModel):
 id: Optional[UUID] = uuid4()
 titre: str
 contenu: str
 date_publication: str
 
#  Mis à jour paramètres  pouvant être 
 class UpdateUser(BaseModel):
 titre: Optional[str]
 contenu: Optional[str]
 date_publication: Optional[str]