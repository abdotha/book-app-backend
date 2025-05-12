# Book App Backend

This is the backend service for the Book App, providing APIs to manage books, users, and related functionalities.

## Features

- CRUD operations for books
- API endpoints for managing user profiles
- Database integration for persistent storage

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/abdotha/book-app-backend.git
    cd book-app-backend
    ```

2. (Recommended) Create and activate a virtual environment:
    ```bash
    python -m venv book_store_venv
    book_store_venv\Scripts\activate
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Set up environment variables:
    Create a `.env` file in the root directory and configure the following:
    ```
    # Example .env for PostgreSQL, FastAPI, and Basic Auth
    DATABASE_URL=postgresql://<username>:<password>@<host>:<port>/<database>
    USERNAME=your_basic_auth_username
    PASSWORD=your_basic_auth_password
    ```

5. Start the server:
    ```bash
    uvicorn app.main:app --reload
    ```

## Project Structure

- `app/main.py` - FastAPI application entry point
- `app/routers/` - API route definitions (books, users, library)
- `app/database.py` - Database connection logic
- `app/schemas.py` - Pydantic models/schemas
- `app/utils.py` - Utility functions
- `books_data.json`, `library_database.xlsx` - Data files

## API Endpoints

| Method | Endpoint                      | Description                                 |
|--------|-------------------------------|---------------------------------------------|
| GET    | /                            | Welcome message                             |
| POST   | /login                       | User login (Basic Auth)                     |
|                                        |                                             |
| **Books**                              |                                             |
| GET    | /books                       | Get all books                               |
| POST   | /books/add                   | Add a new book                              |
| PUT    | /books/update/{book_id}      | Update a book by ID                         |
| DELETE | /books/delete/{book_id}      | Delete a book by ID                         |
| GET    | /books/{book_id}             | Get a book by ID                            |
|                                        |                                             |
| **Users**                              |                                             |
| POST   | /users/purchase              | Get purchased books for a user (by email)   |
| POST   | /users/add/purchase          | Add a purchased book for a user             |
|                                        |                                             |
| **Library**                            |                                             |
| GET    | /library                     | Get all library books                       |
| PUT    | /library/borrow              | Borrow a book                               |
| PUT    | /library/return              | Return a book                               |
| GET    | /library/userbooks           | Get books borrowed by a user (by email)     |
| POST   | /library/add                 | Add a book to the library                   |
| DELETE | /library/delete              | Delete a book from the library (by bookid)  |

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

