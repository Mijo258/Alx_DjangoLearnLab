# Update Operation

## Command
```python
book_to_update = Book.objects.get(title="1984")
book_to_update.title = "Nineteen Eighty-Four"
book_to_update.save()

"""
Output
This command has no direct output, but the database is updated.
"""