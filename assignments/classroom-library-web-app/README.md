# 📘 Assignment: Classroom Library Web App

## 🎯 Objective

Work as a team to build a browser interface for the Book API from the previous FastAPI assignment. Practice creating a responsive page, requesting data with `fetch`, displaying API results, and submitting a form without reloading the page.

## 📝 Tasks

### 🛠️ Build the Library Interface

#### Description
Divide responsibility for HTML, CSS, and JavaScript among team members. Complete the provided page structure so users can scan the library and add a new book.

#### Requirements
Completed program should:

- Include a page heading, a book list, and a form with fields for book ID, title, and author.
- Connect every form label to its input and provide a visible submit button.
- Use `styles.css` to create a readable layout that works at both mobile and desktop widths.
- Serve the frontend at `http://localhost:5500` and configure the FastAPI CORS middleware to allow that origin.
- Record each team member's contribution in an HTML comment at the bottom of `index.html`.

### 🛠️ Load and Display Books

#### Description
Complete `loadBooks` in `app.js`. Request the current collection from the running FastAPI server and turn each returned book into a list item.

#### Requirements
Completed program should:

- Send a `GET` request to `http://localhost:8000/books` with `fetch`.
- Display every returned book's title and author in the book list.
- Show `No books yet. Add the first one!` when the API returns an empty array.
- Show a helpful status message when the request fails.

### 🛠️ Add Books from the Browser

#### Description
Complete `addBook` in `app.js`. Send the form values to the API as JSON, then refresh the visible collection when the API accepts the new book.

#### Requirements
Completed program should:

- Prevent the form's default page reload.
- Send a `POST` request to `http://localhost:8000/books` with the ID as a number and the title and author as strings.
- Include the `Content-Type: application/json` request header.
- Clear the form, display a success message, and reload the book list after a successful response.
- Display an error message when the API returns an unsuccessful response or cannot be reached.