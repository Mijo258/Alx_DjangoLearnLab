# Create Operation

## Command
```python
from bookshelf.models import Book
book1 = Book(title="1984", author="George Orwell", publication_year=1949)
book1.save()
"""
Output
This command has no direct output, but the object is created in the database.
"""