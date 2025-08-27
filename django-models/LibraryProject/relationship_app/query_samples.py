# Retrieving all books
from models import Book, Author, Library, Librarian
books = Library.objects.get(name = 'libraries').books.all()

# Filtering books by author
books_by_author = Book.objects.filter(author='John Doe')
 
librarians = Librarian.objects.all() 
