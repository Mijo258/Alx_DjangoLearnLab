#!/usr/bin/python3
"""
A script to perform sample queries on the Django models for the library project.
This script must be run within the context of the Django project.
"""

import os
import django
import sys

# Add the project's root directory to the Python path
# This is necessary to make Django models importable.
# The '..' goes up one level from 'relationship_app' to the project root.
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

# Set up the Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

# Now you can import your models!
from models import Author, Book, Library, Librarian

def run_queries():
    """
    Executes the three required queries and prints the results.
    """
    
    # --- Task 1: Query all books by a specific author ---
    print("--- Querying all books by George Orwell ---")
    try:
        # First, get the author object
        orwell = Author.objects.get(name="George Orwell")
        # Then, use the author object to filter the Book model
        orwell_books = Book.objects.filter(author=orwell)
        
        if orwell_books.exists():
            for book in orwell_books:
                print(f"- {book.title}")
        else:
            print("No books found by George Orwell.")
    except Author.DoesNotExist:
        print("Author 'George Orwell' not found in the database.")

    print("\n" + "-"*30 + "\n")

    # --- Task 2: List all books in a library ---
    print("--- Listing all books in 'City Central Library' ---")
    try:
        # First, get the library object
        central_library = Library.objects.get(name="City Central Library")
        # Access the ManyToManyField 'books' directly
        library_books = central_library.books.all()

        if library_books.exists():
            for book in library_books:
                print(f"- {book.title} by {book.author.name}")
        else:
            print("No books found in this library.")
    except Library.DoesNotExist:
        print("Library 'City Central Library' not found.")
        
    print("\n" + "-"*30 + "\n")
    
    # --- Task 3: Retrieve the librarian for a library ---
    print("--- Retrieving the librarian for 'City Central Library' ---")
    try:
        # Get the library object again
        central_library = Library.objects.get(name="City Central Library")
        # Access the OneToOne reverse relationship. Django creates this automatically.
        # The related name is the lowercase name of the related model.
        librarian = central_library.librarian
        
        print(f"The librarian is: {librarian.name}")
    except Library.DoesNotExist:
        print("Library 'City Central Library' not found.")
    except Librarian.DoesNotExist:
        # This will be raised if the library exists but has no librarian
        print("This library has no assigned librarian.")

# --- This ensures the code only runs when the script is executed directly ---
if __name__ == "__main__":
    # Note: Before running this script, you need to populate your database with
    # some sample data using the Django shell, otherwise the queries won't find anything.
    # For example:
    # author1 = Author.objects.create(name="George Orwell")
    # book1 = Book.objects.create(title="1984", author=author1)
    # library1 = Library.objects.create(name="City Central Library")
    # library1.books.add(book1)
    # librarian1 = Librarian.objects.create(name="Mr. Smith", library=library1)
    run_queries()