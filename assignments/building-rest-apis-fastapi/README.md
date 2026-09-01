# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a REST API for managing a collection of books with the FastAPI framework. Practice defining endpoints, validating request data with Pydantic models, returning appropriate HTTP status codes, and handling missing resources.

## 📝 Tasks

### 🛠️ Create the API and Health Endpoint

#### Description
Complete the FastAPI application setup and add a simple endpoint that confirms the API is running.

#### Requirements
Completed program should:

- Create a FastAPI application in `starter-code.py`.
- Define a `GET /health` endpoint.
- Return `{"status": "ok"}` from the health endpoint with HTTP status `200`.

### 🛠️ Model and List Books

#### Description
Define the shape of a book and create an endpoint that returns all books currently stored by the application.

#### Requirements
Completed program should:

- Define a Pydantic model named `Book` with integer `id`, string `title`, and string `author` fields.
- Store books in the provided in-memory list.
- Define a `GET /books` endpoint that returns the complete list of books.
- Declare `list[Book]` as the response model for the endpoint.

### 🛠️ Create and Retrieve Books

#### Description
Add endpoints that create a book and retrieve one book by its ID. Validate requests and provide a useful response when a requested book does not exist.

#### Requirements
Completed program should:

- Define a `POST /books` endpoint that accepts a valid `Book` request body.
- Add the submitted book to the in-memory list and return it with HTTP status `201`.
- Define a `GET /books/{book_id}` endpoint that returns the matching book.
- Return HTTP status `404` with the message `Book not found` when no matching book exists.
- Confirm the endpoints and request schemas appear in the interactive documentation at `/docs`.
