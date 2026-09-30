# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a REST API for managing a collection of books. Practice defining FastAPI routes, validating data with Pydantic models, returning appropriate HTTP status codes, and handling missing resources.

## 📝 Tasks

### 🛠️	Create the API and Health Check

#### Description
Complete the initial FastAPI application and add a health-check endpoint that confirms the service is running.

#### Requirements
Completed program should:

- Create a FastAPI application with the title `Book API`.
- Define a `GET /` endpoint.
- Return `{"status": "healthy"}` from the health-check endpoint.
- Run with `fastapi dev starter-code.py` without errors.


### 🛠️	Read and Create Books

#### Description
Add endpoints that let clients view the book collection, find a single book, and add a new book using the provided `Book` model.

#### Requirements
Completed program should:

- Define a `GET /books` endpoint that returns all books.
- Define a `GET /books/{book_id}` endpoint that returns the matching book.
- Return HTTP status `404` with the detail `Book not found` when an ID does not exist.
- Define a `POST /books` endpoint that adds a valid book to the collection.
- Return HTTP status `201` and the newly created book from the `POST` endpoint.


### 🛠️	Update and Delete Books

#### Description
Complete the CRUD API by adding endpoints that modify an existing book and remove a book from the collection.

#### Requirements
Completed program should:

- Define a `PUT /books/{book_id}` endpoint that replaces the matching book data.
- Preserve the requested `book_id` when updating a book.
- Define a `DELETE /books/{book_id}` endpoint that removes the matching book.
- Return HTTP status `204` with no response body after a successful deletion.
- Return HTTP status `404` with the detail `Book not found` when an update or deletion ID does not exist.