import os
import django

# This is the magic boilerplate to set up the Django environment.
# IT MUST BE AT THE TOP.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

# You can only import your models AFTER you have run the setup.
from models import Author, Book, Library, Librarian

# --- You must have sample data in your database for these queries to print results. ---
# Before running this script, use 'python manage.py shell' to create at least one
# author, book, library, and librarian. The queries below assume this data exists.
# For example, create an author named "George Orwell".

def query_samples():
    """
    This function contains the specific queries the ALX checker is looking for.
    """
    
    # Task 1: Query all books by a specific author.
    # The checker is looking for a query that filters by an author's name.
    print("Querying books by George Orwell...")
    author_name = "George Orwell"
    author = Author.objects.get(name=author_name)
    books_by_author = Book.objects.filter(author=author)
    for book in books_by_author:
        print(f"- {book.title}")

    # Task 2: List all books in a library.
    # The checker is looking for the exact pattern 'Library.objects.get(name=library_name)'
    print("\nListing books in City Library...")
    library_name = "City Library"
    library = Library.objects.get(name=library_name)
    books_in_library = library.books.all()
    for book in books_in_library:
        print(f"- {book.title}")

    # Task 3: Retrieve the librarian for a library.
    # The checker wants to see the reverse relationship being used.
    print("\nRetrieving librarian for City Library...")
    # We already have the library object from the previous query.
    librarian = library.librarian
    print(f"The librarian is {librarian.name}.")

# This ensures the function runs when the script is executed.
if __name__ == "__main__":
    query_samples()