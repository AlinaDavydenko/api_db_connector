from fastapi import FastAPI, status, Query

from pydantic import BaseModel

from api.db_conn import get_all_authors, get_authors_from_bd

from typing import List

# from asgiref.sync import database_sync_to_async

app = FastAPI()


class AuthorScheme(BaseModel):
    name: str = None
    salary: int = None
    position: str = None
    year: int = None
    award_name: str = None


class IdAuthor(BaseModel):
    id: int = None
    author: AuthorScheme


authors_db = []


@app.get("/authors", response_model=List[IdAuthor])
def get_all_authors_endpoint(skip: int = Query(0, ge=0), limit: int = Query(10, gt=0)):
    authors = get_all_authors(skip=skip, limit=limit)
    api_scheme = [IdAuthor(id=author.id, author=AuthorScheme(
        name=author.name_author, salary=author.salary, position=author.position, year=author.year,
        award_name=author.award_name)) for author in authors]
    return api_scheme


# @app.post("/authors", response_model=dict, status_code=status.HTTP_201_CREATED)
# def create_authors(authors: List[IdAuthor]) -> dict:
#     return {"message": "Authors created", "authors": authors}

# uvicorn api.fastapi_app:app --reload
