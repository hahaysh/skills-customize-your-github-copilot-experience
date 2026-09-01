from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel


app = FastAPI(title="Book API")


class Book(BaseModel):
    id: int
    title: str
    author: str


books: list[Book] = []


# TODO: Define a GET /health endpoint that returns {"status": "ok"}.


# TODO: Define a GET /books endpoint with list[Book] as its response model.


# TODO: Define a POST /books endpoint that stores and returns a book.
# Use status.HTTP_201_CREATED as the success status code.


# TODO: Define a GET /books/{book_id} endpoint.
# Raise HTTPException with status.HTTP_404_NOT_FOUND if the book does not exist.
