from fastapi import FastAPI
from pydantic import BaseModel, Field


class Book(BaseModel):
    id: int = Field(gt=0)
    title: str = Field(min_length=1)
    author: str = Field(min_length=1)
    year: int = Field(ge=1000, le=2100)


app = FastAPI(title="Book API")

books = [
    Book(id=1, title="The Hobbit", author="J.R.R. Tolkien", year=1937),
    Book(id=2, title="A Wrinkle in Time", author="Madeleine L'Engle", year=1962),
]


# TODO: Add GET / and return {"status": "healthy"}.

# TODO: Add GET /books and return all books.

# TODO: Add GET /books/{book_id} and handle unknown IDs.

# TODO: Add POST /books with status code 201.

# TODO: Add PUT /books/{book_id} and handle unknown IDs.

# TODO: Add DELETE /books/{book_id} with status code 204.