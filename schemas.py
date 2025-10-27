# schemas.py
from tortoise.contrib.pydantic import pydantic_model_creator
from models.author_model import Author

Author_Pydantic = pydantic_model_creator(Author, name="AuthorResponse")
AuthorIn_Pydantic = pydantic_model_creator(Author, name="AuthorIn", exclude_readonly=True)
