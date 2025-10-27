

from fastapi import FastAPI,HTTPException
from config import TORTOISE_ORM
from config import init_db
from schemas import Author_Pydantic,AuthorIn_Pydantic
from models.author_model import Author
app = FastAPI()

init_db(app)

@app.get("/")
async def hello():
    return {"hello"}

@app.post("/author/",response_model=Author_Pydantic)
async def create_author(author:AuthorIn_Pydantic):
    new_author=await Author.create(**author.dict())
    return await Author_Pydantic.from_tortoise_orm(new_author)

@app.get("/authors/",response_model=list[Author_Pydantic])
async def get_author():
    return await Author_Pydantic.from_queryset(Author.all())


@app.get("/author/{id}/", response_model=Author_Pydantic)
async def get_author_id(id: int):
    author = await Author.get_or_none(id=id)
    if not author:
        raise HTTPException(status_code=404, detail="Author not found.")
    return await Author_Pydantic.from_tortoise_orm(author)

@app.put("/authors/{id}/",response_model=Author_Pydantic)
async def author_update(id:int,author:AuthorIn_Pydantic):
    old_author=await Author.get_or_none(id=id)
    if not old_author:
        raise HTTPException(status_code=404,detail="author not found")
    old_author.name=author.name
    old_author.age=author.age
    await old_author.save()
    return await Author_Pydantic.from_tortoise_orm(old_author)


@app.delete("/author/{id}/")
async def delete_author(id:int):
    rem_auth=await Author.filter(id=id).delete()
    if not rem_auth:
        raise HTTPException(status_code=404,detail="not able to delete")
    return None