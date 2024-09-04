# Advanced API Project

## API Endpoints

### Books

- **List Books**: `GET /api/books/`
  - Retrieves a list of all books.
  - Permissions: Open to all users.

- **Retrieve Book**: `GET /api/books/<int:pk>/`
  - Retrieves a single book by its ID.
  - Permissions: Open to all users.

- **Create Book**: `POST /api/books/create/`
  - Creates a new book.
  - Requires authentication.

- **Update Book**: `PUT /api/books/<int:pk>/update/`
  - Updates an existing book.
  - Requires authentication.

- **Delete Book**: `DELETE /api/books/<int:pk>/delete/`
  - Deletes a book.
  - Requires authentication.

## Permissions

- `List` and `Retrieve` views are accessible to all users.
- `Create`, `Update`, and `Delete` views require authentication.
