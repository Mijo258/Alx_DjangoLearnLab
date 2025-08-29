# Update Operation

## Command
```python
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book_to_update.save()

"""
Output
This command has no direct output, but the database is updated.
"""