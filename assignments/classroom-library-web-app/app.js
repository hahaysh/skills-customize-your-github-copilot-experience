const API_URL = "http://localhost:8000/books";

const bookList = document.querySelector("#book-list");
const bookForm = document.querySelector("#book-form");
const statusMessage = document.querySelector("#status");

function showBooks(books) {
  bookList.replaceChildren();

  if (books.length === 0) {
    statusMessage.textContent = "No books yet. Add the first one!";
    return;
  }

  statusMessage.textContent = `${books.length} book(s) available`;

  for (const book of books) {
    const item = document.createElement("li");
    item.textContent = `${book.title} by ${book.author}`;
    bookList.append(item);
  }
}

async function loadBooks() {
  // TODO: Fetch the books, convert the response to JSON, and call showBooks.
  // Remember to catch network errors and update statusMessage.
}

async function addBook(event) {
  event.preventDefault();

  // TODO: Read the three form values and POST a JSON book to API_URL.
  // If the request succeeds, reset the form and call loadBooks.
}

bookForm.addEventListener("submit", addBook);
loadBooks();