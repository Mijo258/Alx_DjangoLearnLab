## Permissions and Groups Setup

This project uses Django's built-in groups and permissions system for access control.

### Custom Permissions
The `Book` model defines four custom permissions:
- `can_view_book`: Allows viewing the list of books.
- `can_create_book`: Allows creating a new book entry.
- `can_edit_book`: Allows editing an existing book.
- `can_delete_book`: Allows deleting a book.

### Groups
Three groups are configured in the Django Admin:
1.  **Viewers:** Has only `can_view_book` permission.
2.  **Editors:** Has `can_view_book`, `can_create_book`, and `can_edit_book` permissions.
3.  **Admins:** Has all four permissions, including `can_delete_book`.

### View Enforcement
Views are protected using the `@permission_required` decorator to ensure only users with the correct permissions (via their group) can access certain actions.